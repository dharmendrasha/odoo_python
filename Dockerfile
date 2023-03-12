FROM python:3.10.10-alpine3.16 as base

WORKDIR /package

COPY . .

RUN apk update && apk upgrade \
    && apk add --no-cache bash \
    pkgconfig \
    git \
    gcc \
    openldap \
    libcurl \
    gpgme-dev \
    libc-dev \
    && rm -rf /var/cache/apk/* \
    && pip install -e .
