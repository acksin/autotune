/* Acksin STRUM - Linux Diagnostics
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

package stats

import (
	"github.com/acksin/strum/stats/io"
	"github.com/acksin/strum/stats/memory"
)

// Process is information about a Linux process
type Process struct {
	// Exe is the executable that is running.
	Exe string
	// PID of the process
	PID int
	// Memory stats of the process
	Memory *memory.ProcessMemory
	// IO contains information about the IO of the machine.
	IO *io.ProcessIO
}
