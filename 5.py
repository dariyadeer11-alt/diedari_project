import random

# 1. Сгенерировать список из 20 случайных чисел и вывести только уникальные значения
print("Задание 1:")
random_list = [random.randint(1, 50) for _ in range(20)]
print(f"Исходный список: {random_list}")
unique_values = list(set(random_list)) #для списка
print(f"Уникальные значения: {unique_values}\n")

# 2. Создать словарь, где ключи – это элементы списка, а значения – количество их повторений
print("Задание 2:")
chastota_dict = {}
for item in random_list:
    chastota_dict[item] = chastota_dict.get(item, 0) + 1
print(f"Словарь частот: {chastota_dict}\n")

# 3. Дан список слов. Создать множество из слов, длина которых больше 5 символов
print("Задание 3:")
words_list = ["python", "hello", "world", "programming", "code", "developer", "short", "longword"]
long_words = {word for word in words_list if len(word) > 5}
print(f"Исходный список слов: {words_list}")
print(f"Слова длиной > 5: {long_words}\n")

# 4. Ввести предложение. Сохранить в словарь количество вхождений каждого слова
print("Задание 4:")
sentence = input("Введите предложение: ")
words = sentence.lower().split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(f"Словарь вхождений: {word_count}\n")

# 5. Создать список чисел, преобразовать его в множество и обратно в список (убрав дубликаты)
print("Задание 5:")
numbers_list = [1, 2, 2, 3, 4, 4, 5]
print(f"Исходный список: {numbers_list}")
unique_list = list(set(numbers_list))
print(f"Список без дубликатов: {unique_list}\n")

# 6. Дан словарь "товар – цена". Найти самый дорогой товар
print("Задание 6:")
products = {"яблоко": 50, "банан": 30, "апельсин": 70, "груша": 60}
most_expensive = max(products, key=products.get)
print(f"Словарь товаров: {products}")
print(f"Самый дорогой товар: {most_expensive} (цена: {products[most_expensive]})\n")

# 7. Дан список имён. Определить, какие из имён встречаются более одного раза. Какое имя встречается чаще всего
print("Задание 7:")
names_list = ["Алексей", "Мария", "Алексей", "Иван", "Мария", "Мария", "Петр"]
name_count = {}
# Подсчёт количества вхождений каждого имени
for name in names_list:
    name_count[name] = name_count.get(name, 0) + 1
# Нахождение имён, которые встречаются более одного раза
duplicates = {name: count for name, count in name_count.items() if count > 1}
# Нахождение имени с максимальным количеством вхождений
most_common = None
max_count = 0
for name, count in name_count.items():
    if count > max_count:
        most_common = name
        max_count = count
print(f"Список имен: {names_list}")
print(f"Имена, встречающиеся более одного раза: {duplicates}")
print(f"Имя, встречающееся чаще всего: {most_common}\n")

# 8. Запросить у пользователя строку и составить словарь: символ → индекс его первого вхождения
text = input("\nВведите строку: ")
char_indices = {char: text.index(char) for char in text}
print("Словарь символов и их первых вхождений:", char_indices)