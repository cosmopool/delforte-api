CREATE TABLE "users" (
  "id" smallserial PRIMARY KEY,
  "username" varchar UNIQUE NOT NULL,
  "password" text NOT NULL
);

CREATE TABLE "tickets" (
  "id" bigserial PRIMARY KEY,
  "client_name" text NOT NULL,
  "client_phone" text NOT NULL,
  "service_type_id" varchar(10) NOT NULL,
  "description" text NOT NULL,
  "is_finished" bool
);

CREATE TABLE "appointments" (
  "id" bigserial PRIMARY KEY,
  "date" date NOT NULL,
  "time" time NOT NULL,
  "duration" interval NOT NULL,
  "ticket_id" bigserial,
  "is_finished" bool
);

ALTER TABLE "appointments" ADD FOREIGN KEY ("ticket_id") REFERENCES "tickets" ("id");

CREATE INDEX ON "users" ("username");

CREATE INDEX ON "appointments" ("date");
