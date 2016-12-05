/*
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

package io

import (
	"github.com/acksin/procfs"
)

// ProcessIO is kernel level IO information about the process. This
// can be used to debug various issues related to open files and
// kernel limits on the process IO.
type ProcessIO struct {
	// Limits are the max limits either in time or size for the
	// following resources on the process.x.
	Limits struct {
		// OpenFiles is the maximum number of files that this
		// process can open at a time.
		OpenFiles int
		// FileSize is the maximum file size that the process
		// can make.
		FileSize int
		// CPUTime is the amount of time that the CPU has to
		// run.
		CPUTime int
	}

	// FD is the file descriptors that the process currently has
	// open.
	FD ProcessFD
}

func (p *ProcessIO) limits(proc *procfs.Proc) {
	limits, err := proc.NewLimits()
	if err != nil {
		return
	}

	p.Limits.CPUTime = limits.CPUTime
	p.Limits.FileSize = limits.FileSize
	p.Limits.OpenFiles = limits.OpenFiles
}

func (p *ProcessIO) fileDescriptors(proc *procfs.Proc) {
	fd, err := proc.NewFD()
	if err != nil {
		return
	}
	p.FD = ProcessFD(fd)
}

// NewProcess returns the file descriptors for a single Linux process.
func NewProcess(proc procfs.Proc) *ProcessIO {
	p := &ProcessIO{}
	p.fileDescriptors(&proc)
	p.limits(&proc)

	return p
}
