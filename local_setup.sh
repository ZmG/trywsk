#!/bin/bash

## This file is intended to help you setup your local environment for development on this site

# Create your local database (is sqlite by default)
./manage.py syncdb

# Migrations
./manage.py migrate

# Create cache table, If you are moving this to a new production environment, please also run it there!
# ./manage.py createcachetable cachetable
./manage.py createcachetable dbcache1 --database=default

./manage.py loaddata base/fixtures/base_initial.json 
./manage.py loaddata base/fixtures/TeamMember-update1.json
