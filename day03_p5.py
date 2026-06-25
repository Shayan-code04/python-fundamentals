def word_frequency(text):
    words = text.lower().split()
    frequency = {}  
    for words in words:
        if words in frequency:
            frequency[words] += 1
        else:
            frequency[words] = 1
          
          
          
    return frequency
        
text = input("Enter a string: ")
result = word_frequency(text)
for words, count in result.items():
    print(f"{words}: {count}")       