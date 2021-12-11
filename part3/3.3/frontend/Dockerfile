FROM node:14

EXPOSE 5000

COPY /example-frontend /app

WORKDIR /app

ENV REACT_APP_BACKEND_URL=http://localhost:8080

RUN useradd -m appuser
RUN npm install
RUN npm run build
RUN npm install -g serve

USER appuser

CMD ["serve", "-s", "-l", "5000", "build"]

