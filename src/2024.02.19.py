from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def rsa_generate_key_pair():
    key = RSA.generate(2048)
    return key


def rsa_encrypt(public_key, plaintext):
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext


def main():
    print("This script encrypts a String with the RSA Cipher.")

    key_pair = rsa_generate_key_pair()
    public_key = key_pair.publickey().export_key()

    public_key = RSA.import_key(public_key)

    plaintext = b"This is a sample text!"

    ciphertext = rsa_encrypt(public_key, plaintext)
    print("Ciphertext:", ciphertext)


if __name__ == '__main__':
    main()
