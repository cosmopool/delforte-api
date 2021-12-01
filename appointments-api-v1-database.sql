#!/bin/bash
set -e

DATABASE_USER="zione"
DATABASE_NAME="test"
DATABASE_HOST="0.0.0.0"
DATABASE_PASS="masktrum(sapiencia)19812"
PGPASSWORD="masktrum(sapiencia)19812"

psql -v ON_ERROR_STOP=1 -U $DATABASE_USER -d $DATABASE_NAME -h $DATABASE_HOST <<-EOSQL
	CREATE TABLE "users" (
	  "id" smallserial PRIMARY KEY,
	  "username" varchar UNIQUE NOT NULL,
	  "password" text NOT NULL
	);
	
	CREATE TABLE "tickets" (
	  "id" bigserial PRIMARY KEY,
	  "client_name" text NOT NULL,
	  "client_phone" text NOT NULL,
	  "client_address" text NOT NULL,
	  "description" text NOT NULL,
	  "is_finished" bool DEFAULT false
	);
	
	CREATE TABLE "appointments" (
	  "id" bigserial PRIMARY KEY,
	  "date" date NOT NULL,
	  "time" time NOT NULL,
	  "duration" interval NOT NULL,
	  "ticket_id" bigserial,
	  "is_finished" bool DEFAULT false
	);

	ALTER TABLE "appointments" ADD FOREIGN KEY ("ticket_id") REFERENCES "tickets" ("id");
	
	CREATE INDEX ON "users" ("username");
	
	CREATE INDEX ON "appointments" ("date");

	CREATE EXTENSION pgcrypto;

	INSERT INTO users (username, password) VALUES ('kaio', crypt('kaio123', gen_salt('bf')));
EOSQL
