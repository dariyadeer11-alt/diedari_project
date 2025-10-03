import random

# Создаём список из 10 случайных чисел
numbers = [random.randint(-50, 50) for _ in range(10)]
print("Исходный список:", numbers)

# 1. Вывод чётных элементов
print("\nЧётные элементы списка:")
for num in numbers:
    if num % 2 == 0:
        print(num, end=" ")
print()

# 2. Нахождение максимального и минимального числа
max_num = numbers[0]
min_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
print(f"\nМаксимальное число: {max_num}")
print(f"Минимальное число: {min_num}")

# 3. Запрос 5 чисел у пользователя, сохранение и сортировка
user_numbers = []
for i in range(5):
    num = int(input("\nВведите число для сортировки: "))
    user_numbers.append(num)
user_numbers.sort()
print("Отсортированный список:", user_numbers)

# 4. Удаление дубликатов без использования множеств
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("\nСписок без дубликатов:", unique_numbers)
print("Исходный список:", numbers)

# 5. Поменять местами первый и последний элемент
if numbers:  # Проверка, что список не пустой
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
print("\nСписок после обмена первого и последнего элементов:", numbers)