# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:                                     Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам    Парам пам-пам
def count_vowels(word):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

def check_rhythm(poem):
    phrases = poem.split()
    vowel_counts = []
    for phrase in phrases:
        words = phrase.split('-')
        phrase_vowel_count = sum(count_vowels(word) for word in words)
        vowel_counts.append(phrase_vowel_count)
    
    if len(set(vowel_counts)) == 1:
        return 'Парам пам-пам'
    else:
        return 'Пам парам'

# Пример использования:
poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)