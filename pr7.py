# 7.1) Поиск числа в списке
def find_number():
    numbers = [5, 12, 8, 3, 25]
    user_number = int(input("Введите число: "))

    print(f"Исходный список: {numbers}")
    print(f"Ваше число: {user_number}")

    if user_number in numbers:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")


# 7.2) Поиск повторяющихся элементов
def find_duplicates():
    my_list = [1, 2, 3, 2, 4, 5, 3, 6, 1]
    duplicates = []

    for item in my_list:
        if my_list.count(item) > 1 and item not in duplicates:
            duplicates.append(item)

    if duplicates:
        print(f"Повторяющиеся элементы: {duplicates}")
    else:
        print("Повторяющихся элементов нет")


# 7.3) Рабочие и выходные дни
def work_weekend_days():
    days = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")

    weekend_count = int(input("Сколько выходных дней вы хотите? "))

    weekend_days = list(days[-weekend_count:])
    work_days = list(days[:-weekend_count])

    print(f"Ваши выходные дни: {', '.join(weekend_days)}")
    print(f"Ваши рабочие дни: {', '.join(work_days)}")


# 7.4) Списки студентов
def student_groups():
    # моя
    group1 = ["Белосток", "Смагин", "Бусурин", "Донгак", "Шахинахон", "Цимбал", "Пылаева", "Семёнов", "Тимофеева", "Полищук"]
    # 2-мд-20
    group2 = ["Анциферова", "Брагина", "Гусарова", "Иванова", "Игнатьева", "Каюмов", "Кондрашкин", "Кондурова", "Коомбаев", "Кравец"]

    # a. Создание команды
    team = tuple(group1[:5] + group2[:5])

    # b. Вывод списков
    print(f"Группа 1: {group1}")
    print(f"Группа 2: {group2}")
    print(f"Спортивная команда: {team}")

    # c. Длина кортежа
    print(f"Длина команды: {len(team)}")

    # d. Сортировка по алфавиту
    sorted_team = tuple(sorted(team))
    print(f"Отсортированная команда: {sorted_team}")

    # e. Поиск Иванова
    ivanov_count = team.count("Иванов")
    print(f"Студент Иванов {'входит' if ivanov_count > 0 else 'не входит'} в команду")
    print(f"Фамилия Иванов встречается {ivanov_count} раз(а)")


# Запуск всех функций
if __name__ == "__main__":
    find_number()
    find_duplicates()
    work_weekend_days()
    student_groups()