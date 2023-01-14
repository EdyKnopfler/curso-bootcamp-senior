#!/bin/bash
docker run -d --rm \
    --name frontend \
    -p 443:443 \
    --link backend-python:backend-python \
    frontend:1.0.0

