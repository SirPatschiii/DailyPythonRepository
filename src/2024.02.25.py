from Crypto.Hash import HMAC, SHA512


def get_hmac_digest(p_secret_key: bytes, p_message: bytes) -> bytes:
    hmac_object = HMAC.new(key=p_secret_key, digestmod=SHA512)
    hmac_object.update(msg=p_message)
    return hmac_object.digest()


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
    print("This script checks a message for a manipulation using HMAC.")

    print("\nThis is now representing the sending side.")
    secret_key_sender = input("Please insert your secret key: ").encode('utf-8')
    message_sender = input("Please insert your message you want to send to the receiver: ").encode('utf-8')

    print("\nThis is now representing the receiving side.")
    secret_key_receiver = input("Please insert the key you and the sender agreed to: ").encode('utf-8')
    message_receiver = input("Please insert now your received message: ").encode('utf-8')

    digest_sender = get_hmac_digest(secret_key_sender, message_sender)
    digest_receiver = get_hmac_digest(secret_key_receiver, message_receiver)

    if digest_sender == digest_receiver:
        print_green("\nHMAC verification successful. Message integrity and authenticity verified.")
    else:
        print_red("\nHMAC verification failed. Message may have been manipulated.")

    print(f"HMAC digest of sender:   {digest_sender.hex()}")
    print(f"HMAC digest of receiver: {digest_receiver.hex()}")


if __name__ == '__main__':
    main()
