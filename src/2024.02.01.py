def caesar_encryption_algorithm(p_string):
    p_string = str(p_string.lower())
    v_encrypted = ""
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a',
                'b', 'c', '1', '2', '3', '4', '5', '6', '7',
                '8', '9', '1', '2', '3']

    for character in p_string:
        index = 0
        for i in range(len(alphabet)):
            if character == alphabet[i]:
                index = i
                break
            else:
                index = -1

        if index == -1:
            v_encrypted += character
        else:
            v_encrypted += alphabet[index + 3]

    return v_encrypted


def main():
    print("This program encrypts your string with the caesar cipher algorithm.")
    v_string = input("Please insert your string to be encrypted: ")

    print(f"Your encrypted string looks like this: {caesar_encryption_algorithm(v_string)}")


if __name__ == '__main__':
    main()
