#!/bin/sh
# verifies Postgres is healthy before running migrations and Django
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    # while net cat doesn't have a response from Postgres
    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate
# python manage.py seed

exec "$@"
