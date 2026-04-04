class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Autobus(Transport):
    def Print(self):
        print(f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}")


name = input("Введите название: ")
speed = int(input("Введите максимальную скорость: "))
mile = int(input("Введите пробег: "))
autobus = Autobus(name,speed,mile)
autobus.max_speed = speed
autobus.name = name
autobus.mileage = mile
autobus.Print()

