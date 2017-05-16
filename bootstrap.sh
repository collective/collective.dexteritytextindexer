#!/bin/sh
rm -r ./lib ./include ./local ./bin
virtualenv --clear .
./bin/pip install -r requirements.txt
./bin/buildout
