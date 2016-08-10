/* Acksin STRUM - Linux Diagnostics
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

// Package mvp contains a bunch of code which is a minimum viable
// product. We either call out to other
package mvp

import (
	"encoding/json"
	"log"
	"os/exec"
)

// BlockDevice returns the blockdevice information about the
type BlockDevice struct {
	Name       string        `json:"name"`
	MajMin     string        `json:"maj:min"`
	RM         string        `json:"rm"`
	Size       string        `json:"size"`
	RO         string        `json:"ro"`
	Type       string        `json:"type"`
	MountPoint string        `json:"mountpoint"`
	Children   []BlockDevice `json:"children,omitempty"`
}

// GetLsBlk gets the output of lsblk and returns that as an object.
func GetLsBlk() []BlockDevice {
	out, err := exec.Command("lsblk", "-J", "-a").Output()
	if err != nil {
		log.Println(err)
	}

	var lsblk struct {
		BlockDevices []BlockDevice `json:"blockdevices"`
	}

	json.Unmarshal(out, &lsblk)

	return lsblk.BlockDevices
}
