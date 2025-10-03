# 1. Создание двух множеств и вывод их пересечения и объединения
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection = set1.intersection(set2)
union = set1.union(set2)
print("Задание 1:")
print(f"Множество 1: {set1}")
print(f"Множество 2: {set2}")
print(f"Пересечение: {intersection}")
print(f"Объединение: {union}\n")


from collections import Counter
# Задание 2: Ввести текст и оставить только слова, которые встречаются ровно один раз
print("Задание 2:")
text = input("Введите слова: ")
words = text.lower().split()
# Подсчёт частоты слов
word_count = Counter(words)
# Оставляем только слова с частотой 1
unique_words = {word for word, count in word_count.items() if count == 1}
print(f"Уникальные слова (встречаются ровно один раз): {unique_words}\n")

# 3. Нахождение общих элементов двух списков с помощью множеств
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
set_list1 = set(list1)
set_list2 = set(list2)
common_elements = set_list1.intersection(set_list2)
print("Задание 3:")
print(f"Список 1: {list1}")
print(f"Список 2: {list2}")
print(f"Общие элементы: {common_elements}\n")

# 4. Проверка, является ли одно множество подмножеством другого
set_a = {1, 2, 8}
set_b = {1, 2, 3, 4, 5}
is_subset = set_a.issubset(set_b)
print("Задание 4:")
print(f"Множество A: {set_a}")
print(f"Множество B: {set_b}")
print(f"Является ли A подмножеством B: {is_subset}\n")

# 5. Удаление из множества всех элементов, которые меньше заданного числа
my_set = {1, 2, 3, 4, 5, 6, 7, 8}
print(f"Исходное множество: {my_set}")
number = int(input("Задание 5: Введите число: "))

my_set.difference_update({x for x in my_set if x < number}) #меняем на месте
print(f"Множество после удаления элементов меньше {number}: {my_set}")