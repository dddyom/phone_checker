FROM python:bullseye
RUN apt update -y && apt upgrade -y

WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./app ./app
