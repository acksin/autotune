/*
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

package stats

import (
	"encoding/json"
	"fmt"
	"sort"

	"github.com/abhiyerra/gojsonexplode"
)

// JSON returns JSON string of Stats
func (n *Stats) JSON() string {
	js, err := json.MarshalIndent(n, "", "  ")
	if err != nil {
		return ""
	}

	return string(js)
}

// Flat returns a flattened results.
func (n *Stats) Flat() string {
	o, err := gojsonexplode.Explodejsonstr(n.JSON(), ".")
	if err != nil {
		fmt.Println(err)
		return ""
	}

	var out map[string]interface{}

	err = json.Unmarshal([]byte(o), &out)
	if err != nil {
		fmt.Println(err)
		return ""
	}

	var o2 string
	var keys []string

	for k := range out {
		keys = append(keys, k)
	}
	sort.Strings(keys)

	for _, k := range keys {
		o2 += fmt.Sprintf("%s = %v\n", k, out[k])
	}

	return o2
}
