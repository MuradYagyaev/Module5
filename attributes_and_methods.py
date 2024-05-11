# Модуль №5. Классы и объекты. "Атрибуты и методы объекта."
class House:
    def __init__(self):
        self.numberOfFloors = 10


my_house = House()
for i in range(1, my_house.numberOfFloors + 1):
    print("Текущий этаж равен", i)
