from typing import Hashable, Callable


class ClassNotFoundError(ValueError):
    pass


class Cookie(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def eat(self, eaten):
        self.weight = self.weight - eaten


class Cake(object):
    def __init__(self, name, weight, size):
        self.name = name
        self.weight = weight
        self.size = size
    def eat(self, eaten):
        self.weight = self.weight - (eaten * self.size)


class Bar(object):
    def __init__(self, name, weight, amount):
        self.name = name
        self.weight = weight
        self.amount = amount
    def eat(self, eaten):
        self.weight = self.weight - (eaten * self.weight / self.amount)
        self.amount = self.amount - eaten


class Chocolate(object):
    @staticmethod
    def get(class_name: Hashable) -> object:
        if not isinstance(class_name, Hashable):
            raise ValueError("Class name must be a Hashable type!")
        
        classes: dict[Hashable, Callable[..., object]] = {
            "Cookie": Cookie,
            "Cake": Cake,
            "Bar": Bar
        }

        class_ = classes.get(class_name, None)
        if class_ is not None:
            return class_

        raise ClassNotFoundError

class1_ = Chocolate.get("Cookie")

cookie = class1_("Юбилейное", 140)

print("Старый вес печенья: ", cookie.weight)

cookie.eat(30)

print("Новый вес печенья: ", cookie.weight)

class2_ = Chocolate.get("Cake")

cake = class2_("Киевский", 1600, 200)

print("Старый вес торта: ", cake.weight)

cake.eat(5)

print("Новый вес торта: ", cake.weight)

class3_ = Chocolate.get("Bar")

bar = class3_("Bounty", 90, 3)

print("Старый вес плитки: ", bar.weight)

bar.eat(1)

print("Новый вес плитка: ", bar.weight)
