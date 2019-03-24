FROM python:3.6.8-slim-jessie

WORKDIR /home/user/docker_dev_projects/emaula/site

COPY requirements.txt ./

# install psycopg2 to handle postgresql
RUN apt-get update \
    && apt-get install -y python3-psycopg2

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# test if the database is working, apply migrations and collect static files
ENTRYPOINT ["/home/user/docker_dev_projects/emaula/site/entrypoint.sh"]

WORKDIR emaula
