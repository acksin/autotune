# Copyright (C) 2016 Acksin <hey@acksin.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from cloud import Cloud

def run_model(config_file, id, timestamp, aws_access_key, aws_secret_key):
     Cloud(config_file, id, timestamp, aws_access_key, aws_secret_key)
