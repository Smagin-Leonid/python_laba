# 8.1) Словарь стран
def countries_dict():
    countries = {
        "Россия": "Москва",
        "Франция": "Париж",
        "Германия": "Берлин",
        "Италия": "Рим",
        "Испания": "Мадрид",
        "Великобритания": "Лондон",
        "Япония": "Токио",
        "Китай": "Пекин",
        "США": "Вашингтон",
        "Канада": "Оттава"
    }

    # a. Все пары ключ-значение
    print("Все страны и столицы:")
    for country, capital in countries.items():
        print(f"{country} - {capital}")

    # b. Столица определенной страны
    country = input("\nВведите название страны: ")
    if country in countries:
        print(f"Столица {country}: {countries[country]}")
    else:
        print("Такой страны нет в словаре")

    # c. Сортировка по алфавиту
    print("\nОтсортированный словарь:")
    for country in sorted(countries.keys()):
        print(f"{country} - {countries[country]}")


# 8.2) Игра Эрудит
def scrabble_score():
    scores = {
        1: ['а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т'],
        2: ['д', 'к', 'л', 'м', 'п', 'у'],
        3: ['б', 'г', 'ё', 'ь', 'я'],
        4: ['й', 'ы'],
        5: ['ж', 'з', 'х', 'ц', 'ч'],
        8: ['ш', 'э', 'ю'],
        10: ['ф', 'щ', 'ъ']
    }

    # Создаем обратный словарь для быстрого поиска
    letter_scores = {}
    for score, letters in scores.items():
        for letter in letters:
            letter_scores[letter] = score

    word = input("Введите слово: ").lower()
    total_score = 0

    for letter in word:
        if letter in letter_scores:
            total_score += letter_scores[letter]
        else:
            print(f"Буква '{letter}' не найдена в системе подсчета очков")

    print(f"Стоимость слова '{word}': {total_score} очков")


# 8.3) Языки студентов
def student_languages():
    students = {
        "Белосток": ["английский", "французский", "китайский"],
        "Смагин": ["английский", "немецкий"],
        "Бусурин": ["испанский", "китайский", "японский"],
        "Донгак": ["английский", "китайский"],
        "Шахинахон": ["французский", "итальянский"]
    }

    # Все уникальные языки
    all_languages = set()
    for languages in students.values():
        all_languages.update(languages)

    print("Все языки, которые знают студенты:")
    for lang in sorted(all_languages):
        print(f"- {lang}")

    # Студенты, знающие китайский
    chinese_speakers = [name for name, langs in students.items() if "китайский" in langs]
    print(f"\nСтуденты, знающие китайский: {', '.join(chinese_speakers)}")


# Запуск всех функций
if __name__ == "__main__":
    countries_dict()
    scrabble_score()
    student_languages()