#!/bin/bash

cp .env.example .env

poetry config virtualenvs.in-project true
poetry install
mkdir -p /logs
chown -R python:python logs
poetry shell
.venv/bin/python manage.py migrate
.venv/bin/python manage.py seeds
tail -f /dev/null