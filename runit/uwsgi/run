#!/usr/bin/env bash

source /mymdb/venv/bin/activate

export PGPASSWORD="$DJANGO_DB_PASSWORD"
psql \
    -h "$DJANGO_DB_HOST" \
    -p "$DJANGO_DB_PORT" \
    -U "$DJANGO_DB_USER" \
    -d "$DJANGO_DB_NAME"

if [[ $? != 0 ]]; then
    echo "no db server"
    exit 1
fi

pushd /mymdb/django

python manage.py migrate

if [[ $? != 0 ]]; then
    echo "can't migrate"
    exit 2
fi

popd

exec /sbin/setuser www-data \
    uwsgi \
    --ini /etc/uwsgi/apps-enabled/mymdb.ini \
    >> /var/log/uwsgi/mymdb.log \
    2>&1