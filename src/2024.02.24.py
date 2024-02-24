from Crypto.Cipher import CAST
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from binascii import hexlify, unhexlify


def cast_encrypt(p_key, p_plaintext):
    cipher = CAST.new(p_key, CAST.MODE_ECB)
    padded_plaintext = pad(p_plaintext.encode(), 8)
    ciphertext = cipher.encrypt(padded_plaintext)
    return hexlify(ciphertext).decode()


def cast_decrypt(p_key, p_ciphertext):
    cipher = CAST.new(p_key, CAST.MODE_ECB)
    decrypted_text = cipher.decrypt(unhexlify(p_ciphertext))
    decrypted_text = unpad(decrypted_text, 8).decode()
    return decrypted_text


def main():
    print("This script encrypts and decrypts a String with the CAST Cipher.")

    key = get_random_bytes(16)

    plaintext = input("Please insert your String to be encrypted: ")

    ciphertext = cast_encrypt(key, plaintext)
    print(f"Cipher String: {ciphertext}")

    decrypted_text = cast_decrypt(key, ciphertext)
    print(f"Decrypted String: {decrypted_text}")


if __name__ == '__main__':
    main()
