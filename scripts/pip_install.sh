#!/usr/bin/env bash

root=$1
source $root/venv/bin/activate

pip3 install -r $root/requirements.production.txt