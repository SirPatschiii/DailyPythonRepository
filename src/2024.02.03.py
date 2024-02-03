def vigenere_encryption_cipher(p_string, key):
    p_string = str(p_string)
    encrypted_text = ""
    v_key_length = len(key)

    for i in range(len(p_string)):
        character = p_string[i]
        if character.isalpha():
            shift = ord(key[i % v_key_length].upper()) - ord('A')

            if character.isupper():
                encrypted_character = chr((ord(character) + shift - ord('A')) % 26 + ord('A'))
            else:
                encrypted_character = chr((ord(character) + shift - ord('a')) % 26 + ord('a'))

            encrypted_text += encrypted_character
        else:
            encrypted_text += character

    return encrypted_text


def vigenere_decryption_cipher(p_encrypted, key):
    p_encrypted = str(p_encrypted)
    v_decrypted = ""
    v_key_length = len(key)

    for i in range(len(p_encrypted)):
        character = p_encrypted[i]
        if character.isalpha():
            shift = ord(key[i % v_key_length].upper()) - ord('A')

            if character.isupper():
                decrypted_character = chr((ord(character) - shift - ord('A')) % 26 + ord('A'))
            else:
                decrypted_character = chr((ord(character) - shift - ord('a')) % 26 + ord('a'))

            v_decrypted += decrypted_character
        else:
            v_decrypted += character

    return v_decrypted


def main():
    print("This program encrypts your string with the vigenere cipher algorithm.")
    v_string = input("Please insert your string to be encrypted: ")
    key = input("Please insert your key for the encryption: ")
    v_encrypted = vigenere_encryption_cipher(v_string, key)
    v_decrypted = vigenere_decryption_cipher(v_encrypted, key)

    print(f"Your encrypted string looks like this: {v_encrypted}")
    print(f"Your decrypted string (your inserted one) should be this: {v_decrypted}")


if __name__ == '__main__':
    main()
