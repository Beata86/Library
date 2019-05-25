FROM python:3.6.7

ARG APP_DIR=/usr/src/library

WORKDIR /tmp
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p $APP_DIR
ADD src/ $APP_DIR/src/

WORKDIR /usr/src/library
CMD PYTHONPATH=$PYTHONPATH:. \
	FLASK_APP=src.api flask run --host=0.0.0.0
