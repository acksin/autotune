/* Acksin STRUM - Linux Diagnostics
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

// Package disk shows information about block drives in the machine.
package disk

import (
	"log"

	"github.com/acksin/go-fstab"
	"github.com/acksin/strum/stats/mvp"
)

// Disk returns information about the block drives on the machine.
type Disk struct {
	BlockDevices []mvp.BlockDevice
	FStab        fstab.Mounts
}

// New returns a Disk object representing system disk information.
func New() *Disk {

	m, err := fstab.ParseSystem()
	if err != nil {
		log.Println(err)
	}

	return &Disk{
		BlockDevices: mvp.GetLsBlk(),
		FStab:        m,
	}
}
