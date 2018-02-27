"""
Simple Python client program.

Receives a message from a server, decrypts it and exits.
"""
__author__ = "Charlie Friend"

import pyDes
import socket

KEY = "WHATEVENISCRYPTO"

SERVER_IP = "127.0.0.1"
SERVER_PORT = 50000


def main():
    # Make a socket and connect to the server
    print("Connecting to " + SERVER_IP + ":" + str(SERVER_PORT))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER_IP, SERVER_PORT))

    # Recieve a message (we'll wait to recieve 1024 bytes, or 1 kilobyte)
    sock.settimeout(3.0)
    server_message_binary = sock.recv(1024)

    # Create your cipher and decrypt the message
    cipher = pyDes.triple_des(KEY, padmode=pyDes.PAD_PKCS5)
    decrypted_message_bytes = cipher.decrypt(server_message_binary)

    # Decode your newly decrypted message
    server_message = decrypted_message_bytes.decode()

    # Print the message and shut down
    print("Got message from server: " + server_message)
    print("Shutting down...")
    sock.close()


if __name__ == "__main__":
    main()
