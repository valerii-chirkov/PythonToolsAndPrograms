#!/usr/bin/env bash

python -m unittest

coverage run --source=bot,handlers,settings -m unittest
coverage report

psql -c 'create database chatbot'
psql -d chatbot
