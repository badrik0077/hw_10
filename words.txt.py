class Box:
    def __init__(self, size, weight, contains):
        self.size = size
        self.weight = weight
        self.contains = contains


def observe(self):
    return (f'Это похоже на ящик размером {self.size} и весом {self.weight}кг')


class Container(Box):
    def open(self):
        return (f"В ящике размером {self.size} и весом {self.weight}кг оказалось {self.contains} кг апельсин"}


box_1 = Box('30x30', '1', '15 золотых монет')

container_1 = Container('50x30', '2', '7 золотых монет')
1




