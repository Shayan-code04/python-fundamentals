def count_words(sentence): 
    words = sentence.lower().split()
    word_count = {}
    
    for word in words:
        word_count[word] = word_count.get(word , 0)+1  #e done this exact line before in day04_p3.py
    
    return word_count


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    result = count_words(sentence)
    print(result)