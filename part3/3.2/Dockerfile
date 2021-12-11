FROM ubuntu:latest

RUN apt update && apt -y install git python3 docker

COPY ./script.py .

CMD [ "python3","script.py" ]
