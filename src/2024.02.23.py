from Crypto.Cipher import CAST
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from binascii import hexlify


def cast_encrypt(p_key, p_plaintext):
    cipher = CAST.new(p_key, CAST.MODE_ECB)
    padded_plaintext = pad(p_plaintext.encode(), 8)
    ciphertext = cipher.encrypt(padded_plaintext)
    return hexlify(ciphertext).decode()


def main():
    print("This script encrypts a String with the CAST Cipher.")

    key = get_random_bytes(16)

    plaintext = input("Please insert your String to be encrypted: ")

    ciphertext = cast_encrypt(key, plaintext)
    print(f"Cipher String: {ciphertext}")


if __name__ == '__main__':
    main()
