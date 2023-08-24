FROM python:3.11

RUN mkdir /fastapi_app

RUN mkdir /data

WORKDIR /fastapi_app

ADD . /fastapi_app

RUN pip install -v /fastapi_app

RUN chmod a+x docker/*.sh

CMD /fastapi_app/docker/app.sh

