"""
Author: Sam Thomson (sthomson@cs.cmu.edu)
        Lingpeng Kong (lingpenk@cs.cmu.edu)
"""
import codecs
import json
import os
import socket
from subprocess import Popen, PIPE
import sys
from tempfile import mkdtemp
from threading import Lock

from semviz.conll_to_json import encode_conll
from semviz.pos_to_conll import pos_to_conll
from semviz.settings import SEMAFOR_HOST, SEMAFOR_PORT, SEMAFOR_HOME
from semviz.utils import reshape, deleting, timer

NUM_CONLL_FIELDS = 10
DEFAULT_BUFFER_SIZE = 8192
DEFAULT_TIMEOUT = 20.0
UTF_8 = 'utf8'


class SocketClient(object):
    """ A client for interacting with a running TCP socket server. """
    def __init__(self, host, port, buffer_size=DEFAULT_BUFFER_SIZE, timeout=DEFAULT_TIMEOUT):
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.timeout = timeout

    def make_request(self, request):
        """
        Sends request to the server and gets the server's response.
        End of response is indicated by an empty string.
        Opens and closes a new connection for each request.
        """
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(self.timeout)
        client.connect((self.host, self.port))
        client.sendall(request)
        client.shutdown(socket.SHUT_WR)
        response = []
        while True:
            chunk = client.recv(self.buffer_size)
            if not chunk:
                break
            response.append(chunk)
        return ''.join(response)


class UnicodeSocketClient(SocketClient):
    """
    A client for interacting with a running TCP socket server.
    Requests and responses are encoded and decoded as utf8
    """

    def make_request(self, request):
        """ Sends request to the server and gets the server's response. """
        response = super(UnicodeSocketClient, self).make_request(request.encode(UTF_8))
        return response.decode(UTF_8)


class SemaforClient(object):
    """
    A client for retrieving frame-semantic parses from a running SEMAFOR
    server.
    """
    def __init__(self, dependency_parser, socket_client):
        """
        Creates a new client with the given dependency parser, connection to
        a running SEMAFOR server.
        """
        self._dependency_parser = dependency_parser
        self._client = socket_client

    @staticmethod
    def create(dependency_parser, host=SEMAFOR_HOST, port=SEMAFOR_PORT):
        """ Convenience static constructor """
        return SemaforClient(dependency_parser, UnicodeSocketClient(host, port))

    def get_parses(self, sentences):
        """
        Gets frame-semantic parses as a list of dicts from a list of sentence
        strings.
        """
        with timer() as dep_timer:
            dependency_parses = self._dependency_parser.get_parses(sentences)
        conll_parses = dependency_parses.split('\n\n')
        brat_ready_parses = [encode_conll(parse) for parse in dependency_parses.split('\n\n')]
        with timer() as frame_timer:
            sentences = self._get_parses_from_conll(dependency_parses)
        for sentence, conll, parse in zip(sentences, conll_parses, brat_ready_parses):
            sentence.update(parse)
            sentence['conll'] = conll
        return {
            "sentences": sentences,
            "debug_info": {
                "dependency_parser_elapsed_seconds": dep_timer['seconds'],
                "frame_parser_elapsed_seconds": frame_timer['seconds'],
            },
        }

    def _get_parses_from_conll(self, dependency_parses):
        """
        Gets frame-semantic parses as a list of dicts from dependency-parsed
        English sentences in conll format.
        """
        response = self._client.make_request(dependency_parses)
        return [json.loads(x) for x in response.splitlines()]


class PosTagger(object):
    """ A client for running tokenization and part-of-speech tagging """
    def tag_sentences(self, sentences):
        """ Runs tokenization and part-of-speech tagging a sentence str. """
        #TODO: could probably just use nltk
        with deleting(mkdtemp(suffix='XXXXXX', prefix='semafor.')) as temp_dir:
            input_filename = os.path.join(temp_dir, "sentence")
            output_filename = os.path.join(temp_dir, "pos.tagged")
            with codecs.open(input_filename, 'w', encoding="utf8") as input_file:
                input_file.write(u'\n'.join(sentences))
            os.system("cd %s && ./tokenize_and_postag.sh %s %s" %
                      (TAGGING_SCRIPT_HOME, input_filename, output_filename))
            with codecs.open(output_filename, encoding="utf8") as output_file:
                output = output_file.read()
            return output



class MaltClient(object):
    """
    A client for retrieving dependency parses from a MaltParser executable
    """
    def get_parses(self, sentences):
        """ Gets a dependency semantic parse as conll from a sentence str. """
        # TODO: server version of Malt?
        with deleting(mkdtemp(suffix='XXXXXX', prefix='semafor.')) as temp_dir:
            input_filename = os.path.join(temp_dir, "sentence")
            output_filename = os.path.join(temp_dir, "conll")
            with codecs.open(input_filename, 'w', encoding="utf8") as input_file:
                input_file.write(u'\n'.join(sentences))
            os.system("cd %s && ./bin/runMalt.sh %s %s" %
                      (SEMAFOR_HOME, input_filename, temp_dir))
            with codecs.open(output_filename, encoding="utf8") as output_file:
                output = output_file.read()
            return output


