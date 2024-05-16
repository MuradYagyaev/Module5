# Модуль №5. Классы и объекты. "Различие атрибутов класса и экземпляра."

class Building:
    """ Здание """
    total = 0

    def __init__(self, floors=9, btype="панельный"):
        Building.total += 1
        self.numberOfFloors = floors
        self.buildingType = btype

    def __str__(self):
        return 'Building: number of floors ' + str(self.numberOfFloors) + ', type ' + self.buildingType


for i in range(40):
    new_house = Building()
    # print(new_house)
# new_house = Building(17, 'монолитный')
# print(new_house)
print("Всего домов:", Building.total)
