# Changes made to the two Dockerfiles and Docker Compose File in order to make all the Buttons work

- Removed the Exposed Ports and ENV variables from the Frontend and Backend Dockerfiles
- Moved the ENV variables to the Docker Compose file, the ports have been already mapped in the previous exercises
- Removed the ports for the URL environments as we are using Nginx
