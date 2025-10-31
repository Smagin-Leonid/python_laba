import json


# 12.1) Чтение JSON
def read_json():
    data = {
        "products": [
            {
                "name": "Шоколад",
                "price": 50,
                "available": True,
                "weight": 100
            },
            {
                "name": "Кофе",
                "price": 100,
                "available": False,
                "weight": 250
            },
            {
                "name": "Чай",
                "price": 70,
                "available": True,
                "weight": 50
            }
        ]
    }

    # Сохраняем данные в файл
    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Читаем и выводим
    with open('products.json', 'r', encoding='utf-8') as f:
        products_data = json.load(f)

    for product in products_data['products']:
        print(f"Название: {product['name']}")
        print(f"Цена: {product['price']}")
        print(f"Вес: {product['weight']}")
        print("В наличии" if product['available'] else "Нет в наличии!")
        print()


# 12.2) Добавление данных в JSON
def add_to_json():
    try:
        # Читаем существующие данные
        with open('products.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Добавляем новый продукт
        new_product = {
            "name": input("Введите название продукта: "),
            "price": int(input("Введите цену: ")),
            "available": input("Есть в наличии? (да/нет): ").lower() == "да",
            "weight": int(input("Введите вес: "))
        }

        data['products'].append(new_product)

        # Сохраняем обновленные данные
        with open('products.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print("\nОбновленный список продуктов:")
        for product in data['products']:
            print(f"Название: {product['name']}")
            print(f"Цена: {product['price']}")
            print(f"Вес: {product['weight']}")
            print("В наличии" if product['available'] else "Нет в наличии!")
            print()

    except Exception as e:
        print(f"Ошибка: {e}")


# 12.3) Русско-английский словарь
def create_ru_en_dict():
    # Создаем тестовый файл
    with open('en-ru.txt', 'w', encoding='utf-8') as f:
        f.write("""cat - кошка
dog - собака
home - домашняя папка, дом
mouse - мышь, манипулятор мышь
to do - делать, изготавливать
to make - изготавливать""")

    # Читаем англо-русский словарь
    en_ru_dict = {}
    with open('en-ru.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if ' - ' in line:
                en_word, ru_translations = line.split(' - ')
                ru_words = [word.strip() for word in ru_translations.split(',')]
                en_ru_dict[en_word] = ru_words

    # Создаем русско-английский словарь
    ru_en_dict = {}
    for en_word, ru_words in en_ru_dict.items():
        for ru_word in ru_words:
            if ru_word in ru_en_dict:
                ru_en_dict[ru_word].append(en_word)
            else:
                ru_en_dict[ru_word] = [en_word]

    # Записываем отсортированный словарь
    with open('ru-en.txt', 'w', encoding='utf-8') as f:
        for ru_word in sorted(ru_en_dict.keys()):
            en_words = ', '.join(sorted(set(ru_en_dict[ru_word])))
            f.write(f"{ru_word} - {en_words}\n")

    print("Русско-английский словарь создан!")


# Запуск функций
if __name__ == "__main__":
    read_json()
    add_to_json()
    create_ru_en_dict()