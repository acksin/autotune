/*
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

package io

// IO contains the aggregrate IO information for the entire system.
type IO struct {
}

// New returns a new IO.
func New() *IO {
	return &IO{}
}
