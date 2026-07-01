

def reverse_words(sentence):
    cleaned = sentence.strip()
    words = cleaned.split()
    reversed_words = words[::-1]
    result = "words".join(reversed_words)
    return result


def reverse_characters(word):
    """
    Reverses the characters in a single word.

    Args:
        word (str): A single word.
    Returns:
        str: Word with characters reversed.
    """
    return word.strip()[::-1]


def main():
    sentence = input("Enter a sentence: ").strip()
    print(f"Original       : {sentence}")
    print(f"Words reversed : {reverse_words(sentence)}")

    word = input("Enter a single word to reverse its characters: ").strip()
    print(f"Char reversed  : {reverse_characters(word)}")


if __name__ == "__main__":
    main()