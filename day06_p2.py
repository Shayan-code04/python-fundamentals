# day06_p2.py

def count_vowels(text):
    """
    Counts vowels and consonants in a given text.

    Args:
        text (str): Input text from user.
    Returns:
        dict: Dictionary with vowel count, consonant count, and found vowels.
    """
    cleaned = text.strip().lower()
    vowels = "aeiou"
    vowel_list = [ch for ch in cleaned if ch in vowels]
    consonant_list = [ch for ch in cleaned if ch.isalpha() and ch not in vowels]

    return {
        "vowel_count": len(vowel_list),
        "consonant_count": len(consonant_list),
        "vowels_found": ", ".join(sorted(set(vowel_list)))
    }


def main():
    text = input("Enter text: ").strip()
    result = count_vowels(text)

    print(f"\n{'--- Vowel Report ---':^30}")
    print(f"{'Vowels found':<20}: {result['vowel_count']}")
    print(f"{'Consonants found':<20}: {result['consonant_count']}")
    print(f"{'Unique vowels':<20}: {result['vowels_found']}")
    
if __name__ == "__main__":
    main()