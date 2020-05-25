FROM python:3.8.0-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create the app user
RUN addgroup -S bogdan && adduser -S bogdan -G bogdan

WORKDIR /blog

RUN pip install --upgrade pip
COPY ./requirements.txt ./
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt

COPY . .

RUN chown -R bogdan:bogdan /blog
USER bogdan
