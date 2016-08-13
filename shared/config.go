/* Acksin Autotune - Linux Diagnostics
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

package shared

import (
	"encoding/json"
	"errors"
	"io/ioutil"
)

// Config is the configuration used by the Autotune Agent.
type Config struct {
	APIKey string
	URL    string
}

// ParseConfig reads and validates a configuration file.
func ParseConfig(configFile string) (c *Config, err error) {
	c = &Config{}

	b, err := ioutil.ReadFile(configFile)
	if err != nil {
		return nil, err
	}

	err = json.Unmarshal(b, c)
	if err != nil {
		return nil, err
	}

	if c.APIKey == "" {
		return nil, errors.New("Set the `APIKey`. For Autotune Cloud this can be found at https://www.acksin.com/console/credentials")
	}

	return c, nil
}
