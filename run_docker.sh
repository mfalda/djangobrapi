#!/bin/bash
sudo docker run --rm --net host -e DATABASE_URL=none --name brapi brapi
