# Copyright (C) 2016 Acksin <hey@acksin.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from decorators import *
import mental_model

class Networking(mental_model.MentalModel):
    """
    References:

    http://vincent.bernat.im/en/blog/2014-tcp-time-wait-state-linux.html
    https://rtcamp.com/tutorials/linux/sysctl-conf/
    https://fasterdata.es.net/host-tuning/linux/
    http://cherokee-project.com/doc/other_os_tuning.html
    https://easyengine.io/tutorials/linux/sysctl-conf/
    https://access.redhat.com/sites/default/files/attachments/20150325_network_performance_tuning.pdf
    """

    def __init__(self, machine):
        self.machine = machine

        self.vars = {
            'nfConntrackMax': 200000
        }

    @procfs_feature
    def procfs_net_ipv4_tcp_fin_timeout(self):
        """
        Usually, the Linux kernel holds a TCP connection even after it
        is closed for around two minutes. This means that there may be
        a port exhaustion as the kernel waits to close the
        connections. By moving the fin_timeout to 15 seconds we
        drastically reduce the length of time the kernel is waiting
        for the socket to get any remaining packets.
        """

        return {
            "/proc/sys/net/ipv4/tcp_fin_timeout": "15"
        }

    @procfs_feature
    def procfs_net_ipv4_ip_local_port_range(self):
        """
        On a typical machine there are around 28,000 ports available to be
        bound to. This number can get exhausted quickly if there are many
        connections. We will increase this.
        """

        return {
            "/proc/sys/net/ipv4/ip_local_port_range": "1024 65535",
        }

    @procfs_feature
    def procfs_net_core_rmem_max(self):
        """
        The size of the receive buffer for all the sockets. 16MB per socket.
        """

        # TODO: Adjust this per the instance size.

        return {
            "/proc/sys/net/core/rmem_max": "16777216"
        }

    @procfs_feature
    def procfs_net_core_wmem_max(self):
        """
        The size of the buffer for all the sockets. 16MB per socket.
        """

        # TODO: Adjust this per the instance size.

        return {
            "/proc/sys/net/core/wmem_max": "16777216",
        }

    @procfs_feature
    def procfs_net_ipv4_tcp_rmem(self):
        """
        (min, default, max): The sizes of the receive buffer for the IP protocol.
        """


        # TODO: Adjust this per the instance size.

        return {
            "/proc/sys/net/ipv4/tcp_rmem": "4096 87380 16777216",
        }

    @procfs_feature
    def procfs_net_ipv4_tcp_wmem(self):
        """
        (min, default, max): The sizes of the write buffer for the IP protocol.
        """

        # TODO: Adjust this per the instance size.

        return {
            "/proc/sys/net/ipv4/tcp_wmem": "4096 65536 16777216",
        }

    @procfs_feature
    def procfs_net_ipv4_tcp_max_syn_backlog(self):
        """
        Increase the number syn requests allowed. Sets how many half-open connections to backlog queue
        """

        # TODO: Adjust this per the instance size.

        return {
            "/proc/sys/net/ipv4/tcp_max_syn_backlog": "20480",
        }

    @procfs_feature
    def procfs_net_ipv4_tcp_syncookies(self):
        """
        Security to prevent DDoS attacks. http://cr.yp.to/syncookies.html
        """

        return {
            "/proc/sys/net/ipv4/tcp_syncookies": "1",
        }

    @procfs_feature
    def procfs_net_ipv4_tcp_no_metrics_save(self):
        """
        TCP saves various connection metrics in the route cache when the
        connection closes so that connections established in the near future
        can use these to set initial conditions. Usually, this increases
        overall performance, but may sometimes cause performance
        degradation.
        """

        return {
            "/proc/sys/net/ipv4/tcp_no_metrics_save": "1",
        }

    @procfs_feature
    def procfs_net_core_somaxconn(self):
        """
        The maximum number of queued sockets on a connection.
        """

        return {
            "/proc/sys/net/core/somaxconn": "16096",
        }

    @procfs_feature
    def procfs_net_core_netdev_max_backlog(self):
        """
        The number of incoming connections on the backlog queue. The maximum
        number of packets queued on the INPUT side.
        """

        return {
            "/proc/sys/net/core/netdev_max_backlog": "30000",
        }

    @procfs_feature
    def procfs_net_ipv4_tcp_max_tw_buckets(self):
        """
        Increase the tcp-time-wait buckets pool size to prevent simple DOS attacks
        """

        return {
            "/proc/sys/net/ipv4/tcp_max_tw_buckets": "400000",
        }

    @procfs_feature
    def procfs_net_ipv4_tcp_syn_retries(self):
        """
        Number of times initial SYNs for a TCP connection attempt will
        be retransmitted for outgoing connections.
        """

        return {
            "/proc/sys/net/ipv4/tcp_syn_retries": "2",
        }

    @procfs_feature
    def procfs_net_ipv4_tcp_synack_retries(self):
        """
        This setting determines the number of SYN+ACK packets sent before
        the kernel gives up on the connection
        """

        return {
            "/proc/sys/net/ipv4/tcp_synack_retries": "2",
        }

    @procfs_feature
    def procfs_net_netfilter_nf_conntrack_max(self):
        """
        The max is double the previous value.
        https://wiki.khnet.info/index.php/Conntrack_tuning
        """

        return {
            "/proc/sys/net/netfilter/nf_conntrack_max": self.vars['nfConntrackMax'],
        }

    @procfs_feature
    def procfs_net_ipv4_tcp_tw_reuse(self):
        """
        """

        return {
            "/proc/sys/net/ipv4/tcp_tw_reuse": "1",
        }

    @sysfs_feature
    def sysfs_nf_conntrack_hashsize(self):
        """
        """

        return {
            "/sys/module/nf_conntrack/parameters/hashsize": self.vars["nfConntrackMax"] / 4
        }
