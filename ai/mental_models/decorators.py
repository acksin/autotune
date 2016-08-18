# Copyright (C) 2016 Acksin <hey@acksin.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

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
            if self.autotune.stats['System']['Kernel'].has_key(k) and \
               not self.autotune.stats['System']['Kernel'][k] == v:
                returned = dict(returned.items() + output.items())

        return returned

    return wrapper

def sysfs_feature(func):
    def wrapper(self):
        return func(self)

    return wrapper
