# -*- coding: utf-8 -*-
"""Find Jellyfin servers on the local network.

A server with auto discovery enabled (its network settings) answers a UDP
broadcast of ``who is JellyfinServer?`` on port 7359 with a JSON description
of itself.

**The replies are not authenticated.** Anything on the network can answer,
with any name and any address, and the address a real server advertises is
usually plain ``http://``. Show people the address a reply carries and let
them choose it; do not sign in to one automatically.
"""

import json
import logging
import socket
import time

#################################################################################################

LOG = logging.getLogger('JELLYFIN.' + __name__)

DISCOVERY_PORT = 7359
DISCOVERY_MESSAGE = b"who is JellyfinServer?"

#################################################################################################


def discover_servers(timeout=1.0, address=("<broadcast>", DISCOVERY_PORT)):
    """Broadcast for servers and return the replies that arrive in time.

    Each server is its own reply dict -- ``Id``, ``Name``, ``Address`` and
    usually ``EndpointAddress`` -- once per ``Id``, in the order they
    answered. A reply that is not JSON, or has no ``Id`` or ``Address``, is
    dropped.

    Blocks for the whole of ``timeout`` seconds, because nothing says when
    the last server has answered, so call it off the UI thread. Never raises
    for a network failure: it logs one and returns what it has.

    ``address`` is where the query goes; the default is the local broadcast
    address.
    """
    servers = []
    seen = set()

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except OSError:
        LOG.exception("Could not open a socket for server discovery")
        return servers

    with sock:
        try:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.sendto(DISCOVERY_MESSAGE, address)
        except OSError:
            LOG.exception("Could not send the server discovery query")
            return servers

        # One deadline for the whole wait. A timeout set once on the socket
        # restarts with every reply, so a steady trickle of them never ends.
        deadline = time.monotonic() + timeout
        while True:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                break
            sock.settimeout(remaining)
            try:
                data, _sender = sock.recvfrom(65535)
            except socket.timeout:
                break
            except ConnectionResetError:
                # Windows reports an ICMP port-unreachable caused by the send
                # on a later read of the socket. It says nothing about the
                # replies still on their way.
                continue
            except OSError:
                LOG.exception("Server discovery stopped reading replies")
                break

            try:
                info = json.loads(data)
            except ValueError:
                LOG.debug("Ignoring a discovery reply that is not JSON: %r",
                          data[:200])
                continue
            if (not isinstance(info, dict) or not info.get("Id")
                    or not info.get("Address")):
                LOG.debug("Ignoring a discovery reply with no Id or Address: %r",
                          info)
                continue
            if info["Id"] in seen:
                continue
            seen.add(info["Id"])
            servers.append(info)

    LOG.info("Found Servers: %s", servers)
    return servers
