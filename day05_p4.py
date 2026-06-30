def sentence_difference():
    """Find words that appear in the first sentence but not in the second."""

    sentence1 = input("Enter the first sentence: ")
    sentence2 = input("Enter the second sentence: ")

    words1 = set(sentence1.lower().split())
    words2 = set(sentence2.lower().split())

    difference = words1 - words2

    print("\nWords only in the first sentence:")
    print(difference)


sentence_difference()