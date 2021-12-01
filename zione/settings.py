import os

HOST = os.environ['DATABASE_HOST']
PORT = os.environ['DATABASE_PORT']
USER = os.environ['DATABASE_USER']
PASSWORD = os.environ['DATABASE_PASS']
DB_NAME = os.environ['DATABASE_NAME']
CONNECTION = f"host={HOST} port={PORT} user={USER} password={PASSWORD} dbname={DB_NAME}"
