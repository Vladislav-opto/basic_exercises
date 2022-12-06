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
counter = 0
for letter in word:
    if letter in vowels:
        counter += 1
print (counter)


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
summ = 0
for word in words:
    summ += len(word)
if summ != 0:
    average = summ / len(words)
    print(average)
else:
    print("Пустое предложение!")