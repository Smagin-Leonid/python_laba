import math


# 3.1) Площадь круга
def circle_area():
    r = float(input("Введите радиус круга: "))
    area = math.pi * r ** 2
    print(f"Площадь круга: {area:.2f}")


# 3.2) Решение линейного уравнения
def linear_equation():
    a = float(input("Введите коэффициент a: "))
    b = float(input("Введите коэффициент b: "))

    if a == 0:
        if b == 0:
            print("Уравнение имеет бесконечно много решений")
        else:
            print("Уравнение не имеет решений")
    else:
        x = -b / a
        print(f"Решение уравнения: x = {x:.2f}")


# 3.3) Преобразование температуры
def celsius_to_fahrenheit():
    celsius = float(input("Введите температуру в градусах Цельсия: "))
    fahrenheit = (9 / 5) * celsius + 32
    print(f"Температура по Фаренгейту: {fahrenheit:.2f}")


# 3.4) Среднее арифметическое
def average():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    num3 = float(input("Введите третье число: "))

    avg = (num1 + num2 + num3) / 3
    print(f"Среднее арифметическое: {avg:.2f}")


# 3.5) Проверка приоритета
def priority_check():
    result1 = 5 + 2 * 3 - 4 / 2  # 5 + 6 - 2 = 9
    result2 = (3 + 5) * (2 + 4) / 2  # 8 * 6 / 2 = 24
    result3 = -3 + 6 / 2 * 4  # -3 + 3 * 4 = -3 + 12 = 9
    result4 = 5 + 4 * 5 ** 2 + 7  # 5 + 4 * 25 + 7 = 5 + 100 + 7 = 112

    print(f"5 + 2 * 3 - 4 / 2 = {result1}")
    print(f"(3 + 5) * (2 + 4) / 2 = {result2}")
    print(f"-3 + 6 / 2 * 4 = {result3}")
    print(f"5 + 4 * 5 ** 2 + 7 = {result4}")


# Запуск всех функций
if __name__ == "__main__":
    circle_area()
    linear_equation()
    celsius_to_fahrenheit()
    average()
    priority_check()