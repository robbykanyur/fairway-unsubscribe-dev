FROM python:3.6-alpine
RUN adduser -D unsubscribe

WORKDIR /home/unsubscribe

RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev openssl-dev make

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql

RUN apk del .build-deps gcc musl-dev libffi-dev openssl-dev make

COPY boot.sh boot.dev.sh ./
RUN chmod +x boot*

RUN chown -R unsubscribe:unsubscribe ./
USER unsubscribe
