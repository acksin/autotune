/* Acksin STRUM - Linux Diagnostics
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

package memory

import (
	"strconv"

	"github.com/acksin/procfs"
)

// ProcessMemory returns memory usage of a Process
type ProcessMemory struct {
	// Swap usage of the Process
	Swap struct {
		// Size of the swap used
		Size int64
		// Unit metric used
		Unit string
	}
}

func (m *ProcessMemory) swap(proc *procfs.Proc) {
	ps, _ := proc.NewStatus()

	v, err := strconv.ParseInt(ps.VMSwap, 10, 64)
	if err != nil {
		return
	}

	m.Swap.Size = v
	m.Swap.Unit = "kb"
}

// NewProcess returns memory information of a Linux Process
func NewProcess(proc procfs.Proc) *ProcessMemory {
	pm := &ProcessMemory{}
	pm.swap(&proc)

	return pm
}
