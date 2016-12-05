# Copyright (C) 2016 Acksin <hey@acksin.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import string

def ai_feature(func):
    def wrapper(self):
        return func(self)

    return wrapper

def procfs_feature(func):
    """
    procfs_feature returns a dictionary if the current system doesn't match
    the value we want it to have.
    """

    def wrapper(self, *args, **kwargs):
        output = func(self, *args, **kwargs)

        returned = {}
        for k, v in output.items():
            kernel = self.machine.stats['System']['Kernel']
            if kernel.has_key(k) and not kernel[k] == v:
                change = {
                    'Current': kernel[k],
                    'Replacement': v,
                    'Docs': string.strip(func.__doc__),
                }
                returned = dict(returned.items() + [(k, change)])

        return returned

    return wrapper

def sysfs_feature(func):
    def wrapper(self):
        return func(self)

    return wrapper
