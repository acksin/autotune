/* Acksin Autotune - Linux Diagnostics
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

package cloud

// Cloud contains the metadata provided by the cloud providers.
type Cloud struct {
	// AWS provides information about AWS EC2 metadata.
	// http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html
	AWS *AWSStats
	// DigitalOcean shows all the information related to
	// DigitalOcean via its metadata interface.
	// https://developers.digitalocean.com/documentation/metadata/
	DigitalOcean *DigitalOceanStats
}

// New creates a new Cloud object and fills in any metadata from the
// cloud providers.
func New() (c *Cloud) {
	c = &Cloud{
		AWS:          NewAWS(),
		DigitalOcean: NewDigitalOcean(),
	}

	return c
}
