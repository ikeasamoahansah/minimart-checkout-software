#!/bin/bash

# exec source venv/bin/activate
exec python3 -m unittest tests
exec python3 database.py
