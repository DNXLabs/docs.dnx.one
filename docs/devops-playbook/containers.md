---
layout: default
title: Containers
parent: DevOps Playbook
nav_order: 2
---

# Containers

## Principles

Containers are used to keep consistency between environments (including local) and reuse tools during deplyoments.

A container should always carry the bare minimum to perform its purpose.

Always start with an Alpine container, or choose one that is based on Alpine.

## Scope

A good container image for performing AWS operations contains only AWS CLI, its requirements and maybe a bash script that calls it.

Another example, to build and deploy a serverless application, you will need (at least):
* A container image with serverless CLI
* Another container image to build that serverless function

We will see how the process works together later on this document.

## Repository Structure

A container image should have its own repository.

Set the repository as public, unless there's a reason not to.

Use DockerHub to build and host the image. DockerHub connects to GitHub and automatically builds images from Dockerfiles in repositores.

The repository should have a `Dockerfile` in the root.

Naming scheme:
* Repository: `docker-<image name>`
* DockerHub: `<image name>`

## Local vs Deployed

> The process described here is alpha (untested), any improvement is welcomed.

When developing locally with a docker container, the image used should be the same as deployed.

Sometimes it's not possible when running locally it requires tools for debugging or auto-refreshing that are not required when deployed to an environment.

In this case, use multi-stage builds so the same Dockerfile have stages for building, running locally and deployed.

* https://dev.to/brpaz/using-docker-multi-stage-builds-during-development-35bc