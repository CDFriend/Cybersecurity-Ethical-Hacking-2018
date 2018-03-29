"""
Simple Python SSL client program.
Connects to a server, recieves a message and exits. Connection should
be encrypted using the server's public certificate!
"""

import ssl
import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 50000


def main():
    # Make a socket and connect to the server
    print("Connecting to " + SERVER_IP + ":" + str(SERVER_PORT))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ssl_sock = ssl.wrap_socket(sock)
    ssl_sock.connect((SERVER_IP, SERVER_PORT))

    # Recieve a message (we'll wait to recieve 1024 bytes, or 1 kilobyte)
    ssl_sock.settimeout(3.0)
    server_message_binary = ssl_sock.recv(1024)

    # Decode server message from binary
    server_message = server_message_binary.decode()

    # Print the message and shut down
    print("Got message from server: " + server_message)
    print("Shutting down...")
    sock.close()


if __name__ == "__main__":
    main()
