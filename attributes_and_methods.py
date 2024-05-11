# Модуль №5. Классы и объекты. "Атрибуты и методы объекта."
class House:
    def __init__(self):
        self.numberOfFloors = 10

    def get_number_of_floor(self, number):
        print("Текущий этаж равен", number)

my_house = House()
# for i in range(1, my_house.numberOfFloors + 1):
#     print("Текущий этаж равен", i)

for i in range(1, my_house.numberOfFloors + 1):
    my_house.get_number_of_floor(i)
