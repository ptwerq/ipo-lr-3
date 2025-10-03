# Запрашиваем у пользователя два числа
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

# Используем тернарное выражение
result = num1 if num1 < num2 else (num2 if num2 < num1 else None)

# Вывод результата
if result is None:
    print("Числа равны!")
else:
    print(f"Наименьшее число: {result}")