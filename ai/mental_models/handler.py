# Copyright (C) 2016 Acksin <hey@acksin.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import json
import psycopg2
import sys

from memory import Memory
from networking import Networking

class Autotune(object):
    def __init__(self, config_file, id):
        self.ID = id

        self.config = json.load(open(config_file, 'r'))
        self.conn = psycopg2.connect(self.config['database'])

        cur = self.conn.cursor()
        cur.execute("SELECT data FROM autotune_stats where id = %s", (id,))
        self.stats = cur.fetchone()[0]
        cur.close()

    def write_ai_features(self, features):
        cur = self.conn.cursor()
        cur.execute("UPDATE autotune_stats SET ai_features = %s WHERE id = %s", (json.dumps(features), self.ID))
        cur.close()
        self.conn.commit()

    def write_procfs_features(self, features):
        cur = self.conn.cursor()
        cur.execute("UPDATE autotune_stats SET procfs_features = %s WHERE id = %s", (json.dumps(features), self.ID))
        cur.close()
        self.conn.commit()

    def write_sysfs_features(self, features):
        cur = self.conn.cursor()
        cur.execute("UPDATE autotune_stats SET sysfs_features = %s WHERE id = %s", (json.dumps(features), self.ID))
        cur.close()
        self.conn.commit()

    def close(self):
        self.conn.close()

def handler(event, context):
    """
    Run on AWS Lambda.
    """

    config_file = "config.dev.json"
    if context.function_name == "autotune-prod-mentalmodels":
        config_file = "config.prod.json"

    autotune = Autotune(config_file, event['ID'])

    memory = Memory(autotune)
    networking = Networking(autotune)

    ai_features = dict(memory.ai_features().items() + networking.ai_features().items())
    procfs_features = dict(memory.procfs_features().items() + networking.procfs_features().items())
    sysfs_features = dict(memory.sysfs_features().items() + networking.sysfs_features().items())

    autotune.write_ai_features(ai_features)
    autotune.write_procfs_features(procfs_features)
    autotune.write_sysfs_features(sysfs_features)

    autotune.close()

    return {
        'Message': "OK"
    }

if __name__ == "__main__":
    print handler({
        'ID': sys.argv[1]
    }, None)
