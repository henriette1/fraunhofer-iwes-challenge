FROM python:3.9.7-bullseye

ADD . /python-app
WORKDIR /python-app

# install psycopg2 library with PIP
COPY python-app/requirements.txt /python-app/requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 5432
CMD [ "python3", "-u", "python-app/iwes-app.py"]