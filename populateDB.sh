#!/bin/bash

python manage.py makemigrations brapi
python manage.py migrate brapi
python manage.py populate_db brapi/data
