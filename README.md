# How to: Tunnel an OpenVPN connection via an OpenSSH Socks Proxy
This guide assumes a running OpenVPN server over TCP (depending on the network, it might also need to run on Port 443)

## Add socks proxy lines to OVPN file:
- socks-proxy localhost 6886
- socks-proxy-retry

## Add gateway route:
- route REMOTE-SERVER-IP 255.255.255.255 net_gateway default

