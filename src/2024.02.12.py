from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def aes_encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext


def aes_decrypt(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_text


def main():
    print("This script encrypts and decrypts a String with the AES Cipher.")

    key = get_random_bytes(32)
    plaintext = b"This is a sample text!"

    ciphertext = aes_encrypt(key, plaintext)
    print("Ciphertext:", ciphertext)

    decrypted_text = aes_decrypt(key, ciphertext)
    print("Decrypted text:", decrypted_text.decode())


if __name__ == '__main__':
    main()
