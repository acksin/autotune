# Copyright (C) 2016 Acksin <hey@acksin.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import json
import os
import boto3

class CloudAWS(object):
    def __init__(self, config, id, timestamp, aws_access_key, aws_secret_key):
        self.config = config

        self.ID = id
        self.Timestamp = timestamp

        self.aws_access_key = aws_access_key
        self.aws_secret_key = aws_secret_key

        self.ec2 = boto3.client(
            'ec2',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
        )

        self.s3 = boto3.client('s3')

    def write_object(self, key, value):
        self.s3.put_object(
            Bucket=self.config['s3_bucket'],
            Key=os.path.join(self.ID, 'ec2', key),
            Body=value.encode('utf-8')
        )

    def get_instances(self):
        desc_instances = self.ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
        instances = []

        for reservation in desc_instances[u'Reservations']:
            instances += reservation['Instances']

        for i in instances:
            print i['InstanceId']
            CloudAWSEC2Instance(self, i)

class CloudAWSEC2Instance(object):
    def __init__(self, aws, instance):
        aws.write_object(
            "{}/{}/stats.json".format(instance['InstanceId']),
            json.dumps(instance, cls=AcksinEncoder)
        )

        CloudAWSMetrics(aws, instance)
        CloudAWSSecurity(aws, instance)

class CloudAWSMetrics(object):
    def __init__(self, aws, instance):
        self.aws = aws
        self.instance = instance

        client = boto3.client('cloudwatch')



class CloudAWSSecurity(object):
    def __init__(self, aws, instance):
        self.aws = aws
        self.instance = instance

        self.security = []

        self.is_open_to_the_web()

    def is_open_to_the_web(self):
        print self.instance['PublicDnsName']


from datetime import datetime
import decimal


class AcksinEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        elif isinstance(o, datetime):
            serial = o.isoformat()
            return serial

        raise TypeError ("Type not serializable")
