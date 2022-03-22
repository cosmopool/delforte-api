FROM tiangolo/meinheld-gunicorn-flask:python3.9

COPY ./zione/ /app/zione/
COPY ./main.py /app
COPY ./setup.py /app
# COPY ./gunicorn_conf.py /
COPY ./requirements/prod-req.txt /app/requirements.txt

ENV APP_MODULE "main:app"
ENV MODULE_NAME "main"
ENV VARIABLE_NAME "app"
ENV PORT 8080

RUN python setup.py bdist_wheel
RUN pip install --no-cache-dir dist/*.whl
RUN rm -rf build dist zione.egg-info
