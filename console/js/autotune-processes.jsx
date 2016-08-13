/* Acksin Autotune - Linux Diagnostics
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

var AcksinAutotuneProcesses  = React.createClass({
  getInitialState: function() {
    var c = [];

    for(var i = 0; i < this.props.processes.length; i++) {
      var proc = this.props.processes[i];

      c.push(
        <tr key={"proc" + i}>
          <td>{proc.Exe}</td>
          <td>
            <AcksinAutotuneTable property={proc.IO.FD} />
          </td>
        </tr>
      );
    }

    return {
      content: c,
    };
  },
  render: function() {
    return (
      <div>
        <h2>Processes</h2>

        <table className="table">
          <thead>
            <tr>
              <th>Exe</th>
              <th>IO</th>
            </tr>
          </thead>

          <tbody>
            {this.state.content}
          </tbody>
        </table>
      </div>
    );
  }
});
