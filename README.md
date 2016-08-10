# STRUM

<a href="https://travis-ci.org/acksin/strum"><img src="https://travis-ci.org/acksin/strum.svg?branch=master" /></a>
<a href="https://godoc.org/github.com/acksin/strum"><img src="https://godoc.org/github.com/acksin/strum?status.svg" alt="GoDoc"></a>

## Introduction

STRUM is a Cloud and Container aware diagnostics that uses Machine
Learning to help figure out issues with your infrastructure.

## Quick Start

STRUM outputs its data in JSON to the command line. Run the following
command:

    sudo strum output

STRUM primarily runs as a daemon which regularily pushes diagnostics
to a central server. Acksin runs
[STRUM Cloud](https://www.acksin.com/console/login?redirectTo=https://www.acksin.com/console/strum)
providing this capability.  Check out
[config.json.template](config.json.template) for agent configuration.

$un the following:

    sudo strum agent config.json

## Getting Started & Documentation

All documentation is on the [STRUM website](https://www.acksin.com/strum).

## Developing STRUM

STRUM's command line portion is primarily written in Go whereas the
Machine Learning is written in Python. We will go over how to code for
each part.

### Primary Dependencies

One of the primary dependencies of STRUM is the [ProcFS Library](https://github.com/acksin/procfs) we use.
Any code that needs to read from ProcFS should go there and we will
primarily code there for things. In the future we will have similar
dependencies for SysFS. In addition to that we use the Go libraries
provided by the Cloud providers.

## Goals

STRUM is based around the work of
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

![OODA](https://assets.acksin.com/images/strum_ooda.png)

### Situational awareness

STRUM's goal is to be situationally aware about the Containers, the
System, the Cluster and the Cloud so that it can help you make
effective decisions. By keeping track of this various information
about the cluster we can help point you to potential issues. STRUM is
not trying to replace application level instrumentation such as
Graphite and Datadog. Our tools are at the system level.

### [Mental Models](https://github.com/acksin/strum/wiki/Mental-Models)

Mental Models are how a system and a cluster should behave such that
there is minimal operational issues. Mental Models are kernel changes
as well as various feature columns that are used to train the Machine
Learning Algorithms.

This data is contained in the [ai/mental_models](https://github.com/acksin/strum/tree/master/ai/mental_models) directory.

## License

Copyright (C) 2016 Acksin <hey@acksin.com>

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at <http://mozilla.org/MPL/2.0/>.
