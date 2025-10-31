# 6.1) Проверка делимости на 3
def divisible_by_three(number):
    return number % 3 == 0


# 6.2) Безопасное деление
def safe_divide():
    try:
        num = input("Введите число для деления 100: ")
        divisor = float(num)
        result = 100 / divisor
        print(f"Результат: {result}")
    except ValueError:
        print("Ошибка: введено не число!")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")


# 6.3) Магическая дата
def is_magic_date(date_str):
    try:
        day, month, year = map(int, date_str.split('.'))
        last_two_digits = year % 100
        return day * month == last_two_digits
    except:
        return False


# 6.4) Счастливый билет
def is_lucky_ticket(ticket_number):
    if len(ticket_number) % 2 != 0:
        return False

    half = len(ticket_number) // 2
    first_half = sum(int(digit) for digit in ticket_number[:half])
    second_half = sum(int(digit) for digit in ticket_number[half:])

    return first_half == second_half


# Тестирование функций
if __name__ == "__main__":
    # 6.1
    num = int(input("Введите число для проверки делимости на 3: "))
    print(f"Число {num} {'делится' if divisible_by_three(num) else 'не делится'} на 3")

    # 6.2
    safe_divide()

    # 6.3
    date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
    print(f"Дата {'магическая' if is_magic_date(date) else 'не магическая'}")

    # 6.4
    ticket = input("Введите номер билета: ")
    print(f"Билет {'счастливый' if is_lucky_ticket(ticket) else 'несчастливый'}")