FROM python:3.12-alpine

RUN apk update && apk add python3 py3-pip
RUN python3 -m venv python-app
RUN source python-app/bin/activate
RUN pip install Flask

COPY ./src /src


CMD python3 src/app.py