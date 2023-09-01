#!/bin/bash

cp .env.example .env

poetry config virtualenvs.in-project true
poetry install
mkdir -p /logs
chown -R python:python logs
python manage.py seeds
tail -f /dev/null