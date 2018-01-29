"""
Decrypts secret messages from code_encryptor.py
"""
__author__ = "Charlie Friend"

import binascii
import pyDes


def main():
    # get your message from hex
    encrypted_message_hex = input("Enter encrypted message: ")
    encrypted_message = binascii.unhexlify(encrypted_message_hex)

    # make your cipher
    cipher = pyDes.triple_des("WHATEVENISCRYPTO", padmode=pyDes.PAD_PKCS5)
    decrypted_message = cipher.decrypt(encrypted_message)

    # decode and print your message
    print(decrypted_message.decode())


if __name__ == "__main__":
    main()
