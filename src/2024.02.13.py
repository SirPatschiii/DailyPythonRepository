from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad


def des_encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))
    return ciphertext


def main():
    print("This script encrypts a String with the DES Cipher.")

    key = get_random_bytes(8)
    plaintext = b"This is a sample text!"

    ciphertext = des_encrypt(key, plaintext)
    print("Ciphertext:", ciphertext)


if __name__ == '__main__':
    main()
