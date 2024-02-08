import secrets


def generate_blowfish_key(p_key_length):
    if not (32 <= p_key_length <= 448):
        raise ValueError("Key length must be between 32 and 448 bits, inclusive.")

    v_key_bits = secrets.randbits(p_key_length)

    v_key_words = [(v_key_bits >> (32 * i)) & 0xFFFFFFFF for i in range(p_key_length // 32)]

    return v_key_words


def main():
    v_key_length = int(input("Enter the desired key length (between 32 and 448 bits): "))

    try:
        v_blowfish_key = generate_blowfish_key(v_key_length)
        print("Generated Blowfish Key:")
        print("key =", [f'0x{value:08X}' for value in v_blowfish_key])
        print(f"\nPlease save your key if you ever encrypt something with it, "
              f"because you will need it to decrypt your data as well")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
