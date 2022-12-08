# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
word = word.lower()
print(word.count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = set('аоуыэеёиюя')
word = word.lower()
list_of_vowels_in_word = [
    n for n in word
    if n in vowels
]
print(len(list_of_vowels_in_word))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
print(len(words))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split()
for word in words:
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
list_of_length_words = [
    len(word)
    for word in words
]
if len(words) != 0:
    average_length_word = sum(list_of_length_words)/len(words)
else:
    print("Пустое предложение!")
print(average_length_word)