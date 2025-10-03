# 1. Словарь с именами студентов и их оценками, подсчёт среднего балла
students = {
    "Петр": 87,
    "Катя": 76,
    "Иван": 43,
    "Полина": 99,
    "Лев": 63,
    "Валерия": 56,
}
average_score = sum(students.values()) / len(students)
print("Оценки студентов:", students)
print(f"Средний балл: {average_score:.2f}")

# 2. Подсчёт количества каждой буквы в строке
text = input("\nВведите строку: ")
letter_count = {}
for char in text:
    if char.isalpha():  # Учитываем только буквы
        letter_count[char] = letter_count.get(char, 0) + 1 #есть ли буква
print("Количество каждой буквы:", letter_count)

# 3. Словарь с числами от 1 до 10 и их квадратами
squares = {}
for i in range(1, 11):
    squares[i] = i ** 2
print("\nСловарь с квадратами чисел:", squares)

# 4. Словарь из двух списков
keys = ["name", "age", "city"]
values = ["Алиса", 25, "Москва"]
combined_dict = {}
for i in range(len(keys)):
    combined_dict[keys[i]] = values[i]
print("\nСловарь из двух списков:", combined_dict)