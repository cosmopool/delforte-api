postgres:
	podman run --name=postgres -e POSTGRES_USER=zione -e POSTGRES_PASSWORD=test_pass -e POSTGRES_DB=test -e PGDATA=/var/lib/postgresql/data/pgdata -v ./container/db_scripts/init.sql:/docker-entrypoint-initdb.d/init.sql --restart="always" -d -p 5432:5432 postgres:14.0

postgres-rm:
	podman stop postgres
	podman rm postgres

init-db:
	psql -h localhost -p 5432 -U zione -d test -f container/db_scripts/init.sql

test:
	pytest -vv --cov . .
