"""
Login Program
Asks for a password, and checks that the hash is correct. If it is, then the
password is correct!
"""

__author__ = "Charlie Friend"

import hashlib
from getpass import getpass


def main():
    # Get password from the user
    password = getpass("Please enter your password: ")

    # Calculate hash of the provided password
    password_bin = password.encode()
    password_hash = hashlib.sha256(password_bin).hexdigest()

    # Read the password from the password hasher program
    with open("pwdhash.txt", "r") as infile:
        correct_hash = infile.read()

    if password_hash == correct_hash:
        print("Welcome!")
    else:
        print("Incorrect password.")


if __name__ == "__main__":
    main()
