#!/usr/bin/env python3

import json
import os
from urllib.parse import urlparse


def print_var(var, value):
	print('export {}={}'.format(var, json.dumps(value)))

db_url = os.getenv('DATABASE_URL')
if not db_url:
	raise Exception("DATABASE_URL not set. Did you run dokku postgres:link?")
db = urlparse(db_url)
db_adapter_map = {'postgres': 'postgresql', 'mysql': 'mysql2'}
db_adapter = db_adapter_map.get(db.scheme)
if not db_adapter:
	raise Exception("Unsupported database: {} (supported: {})".format(db.scheme, ", ".join(sorted(db_adapter_map.keys()))))
print_var('DB_ADAPTER', db_adapter)
print_var('DB_HOST', db.hostname)
print_var('DB_PORT', db.port or 5432)
print_var('DB_USER', db.username)
print_var('DB_PASS', db.password)
print_var('DB_NAME', db.path[1:])

redis_url = os.getenv('REDIS_URL')
if not redis_url:
	raise Exception("REDIS_URL not set. Did you run dokku redis:link?")
redis = urlparse(redis_url)
print_var('REDIS_HOST', redis.hostname)
print_var('REDIS_PORT', redis.port)
