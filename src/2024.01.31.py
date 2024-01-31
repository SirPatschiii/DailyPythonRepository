def karacas_encryption_algorithm(p_input):
    p_input = p_input.lower()
    v_pre_encrypt = ""
    v_encrypt = ""

    for character in reversed(p_input):
        v_pre_encrypt += character

    for character in v_pre_encrypt:
        match character:
            case "a":
                v_encrypt += "0"
                continue
            case "e":
                v_encrypt += "1"
                continue
            case "i":
                v_encrypt += "2"
                continue
            case "o":
                v_encrypt += "2"
                continue
            case "u":
                v_encrypt += "3"
                continue
            case _:
                v_encrypt += character

    v_encrypt += "aca"

    return v_encrypt


def main():
    print("This program encrypts your string with the karacas_encryption_algorithm.")
    v_string = str(input("Please insert your string to be encrypted: "))

    print(f"Your string encrypted looks like this: {karacas_encryption_algorithm(v_string)}")


if __name__ == '__main__':
    main()
