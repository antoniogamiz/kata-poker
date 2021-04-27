#!/usr/bin/env bash

TEST_MODULE_PATH=$(echo "$1" | tr / . | sed -r 's/(src\.|\.py)//g' | rev | sed -e 's/\./_tset\./' | rev)
TEST_DIRECTORY="tests"

PYTHONPATH=${workspaceRoot}/src python3 -m unittest "${TEST_DIRECTORY}.${TEST_MODULE_PATH}"
