
def word_frequency(sentence):
    """Counts word frequency in a sentence and returns words sorted by frequency descending."""
    words = sentence.lower().split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    sorted_by_freq = sorted(word_count.items(), key=lambda pair: pair[1], reverse=True)
    return sorted_by_freq


if __name__ == "__main__":
    sentence = input("Enter sentence: ")
    print(word_frequency(sentence))