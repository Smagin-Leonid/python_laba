# 5.1) Соединение слов
def join_words():
    n = int(input("Введите количество слов: "))
    result = ""

    for i in range(n):
        word = input(f"Введите слово {i + 1}: ")
        result += word + " "

    print("Результат:", result.strip())


# 5.2) Соединение слов до слова "stop"
def join_words_until_stop():
    result = ""

    while True:
        word = input("Введите слово (или 'stop' для завершения): ")
        if word.lower() == "stop":
            break
        result += word + " "

    print("Результат:", result.strip())


# 5.3) Поиск редкой буквы
def find_rare_letter():
    word = input("Введите слово: ")

    if 'ф' in word.lower():
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")


# 5.4) Математика для детей
def math_game():
    import random

    correct_answers = 0
    mistakes = 0

    while mistakes < 3:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        correct_result = a + b

        user_answer = input(f"{a} + {b} = ")

        try:
            if int(user_answer) == correct_result:
                print("Правильно!")
                correct_answers += 1
            else:
                print("Ответ неверный")
                mistakes += 1
        except ValueError:
            print("Пожалуйста, введите число!")
            mistakes += 1

    print(f"Игра окончена. Правильных ответов: {correct_answers}")


# Запуск всех функций
if __name__ == "__main__":
    join_words()
    join_words_until_stop()
    find_rare_letter()
    math_game()