"""
PyDES file encryptor.
"""
__author__ = "Charlie Friend"

import sys
import pyDes

KEY = "WHATEVENISCRYPTO"


def main():
    file_name = sys.argv[1]

    # read file
    with open(file_name, "r") as file:
        file_data = file.read()

    cipher = pyDes.triple_des(KEY, padmode=pyDes.PAD_PKCS5)
    encrypted_file_data = cipher.encrypt(file_data)

    encrypted_file_name = file_name + ".enc"
    with open(encrypted_file_name, "wb") as file:
        file.write(encrypted_file_data)

    print("Wrote encrypted file: " + encrypted_file_name)


if __name__ == "__main__":
    main()
