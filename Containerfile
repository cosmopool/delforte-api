# FROM python:3.9.9-alpine3.15
FROM python:3.9.9

ENV PROJECT_DIR=/app

WORKDIR $PROJECT_DIR

COPY . $PROJECT_DIR/.

RUN pip install flask flask-restful flask-jwt-extended marshmallow psycopg
# RUN pip install -r requirements.txt
RUN pip install -e .

# ENV FLASK_ENV="development"
ENV FLASK_ENV="production"
ENV FLASK_APP="/app/app.py"
# ENV SECRET_KEY="a1b64b4563065c3f60d28aa13744351040d1a25137a42a984770cc2b099f1520"
# ENV APP_SETTINGS="development"
# ENV DF_API_KEY="DF-735016e0ea232c4b7450cd292f4a204f1b8e1318d100d298e86f3d43cc081206"
# ENV API_VERSION="1"
ENV SECRET="a1b64b4563065c3f60d28aa13744351040d1a25137a42a984770cc2b099f1520"
# ENV BASE_URL="http://localhost:5000/"
# ENV DATABASE_URL="postgresql://localhost/test_db"
ENV DATABASE_PASS="masktrum(sapiencia)19812"
ENV DATABASE_USER="zione"
ENV DATABASE_PORT="5432"
ENV DATABASE_HOST="0.0.0.0"
ENV DATABASE_NAME="test"
ENV POSTGRES_VERSION="14.0"

EXPOSE 5000

# CMD [ "flask","run", "--host=0.0.0.0", "--port=5000" ]
# CMD [ "python3", "app.py", "--host=0.0.0.0" ]
# CMD python3 /app/app.py --host=0.0.0.0
CMD flask run --host=0.0.0.0
