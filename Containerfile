FROM python:3.9-bullseye

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt
RUN pip install uwsgi

# CMD ["uwsgi", "--ini, "app.ini"]
CMD uwsgi --ini app.ini
