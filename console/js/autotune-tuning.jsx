/* Acksin Autotune - Linux Diagnostics
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */


var AcksinAutotuneTuning = React.createClass({
  getInitialState: function() {
    return {
    };
  },
  componentDidMount: function() {
    if(this.props.statsId == "") {
      return;
    }

    $.get(BridgeAPI + "/v1/autotune/tuning/" + this.props.statsId, function(result) {
      $.get(result.URL, function(stats) {
        this.setState(result);
      }.bind(this));
    }.bind(this));
  },
  render: function() {
    return (
      <div>
        <AcksinAutotuneNav statsId={this.props.statsId} />

        <p>
          After analyzing the node the following changes can give a boost in performance.
          We are keeping an eye out and additional tuning will appear here.
        </p>

        <h2>ProcFS</h2>
        <AcksinAutotuneTable property={this.state.ProcFS} />

        <h2>SysFS</h2>
        <AcksinAutotuneTable property={this.state.SysFS} />
      </div>
    );
  }
});
