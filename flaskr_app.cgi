#!/usr/local/bin/python3
import sys
sys.path.insert(0, '/Users/troy/Library/Python/3.6/lib/python/site-packages')
from wsgiref.handlers import CGIHandler
from flaskr import app

CGIHandler().run(app)
