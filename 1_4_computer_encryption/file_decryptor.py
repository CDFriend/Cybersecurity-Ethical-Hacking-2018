"""
PyDES file decryptor.
"""
__author__ = "Charlie Friend"

import sys
import pyDes

KEY = "WHATEVENISCRYPTO"


def main():
    file_name = sys.argv[1]

    # read encrypted file bytes
    with open(file_name, 'rb') as file:
        encrypted_file_data = file.read()

    # decrypt file
    cipher = pyDes.triple_des(KEY, padmode=pyDes.PAD_PKCS5)
    file_data = cipher.decrypt(encrypted_file_data)

    # print decrypted text
    print(file_data.decode())


if __name__ == "__main__":
    main()
