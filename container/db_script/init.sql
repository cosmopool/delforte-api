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
	  "service_type" text NOT NULL,
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
  INSERT INTO tickets (client_name, client_phone, client_address, service_type, description, is_finished) VALUES ('Gustavo Micaloski', 41666222888, 'Rua Minecraft, 654', 'Instalacao', 'Instalar o Minecraft', false);
  INSERT INTO appointments (date, time, duration, ticket_id, is_finished) VALUES ('10-05-2022', '11:30', '01:00', 1, false);

  CREATE VIEW appointments_view AS SELECT id, date, time, duration, ticket_id AS "ticketId", is_finished AS "isFinished" FROM appointments;
  CREATE VIEW tickets_view AS SELECT id, client_name AS "clientName", client_phone AS "clientPhone", client_address AS "clientAddress", service_type AS "serviceType", description, is_finished AS "isFinished" FROM tickets;
  CREATE VIEW agenda_view AS SELECT t1.id, t1.date, t1.time, t1.duration, t1.is_finished AS "isFinished", t2.id AS "ticketId", t2.client_name AS "clientName", t2.client_address AS "clientAddress", t2.client_phone AS "clientPhone", t2.description, t2.is_finished AS "ticketIsFinished" FROM appointments AS t1 LEFT JOIN tickets AS t2 ON t1.ticket_id = t2.id;

