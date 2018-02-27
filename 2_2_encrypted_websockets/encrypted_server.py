"""
Simple Python server program.

Waits for a client to connect, then sends a message. The message will be
encrypted under a key, so be sure to call decrypt() before printing!
"""
__author__ = "Charlie Friend"

import pyDes
import socket

KEY = "WHATEVENISCRYPTO"

MESSAGE = "Shh...secret message"


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Listen on port 50000
    print("Waiting for connections on port 50000...")
    sock.bind(('', 50000))
    sock.listen()               # lets the socket listen for clients
    conn, addr = sock.accept()  # wait for a client to connect!

    # encode the message into binary
    encoded_message = MESSAGE.encode()

    # create your cipher, encrypt your binary message
    cipher = pyDes.triple_des(KEY, padmode=pyDes.PAD_PKCS5)
    encrypted_message = cipher.encrypt(encoded_message)

    # A client connected - send it a message!
    print("Connected to " + addr[0] + "!")
    print("Sending message: " + MESSAGE)
    conn.sendall(encrypted_message)

    # Always CLOSE the socket when you're done sending messages. This tells the
    # client that we're done talking, so it can shut down too.
    print("Sent a message! Shutting down...")
    sock.close()


if __name__ == "__main__":
    main()
