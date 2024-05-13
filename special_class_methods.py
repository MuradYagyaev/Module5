# Модуль №5. Классы и объекты. "Специальные методы классов"

class House:
    def __init__(self):
        self.numberOfFloors = 0

    def getNumberOfFloors(self):
        print(f"numberOfFloors = {self.numberOfFloors}")

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        # print(f"numberOfFloors = {self.numberOfFloors}")
        self.getNumberOfFloors()

    def __del__(self):
        pass


my_house = House()

my_house.getNumberOfFloors()
my_house.setNewNumberOfFloors(5)
my_house.setNewNumberOfFloors(7)
