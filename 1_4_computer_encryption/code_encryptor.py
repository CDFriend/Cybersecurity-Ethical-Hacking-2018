"""
Encrypts a secret message using triple DES.
"""
__author__ = "Charlie Friend"

import pyDes


def main():
    message = input("Enter a message: ")

    cipher = pyDes.triple_des("WHATEVENISCRYPTO", padmode=pyDes.PAD_PKCS5)
    out = cipher.encrypt(message)

    print()
    print("Your encrypted message: " + out.hex())


if __name__ == "__main__":
    main()
