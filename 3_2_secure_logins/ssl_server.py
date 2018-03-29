"""
Simple Python server program.
Waits for a client to connect, then sends a message. Connection should
be encrypted by the provided certificates!
"""
__author__ = "Charlie Friend"

import ssl
import socket

MESSAGE = "Hello World! :D"


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Listen on port 50000
    print("Waiting for connections on port 50000...")
    sock.bind(('', 50000))
    sock.listen()               # lets the socket listen for clients
    conn, addr = sock.accept()  # wait for a client to connect!

    # wrap_socket 'wraps' the new connection object with SSL and gives a new
    # encrypted connection object. Use this to transmit/receive!
    ssl_conn = ssl.wrap_socket(conn,
                               certfile='mypublickey.pem',
                               keyfile='myprivatekey.pk',
                               server_side=True)

    # encode the message into binary
    encoded_message = MESSAGE.encode()

    # A client connected - send it a message!
    print("Connected to " + addr[0] + "!")
    print("Sending message: " + MESSAGE)
    ssl_conn.sendall(encoded_message)

    # Always CLOSE the socket when you're done sending messages. This tells the
    # client that we're done talking, so it can shut down too.
    print("Sent a message! Shutting down...")
    ssl_conn.close()


if __name__ == "__main__":
    main()
