#!/bin/sh

export FLASK_ENV="development"
export FLASK_APP="app.py"
export SECRET_KEY="a1b64b4563065c3f60d28aa13744351040d1a25137a42a984770cc2b099f1520"
export APP_SETTINGS="development"
export DF_API_KEY="DF-735016e0ea232c4b7450cd292f4a204f1b8e1318d100d298e86f3d43cc081206"
export API_VERSION="1"
export APP_HOST="10.5.40.40"
export APP_PORT="5000"
export SECRET="a1b64b4563065c3f60d28aa13744351040d1a25137a42a984770cc2b099f1520"
export BASE_URL="http://localhost:5000/"
export DATABASE_URL="postgresql://129.151.35.221/test_db"
export DATABASE_PASS="masktrum(sapiencia)19812"
export DATABASE_USER="zione"
export DATABASE_HOST_PORT="5432"
export DATABASE_PORT="5432"
export DATABASE_HOST="152.67.42.19"
export DATABASE_NAME="test"
export POSTGRES_VERSION="14.0"

uwsgi --ini app.ini
