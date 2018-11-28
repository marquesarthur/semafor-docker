"""
web views for semviz

Author: Sam Thomson (sthomson@cs.cmu.edu)
"""
import os
import sys

from flask import Flask, request, jsonify, render_template
from flask.ext.wtf import Form, TextAreaField, Required

sys.path.append(os.getcwd())  # I thought this happened by default?

from semviz.services import PosTagger, SemaforClient, MaltClient
from semviz.mock import DB_SENTENCE_1, DB_SENTENCE_2, DB_SENTENCE_3
from semviz.settings import CACHE_RESULTS, MONGO_HOST, MONGO_PORT

from pymongo import MongoClient
from pymongo import TEXT

app = Flask(__name__)

SEMAFOR_CLIENT = SemaforClient.create(MaltClient())

# http://containertutorials.com/docker-compose/flask-mongo-compose.html#dockerfile
# https://www.thachmai.info/2015/04/30/running-mongodb-container/
mongo_client = None
if CACHE_RESULTS:
    mongo_client = MongoClient(MONGO_HOST,
                               MONGO_PORT)
    db = mongo_client.semafordb

    db.parsed_frames.create_index([('sentence', TEXT)], name='sentence_text', default_language='english')


class SentenceInputForm(Form):
    sentence = TextAreaField("sentence", validators=[Required()])


@app.route("/api/v1/parse")
def parse():
    text = request.args.get('sentence', '')
    if CACHE_RESULTS:
        query = '\"' + '\" \"'.join(text.split(' ')) + '\"' # https://stackoverflow.com/questions/16902674/mongodb-text-search-and-multiple-search-words
        cached_response = db.parsed_frames.find({
            "$text": {
                "$search": query
            }
        })
        if cached_response and cached_response.count() == 1:
            result = next(iter(cached_response))
            return jsonify(result["frames"])

    response = SEMAFOR_CLIENT.get_parses(text.split(u'\n'))

    if CACHE_RESULTS:
        db.parsed_frames.insert({"sentence": text, "frames": response})

    return jsonify(response)


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route("/")
def home():
    form = SentenceInputForm(request.args, csrf_enabled=False)
    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
