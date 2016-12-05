# Copyright (C) 2016 Acksin <hey@acksin.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import sys; sys.path.append("site-packages")
import os

import machine
import cloud

def handler(event, context):
    """
    Run on AWS Lambda.
    """

    config_file = "config.dev.json"
    if context is not None and context.function_name == "autotune-prod-mentalmodels":
        config_file = "config.prod.json"

    if event.has_key('Machine'):
        machine.run_model(config_file, event['ID'])
    elif event.has_key('Cloud'):
        cloud.run_model(
            config_file,
            event['ID'],
            event['Timestamp'],
            event['AWSAccessKey'],
            event['AWSSecretKey']
        )

    return {
        'Message': "OK"
    }

if __name__ == "__main__":
    if sys.argv[1] == 'Cloud':
        print handler({
            'Cloud': True,
            'ID': sys.argv[2],
            'Timestamp': sys.argv[3],
            'AWSAccessKey': os.environ['AWS_ACCESS_KEY'],
            'AWSSecretKey': os.environ['AWS_SECRET_KEY'],
        }, None)
    else:
        print handler({
            'Machine': True,
            'ID': sys.argv[1]
        }, None)
