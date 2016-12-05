/*
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

package stats

import (
	"encoding/json"

	"github.com/acksin/procfs"

	"github.com/acksin/acksin/stats/cloud"
	"github.com/acksin/acksin/stats/container"
	"github.com/acksin/acksin/stats/disk"
	"github.com/acksin/acksin/stats/io"
	"github.com/acksin/acksin/stats/kernel"
	"github.com/acksin/acksin/stats/memory"
	"github.com/acksin/acksin/stats/network"
)

// Stats contains both the system and process statistics.
type Stats struct {
	// System specific information
	System System
	// Container specific information
	Container *container.Container
	// Cloud specific information
	Cloud *cloud.Cloud
	// Processes are the process information of the system
	Processes []Process
}

func (n *Stats) processes() procfs.Procs {
	fs, err := procfs.NewFS(procfs.DefaultMountPoint)
	if err != nil {
		return nil
	}

	procs, err := fs.AllProcs()
	if err != nil {
		return nil
	}

	return procs
}

func (n *Stats) containsPid(pids []int, proc procfs.Proc) bool {
	for _, pid := range pids {
		if proc.PID == pid {
			return true
		}
	}

	return false
}

// UnmarshalJSON converts a byte blob into the Stats object
// representation.
func (n *Stats) UnmarshalJSON(d []byte) error {
	return json.Unmarshal(d, n)
}

// New returns stats of the machine with pids filtering for
// processes. If pids are empty then it returns all process stats.
func New(pids []int) (s *Stats) {
	s = &Stats{}

	s.System.Memory = memory.New()
	s.System.Disk = disk.New()
	s.System.Network = network.New()
	s.System.Kernel = kernel.New()

	s.Container = container.New()
	s.Cloud = cloud.New()

	for _, proc := range s.processes() {
		exe, err := proc.Executable()
		if err != nil || exe == "" {
			status, _ := proc.NewStatus()
			exe = status.Name
		}

		p := Process{
			Exe:    exe,
			PID:    proc.PID,
			Memory: memory.NewProcess(proc),
			IO:     io.NewProcess(proc),
		}

		if len(pids) == 0 || s.containsPid(pids, proc) {
			s.Processes = append(s.Processes, p)
		}
	}

	return s
}
