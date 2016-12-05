/*
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

package container

// Container information from various container services.
type Container struct {
	// Docker provides information about Containers and Images on
	// the machine.
	Docker *Docker
}

// New creates a new Container object filling in information about
// various containers we support.
func New() (c *Container) {
	c = &Container{
		Docker: NewDocker(),
	}

	return c
}
