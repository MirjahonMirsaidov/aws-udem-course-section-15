FROM python:3.10.4

RUN apt-get update -y
RUN apt-get -y install binutils libproj-dev gdal-bin

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/

RUN pip install -r requirements.txt

ADD . /code/
WORKDIR /code/src

ENTRYPOINT ["sh", "-c", "python manage.py migrate && \
                         python manage.py createcachetable && \
                         daphne -b 0.0.0.0 -p 80 core.asgi:application"]