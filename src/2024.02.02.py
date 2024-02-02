def substitution_encryption_algorithm(p_string):
    p_string = str(p_string)
    v_encrypted = ""
    alphabet = [
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
         'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '.', ',', '_', '<',
         '>', '!', '%', '&', '/', '(', ')', '?', '*', '-', '+'],
        ['?', 'd', 'V', '1', 'W', '%', 's', 'U', 'r', 'a', 'u', '6', '-', 'F', 'i', 'c', 'T', 'K', '/', 'v', 'G', 'h',
         'z', '.', 'g', '*', ' ', 'm', 'k', 'l', '9', 'w', 'b', 'Q', ')', 'e', 'n', 'I', 'p', '8', '5', 'P', 'y', 'M',
         '7', 'B', 'L', '&', '>', 'O', 'A', 'E', 'Z', 'x', 'C', 'N', 'o', '+', 'J', 'D', 'X', '2', 'H', '<', 't', 'Y',
         '!', '(', '_', '4', ',', 'j', 'q', 'f', '3', 'R', 'S']]

    for character in p_string:
        index = 0
        for i in range(len(alphabet[0])):
            if character == alphabet[0][i]:
                index = i
                break
            else:
                index = -1

        if index == -1:
            v_encrypted += character
        else:
            v_encrypted += alphabet[1][index]

    return v_encrypted


def substitution_decryption_algorithm(p_encrypted):
    p_encrypted = str(p_encrypted)
    v_decrypted = ""
    alphabet = [
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
         'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '.', ',', '_', '<',
         '>', '!', '%', '&', '/', '(', ')', '?', '*', '-', '+'],
        ['?', 'd', 'V', '1', 'W', '%', 's', 'U', 'r', 'a', 'u', '6', '-', 'F', 'i', 'c', 'T', 'K', '/', 'v', 'G', 'h',
         'z', '.', 'g', '*', ' ', 'm', 'k', 'l', '9', 'w', 'b', 'Q', ')', 'e', 'n', 'I', 'p', '8', '5', 'P', 'y', 'M',
         '7', 'B', 'L', '&', '>', 'O', 'A', 'E', 'Z', 'x', 'C', 'N', 'o', '+', 'J', 'D', 'X', '2', 'H', '<', 't', 'Y',
         '!', '(', '_', '4', ',', 'j', 'q', 'f', '3', 'R', 'S']]

    for character in p_encrypted:
        index = 0
        for i in range(len(alphabet[0])):
            if character == alphabet[1][i]:
                index = i
                break
            else:
                index = -1

        if index == -1:
            v_decrypted += character
        else:
            v_decrypted += alphabet[0][index]

    return v_decrypted


def main():
    print("This program encrypts your string with the substitution cipher algorithm.")
    v_string = input("Please insert your string to be encrypted: ")
    v_encrypted = substitution_encryption_algorithm(v_string)
    v_decrypted = substitution_decryption_algorithm(v_encrypted)

    print(f"Your encrypted string looks like this: {v_encrypted}")
    print(f"Your decrypted string (your inserted one) should be this: {v_decrypted}")


if __name__ == '__main__':
    main()
