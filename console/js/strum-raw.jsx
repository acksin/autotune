/* Acksin STRUM - Linux Diagnostics
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

var AcksinStrumRAW  = React.createClass({
  getInitialState: function() {
    return {
      content: [],
    }
  },
  componentDidMount: function() {
    if(this.props.statsId == "") {
      return;
    }

    $.get(BridgeAPI + "/v1/strum/stats/" + this.props.statsId , function(result) {
      $.get(result.URL, function(stats) {
        var s = JSON.parse(stats);
        var c = [];

        c.push(<AcksinStrumCloud key="cloud" cloud={s.Cloud} />);
        c.push(<AcksinStrumSystem key="system" system={s.System} />);
        c.push(<AcksinStrumContainer key="container" container={s.Container} />);
        c.push(<AcksinStrumProcesses key="processes" processes={s.Processes} />);

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
          <AcksinStrumNav statsId={this.props.statsId} />

          {this.state.content}
        </div>
    );
  }
});
