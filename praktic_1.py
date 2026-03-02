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
            return f"Поездка происходит на скорости {self.speed} км/ч"

    def accelerate(self): #метод увеличения скорости

        print(f"Движемся на скорости {self.speed} км/ч")

        Flag = True
        while Flag:

            is_speed_info_1 = input("Хотим увеличить скорость. Жми на селекторе + для увеличения > ")

            if is_speed_info_1 == "+":

                Flag_2 = True
                while Flag_2:

                    speed_plus = int(input("На сколько увеличиваем > "))

                    if (self.speed + speed_plus) <= self.MAX_SPEED:
                        self.speed = (speed_plus + self.speed)
                        Flag_2 = False
                        return f"Скорость увеличили до {self.speed} км/ч"

                    else:
                        print("Скорость не может превышать 200 км/ч")

                Flag = False

            else:
                print("Жми '+' баран")

    def decelerate(self): #метод сброса скорости

        print(f"Продолжаем движение на скорости {self.speed} км/ч")

        Flag = True
        while Flag:

            is_speed_info_2 = input("Хотим сбросить скорость. Жми на селекторе - для уменьшения > ")

            if is_speed_info_2 == "-":

                Flag_2 = True
                while Flag_2:

                    speed_minus = int(input("На сколько снижаем > "))

                    if (self.speed - speed_minus) > 0:
                        self.speed = (self.speed - speed_minus)
                        Flag_2 = False
                        return f"Скорость уменьшили до {self.speed} км/ч"

                    else:
                        print("Скорость не может быть меньше нуля")

                Flag = False

            else:
                print("Жми '-' баран")

    def stop_engine(self): #метод глушения двигателя

        print("Начинаем снижать скорость ....")
        if self.speed > 0:

            import time # про данный метод, вспомнил Ваши уроки по строкам. Не зря учили!
            for i in range(self.speed, 0, -10):
                time.sleep(0.65)
                print(f"\r{i} км/ч", end="")

            print(f"\r0 км/ч", end="")  # каюсь, как сделать вывод спидометра на ноль, подсмотрел в паутине
            time.sleep(1.0)  # Небольшая пауза, чтобы увидеть 0
            print()

            self.speed = 0

        else:
            print("Автомобиль уже стоит.")

        Flag = True

        while Flag:

            if self.speed == 0:
                stop = input("Жмем на кнопку выключения авто s > ")

                if stop == "s":
                    self.state = False
                    Flag = False
                    return "Двигатель заглушен"

                else:
                    print("Опять ищи нужную кнопку")

            else:
                self.state = False

    def is_change_color(self): #метод изменения цвета

        Flag =True

        while Flag:

            colors = input("Хотим перекрасить автомобиль? Да: нажмите 'y', Нет: нажмите 'n' > ")

            if colors == "y":

                new_color = input("В какой цвет > ")

                if new_color.lower() != self.color.lower():

                    self.color = new_color
                    Flag = False
                    return f"Автомобиль перекрашен в цвет {new_color}"

                else:
                    return f"Автомобиль уже в этом цвете {self.color}"

            elif colors == "n":
                Flag = False
                return f"Автомобиль остался в прежнем цвете {self.color}"

            else:
                print("Ищем нужную кнопку на клаве")

    def is_running_engine(self): #метод запроса -запущен ли двигатель?

        if self.state == False:
            return "Двигатель заглушен"

        else:
            return "Двигатель работает"


a = AutoModel("BMW", "X600", 2020, "Белый", 107000, False, 0)

print(a)
start = a.starting_engine()
print(start)
ch = a.change_speed(195)
print(ch)
ac = a.accelerate()
print(ac)
dc = a.decelerate()
print(dc)
stop = a.stop_engine()
print(stop)
color = a.is_change_color()
print(color)
run = a.is_running_engine()
print(run)