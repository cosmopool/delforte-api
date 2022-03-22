postgres:
	podman run --name=postgres -e POSTGRES_USER=zione -e POSTGRES_PASSWORD=test_pass -e POSTGRES_DB=test -v ./container/db_script/init.sql:/docker-entrypoint-initdb.d/init.sql --restart="always" -d -p 5432:5432 postgres:13-alpine

postgres-rm:
	podman rm postgres --force

init-db:
	psql -h localhost -p 5432 -U zione -d test -f container/db_script/init.sql

test:
	pytest -vv --cov . .

build:
	podman build --layers --force-rm --tag zione-api .
	podman build --layers --force-rm --tag api_nginx -f container/nginx/.

api-test:
	podman pod create --name delforte-api -p 80:80 -p 443:443 -p 5423:5432
	podman run --name=postgres -e POSTGRES_USER=zione -e POSTGRES_PASSWORD=test_pass -e POSTGRES_DB=test -v ./container/db_script/init.sql:/docker-entrypoint-initdb.d/init.sql --restart="always" -d --pod delforte-api postgres:13-alpine
	podman run --name=nginx --restart="always" --pod delforte-api -d api_nginx
	podman run --name=zione-api -e DATABASE_PORT=5432 -e DATABASE_HOST=0.0.0.0 -e DATABASE_USER=zione -e DATABASE_PASS=test_pass -e DATABASE_NAME=test -e SECRET_KEY=asdfasdfasdfasd --restart="always" --pod delforte-api -d zione-api
