FROM ubuntu:16.04

MAINTAINER Your Name "cyril.nleng@dell.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /webhook/requirements.txt

WORKDIR /webhook

RUN pip install -r requirements.txt

COPY . /webhook

ENTRYPOINT [ "python" ]

CMD [ "webhook.py" ]

