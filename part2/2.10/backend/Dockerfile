FROM golang:1.16

COPY /example-backend /app

WORKDIR /app

RUN go build

CMD [ "./server" ]

