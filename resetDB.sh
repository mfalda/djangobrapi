#!/bin/bash

rm -f tmp.db db.sqlite3
rm -r $1/migrations
python manage.py makemigrations $1
python manage.py migrate $1
python manage.py createsuperuser
