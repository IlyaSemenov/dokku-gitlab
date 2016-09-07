#!/bin/bash
set -e
eval "$(dokku-vars.py)"
exec entrypoint.sh "$@"
