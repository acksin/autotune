# Copyright (C) 2016 Acksin <hey@acksin.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from types import FunctionType

class MentalModel(object):
    """
    MentalModel provides utilities to handle feature extraction.
    """

    def ai_features(self):
        return dict([(k, f(self),)
                    for k, f in self.__class__.__dict__.iteritems()
                    if callable(f) and k.startswith('is_')])

    def procfs_features(self):
        procfs = []
        for k, f in self.__class__.__dict__.iteritems():
            if callable(f) and k.startswith('procfs_'):
                procfs += f(self).items()

        return dict(procfs)

    def sysfs_features(self):
        sysfs = []
        for k, f in self.__class__.__dict__.iteritems():
            if callable(f) and k.startswith('sysfs_'):
                sysfs += f(self).items()

        return dict(sysfs)
