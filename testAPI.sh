#!/bin/bash
./manage.py test brapi/tests/ --pattern "$1" -v 2
