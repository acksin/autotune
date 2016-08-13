/* Acksin Autotune - Linux Diagnostics
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

var AcksinAutotuneContainer  = React.createClass({
  getInitialState: function() {
    return null;
  },
  render: function() {
    return (
      <div>
        <h2>Container</h2>

        <AcksinAutotuneContainerDocker docker={this.props.container.Docker} />
      </div>
    );
  }
});

var AcksinAutotuneContainerDocker  = React.createClass({
  getInitialState: function() {
    var containersTable = [];
    var imagesTable = [];

    for(var k in this.props.docker.Containers) {
      contaienrsTable.push(
        <tr key={k}>
          <td>{k}</td>
          <td>{JSON.stringify(this.props.docker.Containers[k])}</td>
        </tr>
      );
    };

    for(k in this.props.docker.Images) {
      var image = this.props.docker.Images[k];
      imagesTable.push(
        <tr key={k}>
          <td>
            <table className="table">
              <tr>
                <td><b>ID</b></td>
                <td>{image.Id}</td>
              </tr>
              <tr>
                <td><b>Repo Tags</b></td>
                <td>{image.RepoTags}</td>
              </tr>
              <tr>
                <td><b>Labels</b></td>
                <td>{JSON.stringify(image.Labels)}</td>
              </tr>
            </table>
          </td>
        </tr>
      );
    };

    return {
      containersTable: containersTable,
      imagesTable: imagesTable,
    }
  },
  render: function() {
    return (
      <div>
        <h3>Docker</h3>


        <div>
          <h4>Containers</h4>
          <table className="table">
            {this.state.containersTable}
          </table>
        </div>

        <div>
          <h4>Images</h4>
          <table className="table">
            {this.state.imagesTable}
          </table>
        </div>

      </div>
    );
  }
});
