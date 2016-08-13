/* Acksin Autotune - Linux Diagnostics
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

package main

import (
	"fmt"

	"github.com/acksin/autotune/stats"
)

type output struct {
}

func (a output) Synopsis() string {
	return "Output Diagnostics."
}

func (a output) Help() string {
	return "Output Diagnostics."
}

func (a output) Run(args []string) int {
	var (
		s = stats.New([]int{})
	)

	if len(args) != 0 {
		switch args[0] {
		case "flat":
			fmt.Printf("%s", s.Flat())
		}

	} else {
		fmt.Printf("%s", s.JSON())
	}

	return 0
}
