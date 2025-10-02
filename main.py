print('Hello, GitHub!')
# 1. Таблица умножения от 1 до 9
print("Таблица умножения:")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:3}", end="\t")
    print()

# 2. Сумма нечётных чисел от 1 до 100
odd_sum = 0
for i in range(1, 101, 2):
    odd_sum += i
print(f"\nСумма нечётных чисел от 1 до 100: {odd_sum}")

# 3. Делители числа
n = int(input("\nВведите число для нахождения делителей: "))
print(f"Делители числа {n}:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
print()

# 4. Факториал числа
n = int(input("\nВведите число для вычисления факториала: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Факториал числа {n}: {factorial}")

# 5. Последовательность Фибоначчи
n = int(input("\nВведите длину последовательности Фибоначчи: "))
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
print(f"Последовательность Фибоначчи длиной {n}:")
print(fib[:n])