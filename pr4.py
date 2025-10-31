# 4.1) Проверка пароля
def check_password():
    password1 = input("Введите пароль: ")
    password2 = input("Подтвердите пароль: ")

    if password1 == password2:
        print("Пароль принят")
    else:
        print("Пароль не принят")


# 4.2) Определение места в плацкартном вагоне
def train_seat():
    seat = int(input("Введите номер места (1-54): "))

    if seat < 1 or seat > 54:
        print("Неверный номер места")
    elif seat % 2 == 0:
        if seat <= 36:
            print("Верхнее место в купе")
        else:
            print("Верхнее боковое место")
    else:
        if seat <= 35:
            print("Нижнее место в купе")
        else:
            print("Нижнее боковое место")


# 4.3) Високосный год
def leap_year():
    year = int(input("Введите год: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"Год {year} - високосный")
    else:
        print("Это год не високосный")


# 4.4) Смешивание цветов
def mix_colors():
    color1 = input("Введите первый основной цвет: ").lower()
    color2 = input("Введите второй основной цвет: ").lower()

    primary_colors = ["красный", "синий", "желтый"]

    if color1 not in primary_colors or color2 not in primary_colors:
        print("Ошибка: введен не основной цвет")
        return

    if color1 == color2:
        print(f"Получился {color1} цвет")
    elif ("красный" in [color1, color2]) and ("синий" in [color1, color2]):
        print("Получился фиолетовый цвет")
    elif ("красный" in [color1, color2]) and ("желтый" in [color1, color2]):
        print("Получился оранжевый цвет")
    elif ("синий" in [color1, color2]) and ("желтый" in [color1, color2]):
        print("Получился зеленый цвет")


# Запуск всех функций
if __name__ == "__main__":
    check_password()
    train_seat()
    leap_year()
    mix_colors()