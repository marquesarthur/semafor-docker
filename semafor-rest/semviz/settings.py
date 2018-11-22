"""
Author: Sam Thomson (sthomson@cs.cmu.edu)
        Lingpeng Kong (lingpenk@cs.cmu.edu)
"""

# SEMAFOR server settings
SEMAFOR_HOST = "localhost"
SEMAFOR_PORT = 8085

# Location of MaltParser and POS tagger executables
SEMAFOR_HOME = "/semafor-master"

# MST Parser server settings
MST_HOST = "localhost"
MST_PORT = 12345

# caching parsed sentences in key-value NoSQL database
CACHE_RESULTS = True
MONGO_HOST = "mongodb://localhost"
MONGO_PORT = 27017
