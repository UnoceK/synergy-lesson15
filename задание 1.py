class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Autobus(Transport):
    pass  

name = input("Введите название: ")
speed = int(input("Введите максимальную скорость: "))
mile = int(input("Введите пробег: "))
autobus = Autobus(name, speed, mile)
print(f"Название автомобиля: {autobus.name} Скорость: {autobus.max_speed} Пробег: {autobus.mileage}")
