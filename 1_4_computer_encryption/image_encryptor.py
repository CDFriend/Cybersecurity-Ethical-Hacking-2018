"""
PyDES image encryptor.
"""
__author__ = "Charlie Friend"

import sys
import pyDes


def main():
    file_name = sys.argv[1]
    with open(file_name, 'rb') as imagefile:
        image_bytes = imagefile.read()

    cipher = pyDes.triple_des("WHATEVENISCRYPTO", padmode=pyDes.PAD_PKCS5)
    encrypted_bytes = cipher.encrypt(image_bytes)

    with open(file_name + ".enc", 'wb') as encryptedfile:
        encryptedfile.write(encrypted_bytes)

    print("Wrote encrypted file to " + file_name + ".enc")


if __name__ == "__main__":
    main()
