#!/bin/bash

DOCKERFILE="Dockerfile"
ARCH="amd64"

# Check if docker is installed
if ! [ -x "$(command -v docker)" ]; then
  echo 'Error: docker is not installed.' >&2
  exit 1
fi

# Check if we're on ARM or x86
if [ "$(uname -m)" = "arm64" ]; then
  ARCH="arm64"
  DOCKERFILE="${DOCKERFILE}.${ARCH}"
fi

TAG="baler-${ARCH}:latest"

# Build the docker image
docker build -t ${TAG} -f "${DOCKERFILE}" .