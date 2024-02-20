from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def rsa_generate_key_pair():
    key = RSA.generate(2048)
    return key


def rsa_encrypt(public_key, plaintext):
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext


def rsa_decrypt(private_key, ciphertext):
    cipher = PKCS1_OAEP.new(private_key)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext


def main():
    print("This script encrypts a String with the RSA Cipher.")

    key_pair = rsa_generate_key_pair()
    private_key = key_pair.export_key()
    public_key = key_pair.publickey().export_key()

    private_key = RSA.import_key(private_key)
    public_key = RSA.import_key(public_key)

    plaintext = b"This is a sample text!"

    ciphertext = rsa_encrypt(public_key, plaintext)
    print("Ciphertext:", ciphertext)

    decrypted_text = rsa_decrypt(private_key, ciphertext)
    print("Decrypted text:", decrypted_text.decode())


if __name__ == '__main__':
    main()
