"""
Secure Instant Messaging Server
Connects to one client and exchanges messages.

Unfinished! This may have to be re-worked into a separate client and server.
"""

__author__ = "Charlie Friend"

import socket
import threading

RECEIVER_PORT = 50000


class Receiver(threading.Thread):

    def __init__(self, ip, port):
        super().__init__()
        self.ip = ip
        self.port = port

    def run(self):
        recv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        recv_socket.bind(('', self.port))
        recv_socket.listen()
        conn, addr = recv_socket.accept()

        print(addr + " connected!")

        while True:
            message = recv_socket.recv(1024)
            print()                          # print the message on a new line
            print("Message> " + message)


def main():
    ip = input("What address do you want to connect to? ")
    listen_port = int(input("Listen on what port? "))
    port = int(input("What port? "))

    receiver = Receiver(ip, listen_port)

    receiver.start()


if __name__ == "__main__":
    main()
