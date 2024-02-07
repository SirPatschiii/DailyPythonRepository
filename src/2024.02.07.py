import secrets


def generate_blowfish_key(p_key_length):
    if not (32 <= p_key_length <= 448):
        raise ValueError("Key length must be between 32 and 448 bits, inclusive.")

    v_key_bits = secrets.randbits(p_key_length)

    v_key_hex = f'0x{v_key_bits:0{p_key_length // 4}X}'

    return v_key_hex


def main():
    v_key_length = int(input("Enter the desired key length (between 32 and 448 bits): "))

    try:
        v_blowfish_key = generate_blowfish_key(v_key_length)
        print(f"Generated Blowfish Key: {v_blowfish_key}")
        print("Please save your key if you ever encrypt something with it, because you will need it to decrypt your"
              " data as well")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
