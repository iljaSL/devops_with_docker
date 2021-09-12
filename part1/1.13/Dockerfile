FROM golang:1.16

EXPOSE 8080

COPY /example-backend /app

WORKDIR /app

RUN go build

CMD [ "./server" ]
