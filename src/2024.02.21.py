from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes


def cha_cha_20_encrypt(p_key, p_nonce, p_plaintext):
    cipher = ChaCha20.new(key=p_key, nonce=p_nonce)
    ciphertext = cipher.encrypt(p_plaintext)
    return ciphertext


def main():
    print("This script encrypts a String with the ChaCha20 Cipher.")

    key = get_random_bytes(32)
    nonce = get_random_bytes(8)

    plaintext = input("Please insert your String to be encrypted: ").encode("utf-8")

    ciphertext = cha_cha_20_encrypt(key, nonce, plaintext)
    print(f"Cipher String: {ciphertext.hex()}")


if __name__ == '__main__':
    main()
