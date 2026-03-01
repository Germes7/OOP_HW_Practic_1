# Задача №1
# Создайте класс для моделирования автомобиля.
# В качестве полей задаются: марка автомобиля, модель, год выпуска, цвет, пробег (в километрах).
# состояние "запущен/остановлен" и текущая скорость. Реализовать операции: запуск двигателя, остановка двигателя,
# изменение скорости (увеличение и уменьшение), изменение цвета автомобиля, опрос состояния автомобиля
# (запущен ли двигатель), опрос текущей скорости и пробега. Операции изменения скорости должны учитывать текущую
# скорость автомобиля и не допускать превышение максимальной скорости 200 км/ч или отрицательной
# скорости. Операция вывода на экран ( ) должна аккумулировать состояние полей объекта/

class AutoModel:
    MAX_SPEED = 200

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

        if not 0 < self.speed or self.speed < self.MAX_SPEED:
            print (f"Скорость не может быть меньше 0 или больше {self.MAX_SPEED} км/ч")

        else:
            print(f"Скорость {self.speed} введена верно")

    def __str__(self):
        return f"""Автомобиль марки: {self.brand} {self.model}. Год выпуска {self.year}, цвет {self.color}.
Пробег {self.car_mileage_km} км, состояние {self.state}. Скорость {self.speed} км/ч."""

    def starting_engine(self): #метод запуска двигателя

        print("Садимся в автомобиль. Нажимаем кнопку запуска двигателя")

        Flag = True

        while Flag:

            start = input("Нажмите s > ")

            if start == "s":
                self.state = True
                Flag = False
                return "Двигатель запущен"

            else:
                print("Неудачный запуск двигателя (жми нужную кнопку!)")

    def change_speed(self, current_speed: int): #метод изменения скорости поездки на данный момент

        if not current_speed <= self.MAX_SPEED or not current_speed > 0:
            return f"Скорость не может быть отрицательной или превышать допустимый порог в {self.MAX_SPEED} км/ч"

        else:
            self.speed = current_speed
            print(f"Поездка происходит на скорости {self.speed} км/ч")

        is_speed_info = input("""Что хотим увеличить или сбросить скорость?
Жми на селекторе "+" для увеличения. Либо "-" для сброса скорости > """)

        info = print(f"Движемся на скорости {self.speed} км/ч")

        Flag = True
        while Flag:

            if is_speed_info == "+":
                speed_plus = int(input("На сколько увеличиваем > "))

                if (self.speed + speed_plus) < 201:
                    self.speed = (speed_plus + self.speed)
                    Flag = False
                    print(f"Движемся на скорости {self.speed} км/ч")

                else:
                    print("Скорость не может превышать 200 км/ч")

            elif is_speed_info == "-":
                speed_minus = int(input("На сколько снижаем > "))

                if (self.speed - speed_minus) > 0:
                    self.speed = (self.speed - speed_minus)
                    Flag = False
                    print(info)

        return f"Опосля изменения, движемся на скорости {self.speed} км/ч"

    def stop_engine(self): #метод глушения двигателя

        info = "Двигатель заглушен"

        print("Перед выходом из автомобиля, глушим двигатель")

        Flag = True

        while Flag:

            if self.speed == 0:
                stop = input("Жмем на кнопку выключения авто s > ")

                if stop == "s":
                    self.state = False
                    Flag = False
                    return info

                else:
                    print("Опять ищи нужную кнопку")

            else:
                self.speed = 0
                self.state = False
                return info




    def change_color(self): #метод изменения цвета
        pass

    def is_running_engine(self): #метод запроса -запущен ли двигатель?
        pass

    def current_speed(self): #текущая скорость?
        pass

a = AutoModel("BMW", "X600", 2020, "Белый", 107000, False, 0)

print(a)
start = a.starting_engine()
print(start)
ch = a.change_speed(120)
print(ch)
stop = a.stop_engine()
print(stop)