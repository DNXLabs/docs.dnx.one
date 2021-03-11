---
layout: default
title: Makefiles and the 3musketeers pattern
parent: DevOps Playbook
nav_order: 3
---

# Makefiles and the 3musketeers pattern

## Principles

Makefile is used as a common descriptor for building, deploying, testing and other operations to be performed.

By looking at the Makefile, the developer should have a quick view of all possible operations that can be performed on that code base, in the form of make targets.

Examples of targets:
* build
* test
* deploy

A developer should be able to clone a repository, set the required variables in the `.env` file and successfully run `make <target>` without any special setup in their machine other than having make, docker and docker-compose installed.

The main benefit of this pattern is running operations on both developers machine and CI worker the same.

## 3musketeers

A Makefile and docker-compose.yml file should exist in the repository.

Makefile have targets that call `docker-composer run <service>`. The service being a tool or the application itself.

Example:

```make
.env:
	cp .env.template .env

assumeRole: .env
	docker-compose run --rm aws assume-role.sh >> .env
.PHONY: assumeRole

deploy: assumeRole
	docker-compose run --rm deploy ./deploy.sh
.PHONY: deploy
```

The main target above, `deploy`, will first call `assumeRole`, which in turn calls `.env`.

* `.env` target creates the file if it doesn't exist.
* `assumeRole` uses AWS CLI to assume a role and output the credentials to the `.env` file
* `deploy` runs the deploy script using the credentials

The docker-compose.yml file for the example above looks like:

```yaml
version: '3.2'

services:
  deploy:
    image: dnxsolutions/aws:1.4.0
    entrypoint: "/bin/bash -c"
    env_file:
      - .env
    volumes:
      - ./deploy:/work

  aws:
    image: dnxsolutions/aws:1.4.0
    entrypoint: "/bin/bash -c"
    env_file:
      - .env
```

In this example, the deploy script uses AWS CLI so we are using the `dnxsolutions/aws` image, same as the `assumeRole` target, which also uses the AWS CLI.

But in another case where we would deploy to kubernetes, the deploy service would use an image built for that, with kubectl, helm, etc.

## Variables

All variables used by make targets should be declared in the `.env.compose` file, without values.

Example `.env.compose`:
```
NODE_ENV
```

When `make .env` runs, if the `.env` file doesn't exist, it's created from `.env.compose`.

Now, when running in a CI tool, this value should be set in the pipeline stage and set as an environment variable when the worker is running.

And similarly, when running in a developer's local machine, the value can be set in as an environment variable, or set directly in the `.env`, such as:

```
NODE_ENV=development
```

If `make .env` is called again, it won't overwrite the file as it already exists (make has this logic), so the values set there are preserved.

The `.env` file should be in the `.gitignore` and not pushed to the repository. Examples (like a `.env.local`) are ok to push to repository as long as they don't contain credentials or sensitive information.