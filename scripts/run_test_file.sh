#!/usr/bin/env bash

TEST_DIRECTORY="tests"

FILE=$1

if [[ $1 == src/tests* ]] ;
then
    SRC_MODULE_PATH=$(echo "$FILE" | tr / . | sed -r 's/(src\.|\.py)//g')
    MODULE_TO_RUN="${SRC_MODULE_PATH}"
else
    echo "Running test file"
    TEST_MODULE_PATH=$(echo "$FILE" | tr / . | sed -r 's/(src\.|\.py)//g' | rev | sed -e 's/\./_tset\./' | rev)
    MODULE_TO_RUN="${TEST_DIRECTORY}.${TEST_MODULE_PATH}"
fi

PYTHONPATH=${workspaceRoot}/src python3 -m unittest $MODULE_TO_RUN
