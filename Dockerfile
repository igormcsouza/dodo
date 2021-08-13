FROM python:3.8-slim

COPY requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

WORKDIR /dodo

COPY /app /dodo/app
COPY wsgi.py /dodo/wsgi.py

CMD gunicorn -b 0.0.0.0:5000 wsgi:app