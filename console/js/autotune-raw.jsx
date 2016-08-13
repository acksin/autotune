/* Acksin Autotune - Linux Diagnostics
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

var AcksinAutotuneRAW  = React.createClass({
  getInitialState: function() {
    return {
      content: [],
    }
  },
  componentDidMount: function() {
    if(this.props.statsId == "") {
      return;
    }

    $.get(BridgeAPI + "/v1/autotune/stats/" + this.props.statsId , function(result) {
      $.get(result.URL, function(stats) {
        var s = JSON.parse(stats);
        var c = [];

        c.push(<AcksinAutotuneCloud key="cloud" cloud={s.Cloud} />);
        c.push(<AcksinAutotuneSystem key="system" system={s.System} />);
        c.push(<AcksinAutotuneContainer key="container" container={s.Container} />);
        c.push(<AcksinAutotuneProcesses key="processes" processes={s.Processes} />);

        this.setState({
          content: c,
          stats: s,
        });
      }.bind(this));
    }.bind(this));
  },
  render: function() {
    return (
        <div>
          <AcksinAutotuneNav statsId={this.props.statsId} />

          {this.state.content}
        </div>
    );
  }
});
