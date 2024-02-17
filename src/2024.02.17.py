from Crypto.Cipher import ARC4
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad


def arc4_encrypt(key, plaintext):
    cipher = ARC4.new(key)
    ciphertext = cipher.encrypt(pad(plaintext, ARC4.block_size))
    return ciphertext


def main():
    print("This script encrypts a String with the ARC4 Cipher.")

    key = get_random_bytes(16)
    plaintext = b"This is a sample text!"

    ciphertext = arc4_encrypt(key, plaintext)
    print("Ciphertext:", ciphertext)


if __name__ == '__main__':
    main()
