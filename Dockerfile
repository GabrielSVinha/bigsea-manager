FROM alpine:3.6

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    gcc \
    linux-headers \
    libc-dev \
    libffi-dev \
    make \
    openssl-dev

RUN pip install tox setuptools

WORKDIR /usr/asperathos/

COPY . .

CMD [ "sh", "run.sh" ]