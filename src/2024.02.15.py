from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad


def des3_encrypt(key, plaintext):
    cipher = DES3.new(key, DES3.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, DES3.block_size))
    return ciphertext


def main():
    print("This script encrypts a String with the DES3 Cipher.")

    key = get_random_bytes(24)
    plaintext = b"This is a sample text!"

    ciphertext = des3_encrypt(key, plaintext)
    print("Ciphertext:", ciphertext)


if __name__ == '__main__':
    main()

"""
"""
