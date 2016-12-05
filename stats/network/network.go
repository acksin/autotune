/*
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

package network

import (
	"github.com/acksin/procfs"
)

// Total: 804 (kernel 0)
// TCP:   410 (estab 327, closed 75, orphaned 0, synrecv 0, timewait 71/0), ports 0

// Transport Total     IP        IPv6
// *	  0         -         -
// RAW	  0         0         0
// UDP	  15        9         6
// TCP	  335       333       2
// INET	  350       342       8
// FRAG	  0         0         0

// Network returns network information about the machine.
type Network struct {
	// Total sockets the machine is maintaining of all types.
	Total int64

	// TODO Implement RAW sockets
	RAW struct{}
	// TODO Implement UDP sockets
	UDP struct{}

	// TCP socket information.
	TCP struct {
		// Total TCP sockets
		Total int64

		Established int64
		Closed      int64
		Orphaned    int64
		Synrecv     int64
		Timewait    int64
	}
}

func (n *Network) tcp(sockstat *procfs.NetSockstat) {
	n.TCP.Established = sockstat.TCP.InUse
	n.TCP.Orphaned = sockstat.TCP.Orphan
	// TODO: Finish more of this.
}

// New returns the Network information of the machine
func New() *Network {
	n := &Network{}

	netSockstat, err := procfs.NewNetSockstat()
	if err != nil {
		return nil
	}

	n.Total = netSockstat.Sockets.Used
	n.tcp(&netSockstat)

	return n
}
