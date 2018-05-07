# BIGSEA Asperathos - Broker

## Overview
The Broker component is the framework entry point for the user. It is responsible for receiving a submission from the user and preparing its execution.

To more details about Broker, see [architecture.md](https://github.com/bigsea-ufcg/bigsea-manager/tree/refactor/docs/architecture.md)

## How does it works?
The broker is implemented following a **plugin architecture**, providing flexibility to add or remove plugins when necessary.
All the integrations with different infrastructures and components are made by specific plugins.

## How to develop a plugin?
See [plugin-development.md](https://github.com/bigsea-ufcg/bigsea-manager/tree/refactor/docs/plugin-development.md).

## Requirements
* Python 2.7 or Python 3.5
* Linux packages: python-dev and python-pip
* Python packages: setuptools, tox and flake8

To **apt** distros, you can use [pre-install.sh](https://github.com/bigsea-ufcg/bigsea-manager/tree/refactor/tools/pre-install.sh) to install the requirements.

## Install
First of all, install **git**. After, you just need to clone the [Broker repository](https://github.com/bigsea-ufcg/bigsea-manager.git) in your machine.

### Configuration
A configuration file is required to run the Broker. **Edit and fill your broker.cfg in the root of Broker directory.** Make sure you have fill up all fields before run.
You can find a template in [config-example.md](https://github.com/bigsea-ufcg/bigsea-manager/tree/refactor/docs/config-example.md). 

### Run
In the Broker root directory, start the service using tox command:
```
$ tox -e venv -- broker
```

## Broker REST API
Endpoints is avaliable on [restapi-endpoints.md](https://github.com/bigsea-ufcg/bigsea-manager/tree/refactor/docs/restapi-endpoints.md) documentation.

## Avaliable plugins
* [Spark Sahara](https://github.com/bigsea-ufcg/bigsea-manager/tree/refactor/docs/plugins/spark_sahara.md)
* [Spark Mesos](https://github.com/bigsea-ufcg/bigsea-manager/tree/refactor/docs/plugins/spark_mesos.md)
* [Spark Generic](https://github.com/bigsea-ufcg/bigsea-manager/tree/refactor/docs/plugins/spark_mesos.md)
* [Openstack Generic](https://github.com/bigsea-ufcg/bigsea-manager/tree/refactor/docs/plugins/openstack_generic.md)
* [Chronos](https://github.com/bigsea-ufcg/bigsea-manager/tree/refactor/docs/plugins/chronos.md)
