# Общий класс
class Flower:
    def __init__(self, name, color, stem_length, price, life_time):
        self.name = name
        self.color = color
        self.stem_length = stem_length  # длина стебля
        self.price = price
        self.life_time = life_time  # срок жизни

    def __str__(self):
        return (
            f"{self.name}, {self.color}, {self.stem_length}см, "
            f"{self.price}руб, живет {self.life_time} дн."
        )


# Подклассы для конкретных цветов
class Rose(Flower):
    def __init__(self, name, color, stem_length, price, life_time):
        super().__init__(name, color, stem_length, price, life_time)


class Tulip(Flower):
    def __init__(self, name, color, stem_length, price, life_time):
        super().__init__(name, color, stem_length, price, life_time)


class Romashka(Flower):
    def __init__(self, name, color, stem_length, price, life_time):
        super().__init__(name, color, stem_length, price, life_time)


# Класс для букета
class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def total_price(self):
        sum(map(lambda x: x.price, self.flowers))

    def average_life_time(self):
        return sum(i.life_time for i in self.flowers) / len(self.flowers)

    def sort_by(self, key):
        self.flowers.sort(key=lambda x: getattr(x, key))

    def find_by_life_time(self, min_days):
        return [i for i in self.flowers if i.life_time >= min_days]

    def __str__(self):
        return "\n".join(str(i) for i in self.flowers)
    

# Экземпляры (объекты) цветов разных видов.
rose = Rose("Роза", "белая", 50, 350, 8)
tulip = Tulip("Тюльпан", "желтый", 35, 150, 6)
chamomile = Romashka("Ромашка", "белая", 30, 100, 3)

bouquet = Bouquet([rose, rose, rose, rose, rose, tulip, tulip, chamomile, chamomile])

print("Букет состоит из:")
print(bouquet)

print("\nСтоимость букета:", bouquet.total_price(), "P")
print("Время жизни букета:", round(bouquet.average_life_time()), "дн.")

bouquet.sort_by("price")
print("\nСортировка по цене:")
print(bouquet)

found = bouquet.find_by_life_time(4)
print("\nЦветы простоят 4+  дней:")
for f in found:
    print(f)
