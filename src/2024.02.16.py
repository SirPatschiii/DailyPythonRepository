from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def des3_encrypt(key, plaintext):
    cipher = DES3.new(key, DES3.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, DES3.block_size))
    return ciphertext


def des3_decrypt(key, ciphertext):
    cipher = DES3.new(key, DES3.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), DES3.block_size)
    return plaintext


def main():
    print("This script encrypts and decrypts a String with the DES3 Cipher.")

    key = get_random_bytes(24)
    plaintext = b"This is a sample text!"

    ciphertext = des3_encrypt(key, plaintext)
    print("Ciphertext:", ciphertext)

    decrypted_text = des3_decrypt(key, ciphertext)
    print("Decrypted text:", decrypted_text.decode())


if __name__ == '__main__':
    main()
