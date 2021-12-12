FROM node:14-alpine as build-env

WORKDIR /app

COPY . /app

RUN npm install

FROM alpine:latest

WORKDIR /app

RUN apk add nodejs npm && \
    adduser -S appuser

COPY --from=build-env ./app ./build-env

USER appuser

CMD [ "npm", "start" ]

