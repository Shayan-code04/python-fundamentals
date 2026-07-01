# day06_p4.py

def get_text_statistics(text):
    """
    Generates statistics for a given block of text.

    Args:
        text (str): Input text from user.
    Returns:
        dict: Statistics including word count, char count, sentence count, etc.
    """
    cleaned = text.strip()
    words = cleaned.split()
    word_count = len(words)
    char_count_with_spaces = len(cleaned)
    char_count_no_spaces = len(cleaned.replace(" ", ""))
    sentence_count = cleaned.count(".") + cleaned.count("!") + cleaned.count("?")
    unique_words = len(set(word.lower().strip(".,!?") for word in words))
    avg_word_length = round(sum(len(w.strip(".,!?")) for w in words) / word_count, 2) if word_count > 0 else 0

    return {
        "words": word_count,
        "chars_with_spaces": char_count_with_spaces,
        "chars_no_spaces": char_count_no_spaces,
        "sentences": sentence_count,
        "unique_words": unique_words,
        "avg_word_length": avg_word_length
    }


def print_report(stats):
    """
    Prints formatted text statistics report.

    Args:
        stats (dict): Statistics dictionary from get_text_statistics.
    Returns:
        None
    """
    print(f"\n{'=' * 35}")
    print(f"{'TEXT STATISTICS REPORT':^35}")
    print(f"{'=' * 35}")
    print(f"{'Word count':<25}: {stats['words']:>5}")
    print(f"{'Chars (with spaces)':<25}: {stats['chars_with_spaces']:>5}")
    print(f"{'Chars (no spaces)':<25}: {stats['chars_no_spaces']:>5}")
    print(f"{'Sentence count':<25}: {stats['sentences']:>5}")
    print(f"{'Unique words':<25}: {stats['unique_words']:>5}")
    print(f"{'Avg word length':<25}: {stats['avg_word_length']:>5}")
    print(f"{'=' * 35}")


def main():
    print("Enter your text (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    text = " ".join(lines)
    if not text.strip():
        print("No text entered.")
        return

    stats = get_text_statistics(text)
    print_report(stats)


if __name__ == "__main__":
    main()
    