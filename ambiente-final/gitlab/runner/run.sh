#!/bin/bash
export GITLAB_HOME=/home/ederson/Documentos/Aprendendo/senior-cleuton-udemy/ambiente-final/gitlab
sudo sudo docker run --rm --name gitlab-runner \
    --network gitlab-ci \
    -v /home/ederson/Documentos/Aprendendo/senior-cleuton-udemy/ambiente-final/gitlab/runner/data:/etc/gitlab-runner \
    -v /var/run/docker.sock:/var/run/docker.sock \
    gitlab/gitlab-runner:latest

