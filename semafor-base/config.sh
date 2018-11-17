#!/bin/sh
######################## ENVIRONMENT VARIABLES ###############################
######### change the following according to your own local setup #############


# assumes this script (config.sh) lives in "${BASE_DIR}/semafor/bin/"
export BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/../.." > /dev/null && pwd )"
# path to the absolute path
# where you decompressed SEMAFOR.
export SEMAFOR_HOME="${BASE_DIR}/semafor-master"

export CLASSPATH=".:${SEMAFOR_HOME}/target/Semafor-3.0-alpha-04.jar"

# Change the following to the bin directory of your $JAVA_HOME
export JAVA_HOME_BIN="/usr/bin"

# Change the following to the directory where you decompressed
# the models for SEMAFOR 2.0.
export MALT_MODEL_DIR="${BASE_DIR}/models/semafor_malt_model_20121129"
export TURBO_MODEL_DIR="{BASE_DIR}/models/turbo_20130606"


