sen=input("Enter sentence: ").lower().split()
sorted_words = sorted(sen, key=lambda x: x.lower(),reverse=True)
word_count = {}
for word in sen:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)   