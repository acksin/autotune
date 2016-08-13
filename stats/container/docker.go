/* Acksin Autotune - Linux Diagnostics
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

package container

import (
	"github.com/docker/engine-api/client"
	"github.com/docker/engine-api/types"
	"golang.org/x/net/context"
)

// Docker contains information about the current Docker service on the
// machine.
type Docker struct {
	// Containers are all the active and inactive containers that
	// are on the system.
	Containers []types.Container
	// Images are all the images that exist on the Docker Images
	// that exist on the machine.
	Images []types.Image
}

// NewDocker creates a new Docker object.
func NewDocker() (c *Docker) {
	c = &Docker{}

	defaultHeaders := map[string]string{
		"User-Agent": "engine-api-cli-1.0",
	}
	cli, err := client.NewClient("unix:///var/run/docker.sock", "v1.22", nil, defaultHeaders)
	if err != nil {
		return nil
	}

	options := types.ContainerListOptions{All: true}
	c.Containers, err = cli.ContainerList(context.Background(), options)
	if err != nil {
		return nil
	}

	imgOptions := types.ImageListOptions{All: true}
	c.Images, err = cli.ImageList(context.Background(), imgOptions)
	if err != nil {
		return nil
	}

	return c
}
