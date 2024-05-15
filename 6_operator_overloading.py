# Модуль №5. Классы и объекты. Перегрузка операторов

class Building:
    def __init__(self, floors, btype):
        self.numberOfFloors = floors
        self.buildingType = btype

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


my_house = Building(9, "панельный")
friend_house = Building(9, "панельный")
father_house = Building(1, "кирпичный")

if my_house == friend_house:
    print("Эти дома одинаковые")
else:
    print("Эти дома разные")

if my_house == father_house:
    print("Эти дома одинаковые")
else:
    print("Эти дома разные")
