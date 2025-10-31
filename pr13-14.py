# 13.1-13.3) Класс Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, initial_rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = initial_rating

    def describe_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}'")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")

    def open_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг обновлен: {self.rating}")


# 14.1-14.2) Класс IceCreamStand
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, location="", working_hours="", initial_rating=0):
        super().__init__(restaurant_name, cuisine_type, initial_rating)
        self.flavors = flavors
        self.location = location
        self.working_hours = working_hours
        self.ice_cream_types = {
            "на палочке": [],
            "мягкое": [],
            "фруктовое": []
        }

    def show_flavors(self):
        print("Доступные вкусы мороженого:")
        for flavor in self.flavors:
            print(f"- {flavor}")

    def add_flavor(self, flavor):
        if flavor not in self.flavors:
            self.flavors.append(flavor)
            print(f"Вкус '{flavor}' добавлен")
        else:
            print(f"Вкус '{flavor}' уже есть в списке")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Вкус '{flavor}' удален")
        else:
            print(f"Вкус '{flavor}' не найден")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"Вкус '{flavor}' доступен")
            return True
        else:
            print(f"Вкус '{flavor}' недоступен")
            return False

    def add_ice_cream_type(self, ice_type, flavors):
        if ice_type in self.ice_cream_types:
            self.ice_cream_types[ice_type].extend(flavors)
            print(f"Добавлены вкусы для типа '{ice_type}': {flavors}")
        else:
            print(f"Тип мороженого '{ice_type}' не поддерживается")

    def show_ice_cream_types(self):
        print("Типы мороженого и их вкусы:")
        for ice_type, flavors in self.ice_cream_types.items():
            if flavors:
                print(f"{ice_type}: {', '.join(flavors)}")


# Тестирование классов
if __name__ == "__main__":
    # 13.1
    print("=== Задание 13.1 ===")
    new_restaurant = Restaurant("Вкусно и точка", "Фастфуд", 4.2)
    print(new_restaurant.restaurant_name)
    print(new_restaurant.cuisine_type)
    new_restaurant.describe_restaurant()
    new_restaurant.open_restaurant()

    # 13.2
    print("\n=== Задание 13.2 ===")
    restaurant1 = Restaurant("У Франсуа", "Французская", 4.8)
    restaurant2 = Restaurant("Токио Сити", "Японская", 4.5)
    restaurant3 = Restaurant("Мама Рома", "Итальянская", 4.7)

    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

    # 13.3
    print("\n=== Задание 13.3 ===")
    new_restaurant.update_rating(4.5)

    # 14.1-14.2
    print("\n=== Задание 14.1-14.2 ===")
    ice_cream_stand = IceCreamStand(
        "Мороженка",
        "Кафе-мороженое",
        ["ванильное", "шоколадное", "клубничное"],
        "ТЦ 'Галерея'",
        "10:00-22:00"
    )

    ice_cream_stand.describe_restaurant()
    ice_cream_stand.show_flavors()

    ice_cream_stand.add_flavor("фисташковое")
    ice_cream_stand.remove_flavor("клубничное")
    ice_cream_stand.check_flavor("ванильное")

    ice_cream_stand.add_ice_cream_type("на палочке", ["эскимо", "фруктовый лед"])
    ice_cream_stand.add_ice_cream_type("мягкое", ["ванильное", "шоколадное"])
    ice_cream_stand.show_ice_cream_types()