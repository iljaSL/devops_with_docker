FROM golang:1.16-alpine AS build-env

COPY /example-backend /app

WORKDIR /app

RUN go build

FROM alpine:latest

WORKDIR /app

EXPOSE 8080

ENV REQUEST_ORIGIN=http://localhost:5000

COPY --from=build-env /app/server /app

RUN adduser -S appuser

USER appuser

CMD [ "./server" ]

