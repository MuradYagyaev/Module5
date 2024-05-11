# Модуль №5. Классы и объекты. "Атрибуты и методы объекта."
class House:
    def __init__(self):
        self.numberOfFloors = 10
        self.current_floor = 1

    def get_number_of_floor(self, number):
        print("Текущий этаж равен", number)

    def go_up_next_floor(self):
        if self.current_floor < self.numberOfFloors:
            self.current_floor += 1
            self.get_number_of_floor(self.current_floor)
        else:
            print("Мы на послденем этаже")

    def go_down_next_floor(self):
        if self.current_floor > 1:
            self.current_floor -= 1
            self.get_number_of_floor(self.current_floor)
        else:
            print("Мы на первом этаже")


my_house = House()

# for i in range(1, my_house.numberOfFloors + 1):
#     print("Текущий этаж равен", i)

print("Поднимаемся по этажам вверх")
my_house.get_number_of_floor(my_house.current_floor)
while my_house.current_floor < my_house.numberOfFloors:
    my_house.go_up_next_floor()

print("А теперь спускаемся вниз")
while my_house.current_floor > 1:
    my_house.go_down_next_floor()
