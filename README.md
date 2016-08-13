![Autotune](https://assets.acksin.com/images/autotune.png)

# Autotune

<a href="https://travis-ci.org/acksin/autotune"><img src="https://travis-ci.org/acksin/autotune.svg?branch=master" /></a>
<a href="https://godoc.org/github.com/acksin/autotune"><img src="https://godoc.org/github.com/acksin/autotune?status.svg" alt="GoDoc"></a>

## Introduction

Autotune is a Cloud and Container aware diagnostics that uses Machine
Learning to help figure out issues with your infrastructure.

## Quick Start

[Download Autotune](https://www.acksin.com/autotune)

Autotune outputs its data in JSON to the command line. Run the following
command:

    sudo autotune output

Autotune primarily runs as a daemon which regularily pushes
diagnostics to a central server. Acksin runs
[Autotune Cloud](https://www.acksin.com/console/login?redirectTo=https://www.acksin.com/console/autotune)
providing this capability. You can get the configuration on the Acksin
Console or you can check out
[config.json.template](config.json.template) for agent
configuration. We will open source the server side in the future.

Run the following:

    sudo autotune agent config.json

## Getting Started & Documentation

All documentation is on the [Autotune website](https://www.acksin.com/autotune).

## Developing Autotune

Autotune's command line portion is primarily written in Go whereas the
Machine Learning is written in Python. We will go over how to code for
each part.

The code is split into a couple different sections:

 - [CLI Tool](stats): Collects stats from the System and Containers.
 - [Mental Models](ai/mental_models): Take System stats and creates models for AI. AWS Lambda code.
 - [Tensorflow AI](ai/tensorflow): Uses Mental Models to generate train AI for various tasks.
 - [Console](console/js): ReactJS Frontend App used on STRUM Cloud
 - Server: This component is not yet open sourced.

### Primary Dependencies

One of the primary dependencies of Autotune is the [ProcFS Library](https://github.com/acksin/procfs) we use.
Any code that needs to read from ProcFS should go there and we will
primarily code there for things. In the future we will have similar
dependencies for SysFS. In addition to that we use the Go libraries
provided by the Cloud providers.

## Goals

Autotune is based around the work of
[John Boyd](https://en.wikipedia.org/wiki/John_Boyd_(military_strategist))
with his Observe Orient Decide and Act paradigm, also called
the OODA loop.

UNIX has traditionally been very much about composition of tools which
works exceedingly well when you have a single machine with multiple
services. However, we are now in the era of Linux as applicance. Linux
is now just a single layer with one or two apps being the main users
of the operating system. Furthermore, as we go up the stack with
Containers and maintain clusters instead of individual machines we
need to know how one service affects the others.

![OODA](https://assets.acksin.com/images/autotune_ooda.png)

### Situational awareness

Autotune's goal is to be situationally aware about the Containers, the
System, the Cluster and the Cloud so that it can help you make
effective decisions. By keeping track of this various information
about the cluster we can help point you to potential issues. Autotune is
not trying to replace application level inautotuneentation such as
Graphite and Datadog. Our tools are at the system level.

### [Mental Models](https://github.com/acksin/autotune/wiki/Mental-Models)

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
