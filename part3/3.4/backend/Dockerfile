FROM golang:1.16-alpine

EXPOSE 8080

COPY /example-backend /app

WORKDIR /app

ENV REQUEST_ORIGIN=http://localhost:5000

RUN go build && \
    adduser -S appuser

USER appuser

CMD [ "./server" ]

