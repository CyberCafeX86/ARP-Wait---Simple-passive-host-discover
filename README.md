# ARP-Wait - Simple passive host discover
A simple POC of a method to capture hosts on a local network without doing any noise.

## How it works?
It just waits ARP broadcast requests, many times sent by the router/gateway, it captures the IPs on the packets.

## Pros
- Capture hosts addresses without sending nothing on the network.

## Cons
- Not so reliable, depends on the router / hosts configuration about ARP settings.
