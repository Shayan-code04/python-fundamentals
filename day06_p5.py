# day06_p5.py

def caesar_encrypt(text, shift):
    """
    Encrypts text using Caesar cipher with a given shift.

    Args:
        text (str): Plaintext to encrypt.
        shift (int): Number of positions to shift each character.
    Returns:
        str: Encrypted ciphertext.
    """
    result = ""
    shift = shift % 26  # handles shifts > 26

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char  # non-letters stay unchanged

    return result


def caesar_decrypt(text, shift):
    """
    Decrypts a Caesar cipher text by reversing the shift.

    Args:
        text (str): Ciphertext to decrypt.
        shift (int): The shift that was used during encryption.
    Returns:
        str: Decrypted plaintext.
    """
    return caesar_encrypt(text, -shift)


def main():
    print(f"{'Caesar Cipher':^40}")
    print(f"{'=' * 40}")

    text = input("Enter text: ").strip()

    shift_input = input("Enter shift (1–25): ").strip()
    if not shift_input.isdigit():
        print("Invalid shift. Must be a number.")
        return

    shift = int(shift_input)
    encrypted = caesar_encrypt(text, shift)
    decrypted = caesar_decrypt(encrypted, shift)

    print(f"\n{'Original ':<12}: {text}")
    print(f"{'Encrypted':<12}: {encrypted}")
    print(f"{'Decrypted':<12}: {decrypted}")
    print(f"{'Match':<12}: {decrypted == text}")


if __name__ == "__main__":
    main()