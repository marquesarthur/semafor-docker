# semafor-docker
Docker container that orchestrates a frame-semantic parsing system


## Build

Build images:



`docker build -t msarthur/semafor-base .` 
`docker build -t msarthur/semafor-frameparser .`
`docker build -t msarthur/semafor-rest .`


### Publish


`docker push msarthur/semafor-base:latest`
`docker push msarthur/semafor-frameparser:latest`
`docker push msarthur/semafor-rest:latest`