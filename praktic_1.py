# Задача №1
# Создайте класс для моделирования автомобиля.
# В качестве полей задаются: марка автомобиля, модель, год выпуска, цвет, пробег (в километрах).
# состояние "запущен/остановлен" и текущая скорость. Реализовать операции: запуск двигателя, остановка двигателя,
# изменение скорости (увеличение и уменьшение), изменение цвета автомобиля, опрос состояния автомобиля
# (запущен ли двигатель), опрос текущей скорости и пробега. Операции изменения скорости должны учитывать текущую
# скорость автомобиля и не допускать превышение максимальной скорости 200 км/ч или отрицательной
# скорости. Операция вывода на экран ( ) должна аккумулировать состояние полей объекта/

class AutoModel:

    brand: str
    model: str
    year: int
    color: str
    car_mileage_km: int
    state: bool
    speed: int
    def __init__(self, brand: str, model: str, year: int, color: str, car_mileage_km: int, state: bool, speed: int):

        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.car_mileage_km = car_mileage_km
        self.state = state
        self.speed = speed

        if self.state == True:
            self.state = "заведен"

        else:
            self.state = "заглушен"
            self.speed = 0

    def __str__(self):
        return f"""Автомобиль марки: {self.brand} {self.model}. Год выпуска {self.year}, цвет {self.color}.
Пробег {self.car_mileage_km} км, состояние {self.state}. Скорость {self.speed} км/ч."""

    def starting_engine(self): #метод запуска двигателя

        print("Садимся в автомобиль. Нажимаем кнопку запуска двигателя")

        Flag = True

        while Flag:

            start = input("Нажмите s >")

            if start == "s":
                self.state = True
                Flag = False
                return f"Двигатель запущен"

            else:
                print("Неудачный запуск двигателя (жми нужную кнопку!)")

    def stop_engine(self): #метод глушения двигателя
        pass

    def change_speed(self): #метод изменения скорости
        pass

    def change_color(self): #метод изменения скорости
        pass

    def is_running_engine(self): #метод запроса -запущен ли двигатель?
        pass

    def current_speed(self): #текущая скорость?
        pass

a = AutoModel("BMW", "X600", 2020, "Белый", 107000, False, 0)

print(a)
start = a.starting_engine()
print(start)
