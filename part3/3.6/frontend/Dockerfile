FROM node:14-alpine as build

COPY /example-frontend /app

WORKDIR /app

RUN npm install && \
    npm run build

FROM alpine:latest

WORKDIR /app

EXPOSE 5000

ENV REACT_APP_BACKEND_URL=http://localhost:8080

RUN apk add nodejs npm && \
    npm install -g serve && \
    adduser -S appuser

COPY --from=build ./app/build ./build

USER appuser

CMD ["serve", "-s", "-l", "5000", "build"]

