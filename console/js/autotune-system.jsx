/* Acksin Autotune - Linux Diagnostics
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

var AcksinAutotuneSystem  = React.createClass({
  getInitialState: function() {
    return null;
  },
  render: function() {
    return (
      <div>
        <h2>System</h2>

        <AcksinAutotuneSystemMemory memory={this.props.system.Memory} />
        <AcksinAutotuneSystemDisk disk={this.props.system.Disk} />
        <AcksinAutotuneSystemNetwork network={this.props.system.Network} />
        <AcksinAutotuneSystemKernel kernel={this.props.system.Kernel} />
      </div>
    );
  }
});

var AcksinAutotuneSystemMemory  = React.createClass({
  render: function() {
    return (
      <div>
        <h3>Memory</h3>

        <AcksinAutotuneTable property={this.props.memory} />
      </div>
    );
  }
});

var AcksinAutotuneSystemDisk  = React.createClass({
  render: function() {
    return (
      <div>
        <h3>Disk</h3>

        <AcksinAutotuneTable property={this.props.disk} />
      </div>
    );
  }
});

var AcksinAutotuneSystemNetwork  = React.createClass({
  render: function() {
    return (
      <div>
        <h3>Network</h3>

        <AcksinAutotuneTable property={this.props.network} />
      </div>
    );
  }
});

var AcksinAutotuneSystemKernel  = React.createClass({
  render: function() {
    return (
      <div>
        <h3>Kernel</h3>

        <AcksinAutotuneTable property={this.props.kernel} />
      </div>
    );
  }
});
