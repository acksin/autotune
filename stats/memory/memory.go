/* Acksin STRUM - Linux Diagnostics
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

// Package memory provides sanatized information about for Linux Memory
// - http://superuser.com/questions/521551/cat-proc-meminfo-what-do-all-those-numbers-mean
// - https://www.centos.org/docs/5/html/5.1/Deployment_Guide/s2-proc-meminfo.html
package memory

import (
	"github.com/acksin/procfs"
)

// Memory returns the memory usage of the system.
type Memory struct {
	// Unit is the metric used for all the numbers returned. E.g. kb, mb, gb.
	Unit string

	// Physical memory statistics of the machine.
	Physical struct {
		// Total is the total physical memory of the system.
		Total int64
		// Free is the free physical memory in the system.
		Free int64
		// Used physical memory of the system.
		Used int64
		// Cached is the physical memory that is used for cache.
		Cached int64
		// Buffers is the amount of memory used for file buffers.
		Buffers int64
		// TotalFree is Free memory + Used + Cached which is the real
		// amount of memory that Linux has available
		TotalFree int64
	}

	// Swap is information on swap usage on the system.
	Swap struct {
		// Total swap that is available.
		Total int64
		// Free swap space.
		Free int64
		// Used swap space.
		Used int64
		// Cached is space used for cache
		Cached int64
	}

	// Virtual is the virtual memory used by the machine.
	Virtual struct {
		// Total virtual memory that has been allocated.
		Total int64
		// Used virtual memory.
		Used int64
		// Chunk is the largest chunk that is being used.
		Chunk int64
	}

	// Dirty is the memory waiting to be written back to disk.
	Dirty int64
	// Writeback is the memory currently being written back to disk.
	Writeback int64
	// Mapped is memory used my mmap files.
	Mapped int64
}

func (m *Memory) physical(meminfo *procfs.Meminfo) {
	m.Physical.Total = meminfo.MemTotal
	m.Physical.Free = meminfo.MemFree
	m.Physical.Used = meminfo.MemTotal - meminfo.MemFree
	m.Physical.Cached = meminfo.Cached
	m.Physical.Buffers = meminfo.Buffers
	m.Physical.TotalFree = m.Physical.Free + m.Physical.Cached + m.Physical.Buffers
}

func (m *Memory) swap(meminfo *procfs.Meminfo) {
	m.Swap.Total = meminfo.SwapTotal
	m.Swap.Free = meminfo.SwapFree
	m.Swap.Used = meminfo.SwapTotal - meminfo.SwapFree
	m.Swap.Cached = meminfo.SwapCached
}

func (m *Memory) virtual(meminfo *procfs.Meminfo) {
	m.Virtual.Total = meminfo.VMallocTotal
	m.Virtual.Used = meminfo.VMallocUsed
	m.Virtual.Chunk = meminfo.VMallocChunk
}

func (m *Memory) other(meminfo *procfs.Meminfo) {
	m.Dirty = meminfo.Dirty
	m.Writeback = meminfo.Writeback
	m.Mapped = meminfo.Mapped
}

// New returns a Memory object representing system memory information.
func New() *Memory {
	m := &Memory{}

	meminfo, err := procfs.NewMeminfo()
	if err != nil {
		return nil
	}

	// TODO: Should specify unit type in the future.
	m.Unit = "kb"

	m.physical(&meminfo)
	m.swap(&meminfo)
	m.virtual(&meminfo)
	m.other(&meminfo)

	return m
}
