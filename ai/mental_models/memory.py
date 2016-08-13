# Copyright (C) 2016 Acksin <hey@acksin.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from decorators import *
import mental_model

class Memory(mental_model.MentalModel):
    def __init__(self, autotune):
        self.autotune = autotune
        self.memory = self.autotune.stats['System']['Memory']
        self.kernel = self.autotune.stats['System']['Kernel']

    @ai_feature
    def is_swapping(self):
        """
        If The machine is swapping memory consider moving to a larger machine with more memory.
        """

        return self.memory['Physical']['Free'] == 0 and self.memory['Swap']['Used'] > 0

    @ai_feature
    def is_under_utilized(self):
        """
        Linux uses some of the free memory for storing file buffers in
        memory. Let's see how much it caches and recommend an instance
        size.

        http://askubuntu.com/questions/198549/what-is-cached-in-the-top-command

        """
        if self.memory['Physical']['Free'] > 0:
            percent_used = self.memory['Physical']['Free'] / self.memory['Physical']['Total']
            return percent_used < 0.5

        return False

    @procfs_feature
    def procfs_vm_swappiness(self):
        """
        Disable swapping and clear the file system page cache to free memory first.
        """

        return {
            "/proc/sys/vm/swappiness": "0"
        }

    @procfs_feature
    def procfs_vm_min_free_kbytes(self):
        """
        Amount of memory to keep free. Don't want to make this too high as
        Linux will spend more time trying to reclaim memory.
        """

        return {
            "/proc/sys/vm/min_free_kbytes": "65536"
        }

    @sysfs_feature
    def sysfs_mm_transparent_hugepages(self):
        """
        Explit huge page usage making the page size of 2 or 4 MB
        instead of 4kb. Should reduce CPU overhead and improve MMU
        page translation.
        """

        return {
            "/sys/kernel/mm/transparent_hugepage/enabled": "always"
        }
