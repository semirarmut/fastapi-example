# fastapi-example

## Build an App With FastAPI for Python

* _docker build -t fastapi_image ._ 
* _docker run -dp 127.0.0.1:8080:8080 fastapi_image_
* List all containers (-a) by container ID (-q):
  *  _docker ps -aq_
* Stop docker:
  *  _docker ps -aq | xargs docker stop_
* Remove docker containers:
  *  _docker ps -aq | xargs docker stop | xargs docker rm_

*  Build with docker compose:
  * _docker compose up_