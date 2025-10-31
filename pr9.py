from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os
from pathlib import Path


# 9.1) Информация об изображении
def image_info():
    try:
        image_path = input("Введите путь к изображению: ")
        with Image.open(image_path) as img:
            print(f"Размер: {img.size}")
            print(f"Формат: {img.format}")
            print(f"Цветовая модель: {img.mode}")

            # Показать изображение
            img.show()
    except Exception as e:
        print(f"Ошибка: {e}")


# 9.2) Обработка изображения
def process_image():
    try:
        image_path = "test_file.jpg"
        with Image.open(image_path) as img:
            # Уменьшение в 3 раза
            small_img = img.resize((img.width // 3, img.height // 3))
            small_img.save("small_image.jpg")

            # Горизонтальное отражение
            h_mirror = img.transpose(Image.FLIP_LEFT_RIGHT)
            h_mirror.save("horizontal_mirror.jpg")

            # Вертикальное отражение
            v_mirror = img.transpose(Image.FLIP_TOP_BOTTOM)
            v_mirror.save("vertical_mirror.jpg")

            print("Изображения сохранены!")
    except Exception as e:
        print(f"Ошибка: {e}")


# 9.3) Применение фильтра к нескольким изображениям
def batch_process():
    try:
        input_folder = "files"
        output_folder = "processed_images"

        # Создаем папку для результатов
        Path(output_folder).mkdir(exist_ok=True)

        for i in range(1, 6):
            filename = f"{i}.jpg"
            input_path = os.path.join(input_folder, filename)

            if os.path.exists(input_path):
                with Image.open(input_path) as img:
                    # Применяем фильтр контура
                    processed = img.filter(ImageFilter.CONTOUR)
                    output_path = os.path.join(output_folder, f"processed_{i}.jpg")
                    processed.save(output_path)
                    print(f"Обработано: {filename}")
            else:
                print(f"Файл {filename} не найден")
    except Exception as e:
        print(f"Ошибка: {e}")


# 9.4) Водяной знак
def add_watermark():
    try:
        image_path = "watermark/test_file.jpg"
        with Image.open(image_path) as img:
            # Создаем копию для рисования
            watermarked = img.copy()
            draw = ImageDraw.Draw(watermarked)

            try:
                font = ImageFont.truetype("arial.ttf", 36)
            except:
                font = ImageFont.load_default()

            # Добавляем текст
            text = "Watermark"
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            # Позиция в правом нижнем углу
            position = (img.width - text_width - 10, img.height - text_height - 10)

            draw.text(position, text, font=font, fill=(255, 255, 255, 128))

            watermarked.save("watermarked_image.jpg")
            print("Изображение с водяным знаком сохранено!")
    except Exception as e:
        print(f"Ошибка: {e}")


# 11.3) Работа с CSV
import csv


def process_csv():
    total_sum = 0
    products = []

    try:
        # Читаем данные из CSV файла
        with open('products.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Пропускаем заголовок

            for row in reader:
                product, quantity, price = row
                quantity = int(quantity)
                price = int(price)
                total = quantity * price
                total_sum += total
                products.append((product, quantity, price, total))

        # Выводим результат
        print("Нужно купить:")
        for product, quantity, price, total in products:
            print(f"{product} - {quantity} шт. за {price} руб.")

        print(f"Итоговая сумма: {total_sum} руб.")

    except FileNotFoundError:
        print("Файл products.csv не найден!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Запуск функций
if __name__ == "__main__":
    # image_info()
    # process_image()
    # batch_process()
    # add_watermark()
    process_csv()