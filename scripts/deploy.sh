#!/bin/bash

# Build the Docker image
docker build -t abstract-assistant .

# Run the Docker container
docker run -d -p 5000:5000 abstract-assistant

