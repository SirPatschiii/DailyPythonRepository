from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad


def aes_encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext


def main():
    print("This script encrypts a String with the AES Cipher.")

    key = get_random_bytes(32)
    plaintext = b"This is a sample text!"

    ciphertext = aes_encrypt(key, plaintext)
    print("Ciphertext:", ciphertext)


if __name__ == '__main__':
    main()
