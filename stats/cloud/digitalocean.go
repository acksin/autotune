/* Acksin STRUM - Linux Diagnostics
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

package cloud

import (
	"github.com/digitalocean/go-metadata"
)

// DigitalOceanStats returns information about DigitalOcean droplet
// metadata.
type DigitalOceanStats struct {
	*metadata.Metadata
}

// NewDigitalOcean returns a DigitalOceanStats object otherwise it
// returns nil.
func NewDigitalOcean() *DigitalOceanStats {
	client := metadata.NewClient()

	all, err := client.Metadata()
	if err != nil {
		return nil
	}

	return &DigitalOceanStats{all}
}
