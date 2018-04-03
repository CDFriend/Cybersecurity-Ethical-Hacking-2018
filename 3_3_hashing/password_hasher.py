"""
Password Hasher Program
Takes a password as input and writes its hash into a file.
"""

__author__ = "Charlie Friend"

import hashlib
from getpass import getpass


def main():
    # Get the password from the command line. getpass() works the same as input(),
    # but won't print what you're writing to the command line!
    password = getpass("Enter a password: ")

    # Calculate the SHA-256 hash of the password
    password_bin = password.encode()
    password_hash = hashlib.sha256(password_bin).hexdigest()

    # Write the password hash to a file
    with open("pwdhash.txt", "w") as outfile:
        outfile.write(password_hash)


if __name__ == "__main__":
    main()
