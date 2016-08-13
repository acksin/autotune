/* Acksin Autotune - Linux Diagnostics
 * Copyright (C) 2016 Acksin <hey@acksin.com>
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */

var AcksinAutotuneTable = React.createClass({
  render: function() {
    var property = this.props.property;

    if(Array.isArray(property)) {
      var its = []

      for(var i in property) {
        its.push(
          <tr key={i}>
            <td><AcksinAutotuneTable property={property[i]} /></td>
          </tr>
        );
      }

      return (
        <table className="table">
          {its}
        </table>
      );
    } else if(typeof property == "object") {
      var its = []

      for(var i in property) {
        its.push(
          <tr key={i}>
            <td><strong>{i}</strong></td>
            <td><AcksinAutotuneTable property={property[i]} /></td>
          </tr>
        );
      }

      return (
        <table className="table">
          {its}
        </table>
      );
    }

    return (
      <span>{property}</span>
    );
  }
});
