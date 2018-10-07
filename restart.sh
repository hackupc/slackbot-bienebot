#!/usr/bin/env bash
DOCKER_ID="$(docker inspect --format="{{.Id}}" hackupc-bienebot)"
docker cp ${DOCKER_ID}:/srv/bienebot/logs/ .
docker-compose down
docker-compose up -d --build
docker image prune -f