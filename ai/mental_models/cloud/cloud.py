# Copyright (C) 2016 Acksin <hey@acksin.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import json

from aws import CloudAWS

class Cloud(object):
    def __init__(self, config_file, id, timestamp, aws_access_key, aws_secret_key):
        self.config = json.load(open(config_file, 'r'))

        aws_cloud = CloudAWS(self.config, id, timestamp, aws_access_key, aws_secret_key)
        aws_cloud.get_instances()

    def network_usage(self):
        pass

    def cpu_utilization(self):
        pass

    def memory_utilization(self):
        pass
