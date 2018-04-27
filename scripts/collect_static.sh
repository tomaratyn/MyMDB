#!/usr/bin/env bash

root=$1
source $root/venv/bin/activate

export DJANGO_CACHE_TIMEOUT=100
export DJANGO_SECRET_KEY=FAKE_KEY
export DJANGO_SETTINGS_MODULE=config.production_settings
export DJANGO_LOG_FILE=/var/log/mymdb/mymdb.log
cd $root/django/

python manage.py collectstatic
