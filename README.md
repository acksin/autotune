![Acksin](https://www.acksin.com/imgs/logos/spider-788ea680.png)

# Acksin

<a href="https://travis-ci.org/acksin/acksin"><img src="https://travis-ci.org/acksin/acksin.svg?branch=master" /></a>
<a href="https://godoc.org/github.com/acksin/acksin"><img src="https://godoc.org/github.com/acksin/acksin?status.svg" alt="GoDoc"></a>

IRC: [#acksin on Freenode](https://www.acksin.com/irc)

## Introduction

Acksin is a Cloud and Container aware diagnostics and tuning
tool. It uses Machine Learning to find optimizations in your
infrastructure. The goal is to make your servers more performant,
reduce the amount you spend on servers, and help reduce the
environmental footprint.

## [Quick Start and Download](https://www.acksin.com/)

Acksin outputs its data in JSON to the command line. Run the
following command:

    sudo acksin output

Acksin primarily runs as a daemon which regularily pushes diagnostics
to a central server. Acksin runs a service called
[Acksin Console](https://www.acksin.com/console/login?redirectTo=https://www.acksin.com/console/)
providing this capability. You can get the configuration on the Acksin
Console or you can check out
[config.json.template](config.json.template) for agent
configuration. We will open source the server side in the near future.

Run the following:

    sudo acksin agent config.json

## Getting Started & Documentation

All documentation is on the [Acksin website](https://www.acksin.com/).

## Developing Acksin

Acksin's command line portion is primarily written in Go whereas the
Machine Learning is written in Python. The code is split into a
couple different sections:

 - [Command Line Tool](stats): Collects stats from the System and
   Containers.
 - [Mental Models](ai/mental_models): Take System stats and creates
   models for AI. Currently this is a program that runs on AWS Lambda.
 - [Tensorflow AI](ai/tensorflow): We use the output generated from
   the Mental Models to create train AI for the various tasks.
 - [Console](console/js): ReactJS Frontend App used on Acksin Cloud.
 - Server: This component is not yet open sourced. This is will be a
   Go server which will be built into the command line.

### Primary Dependencies

The primary dependency of Acksin is the
[ProcFS Library](https://github.com/acksin/procfs) we use.  Any code
that needs to read from ProcFS should go there. Most of the Command
Line App is a wrapper for that library. In the future we will have
similar dependencies for SysFS. In addition to that we use the Go
libraries provided by the Cloud providers.

### Deploying Acksin

Acksin has several components that need to be deployed to make a
complete system. This includes the Command Line Tool, Mental Models,
AI, Console, and Server.

#### Command Line Tool

To build the command line tool run the following:

```
make deps
make build
```

#### Mental Models

Currently to run the Mental Models you need to install the
[Serverless Framework](https://www.serverless.com) as they run on AWS
Lambda. We will split this out so it doesn't rely on Lambda in the
near future.

Make sure to create a `ai/mental_models/serverless.env.yaml` file.

Example:
```
vars: null
stages:
    dev:
        vars: null
        regions:
            us-west-2:
    prod:
        vars: null
        regions:
            us-west-2:
```

To deploy this function run.

```
cd ai
make deps
make dev
```


### [Contributing](CONTRIBUTING.md)

We love contributors to the project. Please check out the
[CONTRIBUTING.md](CONTRIBUTING.md) file.

## Goals

Acksin is based around the work of
[John Boyd](https://en.wikipedia.org/wiki/John_Boyd_(military_strategist))
with his Observe, Orient, Decide and Act paradigm, also called
the OODA loop.

UNIX has traditionally been very much about composition of tools which
works exceedingly well when you have a single machine with multiple
services. However, we are now in the era of Linux as applicance. Linux
is now just a single layer with one or two apps being the main users
of the operating system. Furthermore, as we go up the stack with
Containers and maintain clusters instead of individual machines we
need to know how one service affects the others. We need to understand
the entire system.

![OODA](https://assets.acksin.com/images/autotune_ooda.png)

### Situational awareness

Acksin's goal is to be situationally aware about the Containers, the
System, the Cluster and the Cloud so that it can help you make
effective decisions. By keeping track of this various information
about the cluster we can help point you to potential issues. Acksin
is not trying to replace application level instrumentation and
monitoring services such as Graphite and Datadog. Acksin is being
built to augment those services.

### [Mental Models](https://github.com/acksin/acksin/wiki/Mental-Models)

Mental Models are how a system and a cluster should behave such that
there is minimal operational issues. Mental Models are kernel changes
as well as various feature columns that are used to train the Machine
Learning Algorithms.

This data is contained in the [ai/mental_models](ai/mental_models) directory.

## License

Copyright (C) 2016 Acksin <hey@acksin.com>

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at <http://mozilla.org/MPL/2.0/>.
