#!/bin/bash
export GITLAB_HOME=/home/ederson/Documentos/Aprendendo/senior-cleuton-udemy/ambiente-final/gitlab
sudo docker run --rm \
    --hostname gitlab \
    --publish 9843:443 --publish 9880:9880 --publish 422:22 \
    --name gitlab \
    --network gitlab-ci \
    --volume $GITLAB_HOME/config:/etc/gitlab \
    --volume $GITLAB_HOME/logs:/var/log/gitlab \
    --volume $GITLAB_HOME/data:/var/opt/gitlab \
    gitlab/gitlab-ee:latest

