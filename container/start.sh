#!/bin/sh

# app variables
export FLASK_ENV="development"
export FLASK_APP="app.py"
export APP_SETTINGS="development"
export APP_HOST="10.5.40.40"
export APP_PORT="5000"
export API_VERSION="1"

# secret variables
export SECRET_KEY="a1b64b4563065c3f60d28aa13744351040d1a25137a42a984770cc2b099f1520"
export SECRET="a1b64b4563065c3f60d28aa13744351040d1a25137a42a984770cc2b099f1520"

# database production variables
export DATABASE_PASS="masktrum(sapiencia)19812"
export DATABASE_USER="zione"
export DATABASE_PORT="5432"
export DATABASE_HOST="152.67.42.19"
export DATABASE_NAME="test"
export POSTGRES_VERSION="14.0"
# database test variables
export APP_PORT_TEST="5000"
export APP_HOST_TEST="10.5.40.40"
export DATABASE_PASS_TEST="test_pass"
export DATABASE_HOST_TEST="0.0.0.0"
export DATABASE_NAME_TEST="test"
# database development variables
export APP_PORT_DEVEL="5000"
export APP_HOST_DEVEL="10.5.40.40"
export DATABASE_PASS_DEVEL="devel_pass"
export DATABASE_NAME_DEVEL="devel"
export DATABASE_HOST_DEVEL="0.0.0.0"

uwsgi --ini app.ini
