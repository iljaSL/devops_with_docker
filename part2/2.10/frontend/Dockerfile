FROM node:14

COPY /example-frontend /app

WORKDIR /app

RUN npm install

RUN npm run build

RUN npm install -g serve

CMD ["serve", "-s", "-l", "5000", "build"]

