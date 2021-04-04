FROM python:3.9-alpine

RUN apk add --no-cache linux-headers g++ postgresql-dev gcc build-base linux-headers ca-certificates python3-dev libffi-dev libressl-dev libxslt-dev

RUN pip3 install wheel uwsgi

COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

COPY ./uwsgi.ini /app/

COPY ./app /app

WORKDIR /app

CMD ["uwsgi", "--ini", "/app/uwsgi.ini"]