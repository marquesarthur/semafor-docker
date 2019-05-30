"""
Author: Sam Thomson (sthomson@cs.cmu.edu)
        Lingpeng Kong (lingpenk@cs.cmu.edu)
"""
import os

# SEMAFOR server settings
SEMAFOR_HOST = os.environ.get('DOCKER_HOST') if os.environ.get('DOCKER_HOST') else "localhost"
SEMAFOR_PORT = 8085

# Location of MaltParser and POS tagger executables
SEMAFOR_HOME = "/semafor-master"

# MST Parser server settings
MST_HOST = os.environ.get('DOCKER_HOST') if os.environ.get('DOCKER_HOST') else "localhost"
MST_PORT = 12345

# caching parsed sentences in key-value NoSQL database
CACHE_RESULTS = str(os.environ.get('CACHE_RESULTS')).lower() == 'true' if os.environ.get('CACHE_RESULTS') else False
MONGO_HOST = "mongodb://{}".format(os.environ.get('DOCKER_HOST'))
MONGO_PORT = 27017
