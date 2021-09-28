Dockerhub link: https://hub.docker.com/r/plustig/robo-friends

How to run the robo-friends image:

- Pull the image with `docker pull plustig/robo-friends`

- Run the container with `docker run -it -p 3000:3000 plustig/robo-friends` <br>
  **Note: The `-it` flag is required, because it's an react app and react is relying on a interactive terminal to start the application.**
  
- Visit the app through a browser `http://localhost:3000`
