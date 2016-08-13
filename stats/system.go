/* Acksin Autotune - Linux Diagnostics
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

package stats

import (
	"github.com/acksin/autotune/stats/disk"
	"github.com/acksin/autotune/stats/memory"
	"github.com/acksin/autotune/stats/network"
)

// System contains information about the system
type System struct {
	// Memory stats of the system
	Memory *memory.Memory
	// Network stats of the system
	Network *network.Network
	// Disk stats of the system
	Disk *disk.Disk
	// Kernel represents the kernel parameters of the current
	// system. On Linux this is the output of `sysctl -a`
	Kernel map[string]string
}
