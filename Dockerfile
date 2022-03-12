FROM tiangolo/meinheld-gunicorn-flask:python3.9

COPY ./zione /app
COPY ./wsgi.py /app
COPY ./requirements/prod-req.txt /app/requirements.txt

RUN pip install --upgrade --no-cache-dir pip psycopg[binary]
RUN pip install --no-cache-dir -r requirements.txt
