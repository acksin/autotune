# Copyright (C) 2016 Acksin <hey@acksin.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from machine import Machine

from memory import Memory
from networking import Networking

def run_model(config_file, machine_id):
    print "Running {}".format(machine_id)

    machine = Machine(config_file)
    machine.get_id(machine_id)

    memory = Memory(machine)
    networking = Networking(machine)

    ai_features = dict(memory.ai_features().items() + networking.ai_features().items())
    procfs_features = dict(memory.procfs_features().items() + networking.procfs_features().items())
    sysfs_features = dict(memory.sysfs_features().items() + networking.sysfs_features().items())

    machine.write_features('ai_features', ai_features)
    machine.write_features('procfs', procfs_features)
    machine.write_features('sysfs', sysfs_features)

    machine.write_features('quick', {
        'Security': 0,
        'Stats': len(procfs_features) + len(sysfs_features),
    })
