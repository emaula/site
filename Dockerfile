FROM python:3.6.8-slim-jessie

COPY requirements.txt ./

# install psycopg2 to handle postgresql
RUN apt-get update \
    && apt-get install -y python3-psycopg2

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# test if the database is working, apply migrations and collect static files
ENTRYPOINT ["/entrypoint.sh"]

WORKDIR emaula
