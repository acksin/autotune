/* Acksin STRUM - Linux Diagnostics
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

var AcksinStrumNav = React.createClass({
  getInitialState: function() {
    switch(document.location.pathname) {
      case "/console/autotune/":
        console.log("autotune");
        return {
          item: "autotune"
        }
    }

    return {
      item: "raw"
    }
  },
  isActive: function(item) {
    return this.state.item == item ? "active" : "";
  },
  render: function() {
    return (
      <ul className="nav nav-tabs">
        <li role="presentation" className={this.isActive("autotune")}>
          <a href={"/console/autotune/#/" + this.props.statsId}>Autotune</a>
        </li>
        <li role="presentation" className={this.isActive("raw")}>
          <a href={"/console/strum/#/" + this.props.statsId}>RAW</a>
        </li>
      </ul>
    );
  }
});
