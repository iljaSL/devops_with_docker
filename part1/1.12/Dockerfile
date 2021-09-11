FROM ubuntu:20.04

RUN apt update && apt upgrade -y
RUN apt install -y git curl
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash
RUN apt install -y nodejs
RUN git clone https://github.com/docker-hy/material-applications.git

WORKDIR  /material-applications/example-frontend

EXPOSE 5000

ENV API_URL=http://localhost:8080

RUN npm install

CMD ["npm", "start"]
