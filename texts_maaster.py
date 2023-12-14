text = input("Введите текст: ")
text = text.lower()

punctuation = [".", ",", "!", "?", ";", ':']
for symb in punctuation:
    text = text.replace(symb, "")

# список слов из строки
words = text.split()

longest_word = words[0]

word_frequency = {}
for word in words:
    if word in word_frequency:
       word_frequency[word] += 1 
    else:
        word_frequency[word] = 1
    if len(word) > len(longest_word):
        longest_word = word



# print(words)




print("Количество разных слов:", len(set(words)))

print("Частота слов:")
for k, v in word_frequency.items():
    print(f'{k}: {v}')