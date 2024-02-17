from Crypto.Cipher import ARC4
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def arc4_encrypt(key, plaintext):
    cipher = ARC4.new(key)
    ciphertext = cipher.encrypt(pad(plaintext, ARC4.block_size))
    return ciphertext


def arc4_decrypt(key, ciphertext):
    cipher = ARC4.new(key)
    plaintext = unpad(cipher.decrypt(ciphertext), ARC4.block_size)
    return plaintext


def main():
    print("This script encrypts and decrypts a String with the ARC4 Cipher.")

    key = get_random_bytes(16)
    plaintext = b"This is a sample text!"

    ciphertext = arc4_encrypt(key, plaintext)
    print("Ciphertext:", ciphertext)

    decrypted_text = arc4_decrypt(key, ciphertext)
    print("Decrypted text:", decrypted_text.decode())


if __name__ == '__main__':
    main()
