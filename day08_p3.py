def count_word_frequency(filepath):
    """
    Count how many times each word appears in a text file.

    Parameters:
        filepath (str): path to the .txt file to analyze.

    Returns:
        dict: mapping of word (lowercase, punctuation-stripped) to count.
    """
    frequency = {}
    with open(filepath, "r") as f:
        for line in f:
            words = line.strip().split()
            for word in words:
                cleaned = word.strip(".,!?;:\"'()").lower()
                if cleaned:
                    frequency[cleaned] = frequency.get(cleaned, 0) + 1
    return frequency


def top_n_words(frequency, n=5):
    """
    Return the top N most frequent words.

    Parameters:
        frequency (dict): word-to-count mapping.
        n (int): number of top words to return.

    Returns:
        list of tuple: (word, count), sorted by count descending.
    """
    return sorted(frequency.items(), key=lambda item: item[1], reverse=True)[:n]


def print_top_words(top_words):
    """
    Print top words with their counts.

    Parameters:
        top_words (list of tuple): (word, count) pairs.
    """
    for word, count in top_words:
        print(f"{word}: {count}")


if __name__ == "__main__":
    filepath = "sample.txt"

    # create a sample file for testing
    with open(filepath, "w") as f:
        f.write("the quick brown fox jumps over the lazy dog. The dog barks.\n")

    freq = count_word_frequency(filepath)
    top = top_n_words(freq, n=5)
    print_top_words(top)