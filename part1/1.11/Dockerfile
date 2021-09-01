FROM openjdk:16-alpine

EXPOSE 8080

RUN apk update && apk upgrade
RUN apk add git
RUN git clone https://github.com/docker-hy/material-applications.git

WORKDIR /material-applications/spring-example-project

RUN ./mvnw package

CMD java -jar ./target/docker-example-1.1.3.jar

