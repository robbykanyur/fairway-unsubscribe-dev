FROM node:11.14.0-alpine

COPY package.json /home/node

RUN apk add --no-cache --virtual .build-deps gcc g++ make autoconf automake libtool nasm build-base zlib-dev
RUN cd /home/node && npm install
RUN apk del .build-deps gcc g++ make autoconf automake libtool nasm build-base zlib-dev

COPY assets.sh assets.dev.sh ./
RUN chmod +x ./assets*
