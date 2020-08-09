FROM python:3.6.11-slim-buster

COPY requirements ./requirements/

# install psycopg2 to handle postgresql
RUN apt-get update \
    && apt-get install -y python3-psycopg2

RUN pip install --no-cache-dir -r requirements/production.txt

COPY . .

# test if the database is working, apply migrations and collect static files
ENTRYPOINT ["/entrypoint.sh"]

WORKDIR emaula
