"""
Port scanner utility.
"""
__author__ = "Charlie Friend"

import sys
import socket


def main():
    # Check that enough command-line arguments were provided
    if len(sys.argv) < 2:
        print("No address to scan provided!")

    # Find the IP address of the hostname you provided
    host_addr = socket.gethostbyname(sys.argv[1])

    print("Scanning host " + sys.argv[1] + " (" + host_addr + ")...")

    # Scan all port numbers between 1-1024. These are the ports which
    # we expect find specific types of servers (i.e. web servers, file
    # servers, remote access...)
    for port_num in range(1, 1024):

        # Try to connect to the port
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.3)  # time out after 3 seconds

            sock.connect((host_addr, port_num))

            protocol_name = socket.getservbyport(port_num)
            print("  " + str(port_num) + ": OPEN (" + protocol_name + ")")

        except (socket.timeout, ConnectionRefusedError):
            # If the socket timed out, then we weren't able to connect to
            # the port, so it's probably not open.
            pass


if __name__ == "__main__":
    main()
