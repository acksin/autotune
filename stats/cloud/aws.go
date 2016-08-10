/* Acksin STRUM - Linux Diagnostics
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

package cloud

import (
	"reflect"

	"github.com/aws/aws-sdk-go/aws/ec2metadata"
	"github.com/aws/aws-sdk-go/aws/session"
)

// AWSStats returns the relevant AWS information about the current
// instance via the machine's EC2 Metadata IP interface.
type AWSStats struct {
	AmiID           string `metadata:"ami-id" `
	AmiLaunchIndex  string `metadata:"ami-launch-index"`
	AmiManifestPath string `metadata:"ami-manifest-path"`
	Hostname        string `metadata:"hostname"`
	InstanceAction  string `metadata:"instance-action"`
	InstanceID      string `metadata:"instance-id"`
	InstanceType    string `metadata:"instance-type"`
	LocalHostname   string `metadata:"local-hostname"`
	LocalIpv4       string `metadata:"local-ipv4"`
	MAC             string `metadata:"mac"`
	Profile         string `metadata:"profile"`
	PublicHostname  string `metadata:"public-hostname"`
	PublicIpv4      string `metadata:"public-ipv4"`
	ReservationID   string `metadata:"reservation-id"`
	SecurityGroups  string `metadata:"security-groups"`

	Spot struct {
		Termination string
	}
	// TODO: These need to be converted into iteration tasks.
	// block-device-mapping/
	// metrics/
	// network/
	// placement/
	// public-keys/
	// services/
}

func (a *AWSStats) parseMetadata(m *ec2metadata.EC2Metadata) {
	st := reflect.TypeOf(*a)

	for i := 0; i < st.NumField(); i++ {
		metadataTag := st.Field(i).Tag.Get("metadata")
		if metadataTag != "" {
			data, err := m.GetMetadata(metadataTag)
			if err != nil {
				continue
			}

			reflect.ValueOf(a).Elem().Field(i).SetString(data)
		}
	}
}

// NewAWS returns an AWSStats if the current machine is an AWS
// instance otherwise it returns nil.
func NewAWS() (i *AWSStats) {
	metadata := ec2metadata.New(session.New())

	// Verify that this is in fact an AWS machine.
	if !metadata.Available() {
		return nil
	}

	i = &AWSStats{}
	i.parseMetadata(metadata)

	data, err := metadata.GetMetadata("spot/termination")
	if err == nil {
		i.Spot.Termination = data
	}

	return
}
