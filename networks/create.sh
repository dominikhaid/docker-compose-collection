#!/usr/bin/env bash

docker network create --driver --subnet=172.29.0.0/16 bridge tools
docker network create --driver --subnet=172.29.1.0/16 bridge db
docker network create --driver --subnet=172.29.2.0/16 bridge web
docker network create --driver --subnet=172.29.3.0/16 bridge system
docker network create --driver --subnet=172.29.4.0/16 bridge monitor
