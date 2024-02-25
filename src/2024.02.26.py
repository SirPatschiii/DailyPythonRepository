from Crypto.Hash import KMAC256
from Crypto.Random import get_random_bytes


def get_kmac_digest(p_secret_key: bytes, p_message: bytes) -> bytes:
    kmac_object = KMAC256.new(key=p_secret_key)
    kmac_object.update(p_message)
    return kmac_object.digest()


def print_red(text: str) -> None:
    """
        Prints the specified text in bright red color.

        Parameters:
        - text (str): The text to be printed in red. Must be a string.

        Raises:
        - TypeError: If the provided text is not a string.

        Usage:
        - Use print_red function to print text in red.
    """

    if not isinstance(text, str):
        raise TypeError("Text must be a string")

    print("\033[91m{}\033[0m".format(text))


def print_green(text: str) -> None:
    """
        Prints the specified text in bright green color.

        Parameters:
        - text (str): The text to be printed in green.

        Raises:
        - TypeError: If the provided text is not a string.

        Usage:
        - Use print_green function to print text in green.
    """

    if not isinstance(text, str):
        raise TypeError("Text must be a string")

    print("\033[92m{}\033[0m".format(text))


def main():
    print("This script checks a message for a manipulation using KMAC256.")

    key = get_random_bytes(32)

    print("\nThis is now representing the sending side.")
    secret_key_sender = key
    print(f"Your key is {secret_key_sender.hex()}.")
    message_sender = input("Please insert your message you want to send to the receiver: ").encode('utf-8')

    print("\nThis is now representing the receiving side.")
    secret_key_receiver = key
    print(f"Your key is {secret_key_receiver.hex()}.")
    message_receiver = input("Please insert now your received message: ").encode('utf-8')

    digest_sender = get_kmac_digest(secret_key_sender, message_sender)
    digest_receiver = get_kmac_digest(secret_key_receiver, message_receiver)

    if digest_sender == digest_receiver:
        print_green("\nKMAC verification successful. Message integrity and authenticity verified.")
    else:
        print_red("\nKMAC verification failed. Message may have been manipulated.")

    print(f"KMAC digest of sender:   {digest_sender.hex()}")
    print(f"KMAC digest of receiver: {digest_receiver.hex()}")


if __name__ == '__main__':
    main()
