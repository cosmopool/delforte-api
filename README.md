[![codecov](https://codecov.io/gh/cosmopool/delforte-api/branch/master/graph/badge.svg?token=UTEH40FB51)](https://codecov.io/gh/cosmopool/delforte-api)

## Instalation

The api was setup to run on containers, so that's the easier way to deploy.
You will need at least three things to run the api: a webserver, reverse proxy and postgres database.

### Deploy
Deploy via containers with podman.

First, you need to prepare your ssl certificates:
Copy you ssl certificates to folder `container/ssl/` and point `ssl_certificate` and `ssl_certificate_key` properties in `container/nginx/nginx.conf` accordingly.
If you don't want or have an ssl certificate, just configure `container/nginx/nginx.conf` or don't use nginx container.

create a pod:
```
podman pod create --name delforte-api -p 80:80 -p 443:443 -p 5423:5432
```

build images:
```
cd /project/root/folder
make build
```

#### Environment variables

Set environment variables:
- `$DATABASE_USER`
- `$DATABASE_PASS`
- `$DATABASE_HOST`
- `$DATABASE_PORT`
- `$DATABASE_NAME`

#### Database setup

Requirements:
- database credentials environment variables setup
- empty directory `/$HOME/data` for the database (you can change it!)

create database container:
```
podman run --name=postgres -e POSTGRES_USER=$DATABASE_USER -e POSTGRES_PASSWORD=$DATABASE_PASS -e POSTGRES_DB=$DATABASE_NAME -e PGDATA=/var/lib/postgresql/data/pgdata -v /$HOME/data/database/:/var/lib/postgresql/data:z -v /$HOME/api/scripts/:/docker-entrypoint-initdb.d:z --restart="always" --pod delforte-api -d postgres:13-alpine
```

#### API setup

create nginx container:
```
podman run --name=nginx --restart="always" --pod delforte-api -d api_nginx
```

#### API setup

Requirements:
- database credentials environment variables setup

create api container:
```
podman run --name=zione-api -e DATABASE_PORT=5432 -e DATABASE_HOST=$DATABASE_HOST -e DATABASE_USER=$DATABASE_USER -e DATABASE_PASS=$DATABASE_PASS -e DATABASE_NAME=$DATABASE_NAME -e SECRET_KEY=$SECRET_KEY --restart="always" --pod delforte-api zione-api
```

That's it, you can now send requests to the server hosting the api. Have fun 💃.
