from __future__ import annotations

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

        if self.speed > AutoModel.MAX_SPEED or self.speed < 0:
            raise ValueError("Скорость не должна превышать 200 км/ч либо быть отрицательной")

    def __str__(self):

        return f"""Автомобиль марки: {self.brand} {self.model}. Год выпуска {self.year}, цвет {self.color}.
Пробег {self.car_mileage_km} км, состояние {self.state}. Скорость {self.speed} км/ч."""

    def starting_engine(self):  # метод запуска двигателя

        if self.state == False:
            self.state = True
            return "Двигатель запущен"

        return "Двигатель уже запущен"

    def change_speed(self, current_speed: int):  # метод изменения скорости поездки на данный момент

        if not current_speed <= AutoModel.MAX_SPEED or not current_speed > 0:
            raise ValueError(
                f"Скорость не может быть отрицательной или превышать допустимый порог в {AutoModel.MAX_SPEED} км/ч")

        self.speed = current_speed
        return f"Скорость составляет {self.speed} км/ч"

    def accelerate(self, new_speed: int):  # метод изменения скорости

        if new_speed > (AutoModel.MAX_SPEED - self.speed) or abs(new_speed) > self.speed:
            raise ValueError(
                f"Скорость не может быть отрицательной или превышать допустимый порог в {AutoModel.MAX_SPEED} км/ч")

        self.speed += new_speed
        return f"Скорость изменилась. Составляет {self.speed}"

    def stop_engine(self):  # метод глушения двигателя

        if self.state == True:
            self.state = False
            return "Двигатель заглушен"

        return "Двигатель был заглушен"

    def is_change_color(self, new_color: str):  # метод изменения цвета

        if new_color.lower() != self.color.lower():
            self.color = new_color
            return f"Авто перекрашен. Цвет {self.color}"

        return f"Цвет не изменился. Авто остался в прежнем цвете {self.color}"

    def is_running_engine(self):  # метод запроса -запущен ли двигатель?

        if self.state == False:
            return "Двигатель заглушен"

        return "Двигатель работает"


# Задача №2
# Создайте класс для моделирования работы смартфона. В качестве полей задаются: марка, модель, операционная система,
# объем встроенной памяти, объем оперативной памяти, заряд батареи (в процентах), состояние "включен/выключен".
# Реализовать операции: включение и выключение смартфона, установка новой операционной системы, установка/удаление
# приложений, изменение уровня заряда батареи (зарядка и разрядка), опрос состояния смартфона (включен или выключен),
# опрос текущего уровня заряда батареи. Операция вывода на экран ( __str__) должна аккумулировать
# состояние полей объекта.

from typing import Literal


class Smartphone:
    marca: str
    model: str
    o_sistem: str
    memory_capa: int
    charge: int
    current_state: bool

    def __init__(self, marca: str, model: str, o_sistem: str, memory_capa: int, charge: int, current_state: bool):

        self.marca = marca
        self.model = model
        self.o_sistem = o_sistem
        self.memory_capa = memory_capa
        self.charge = charge
        self.current_state = current_state

        if self.charge > 100 or self.charge < 0:
            raise ValueError("Заряд батареи, не может превышать 100% либо быть меньше нуля")

    def __str__(self):

        return f"""Смартфон. Модель {self.marca} {self.model}. С предустановленной операционной системой: {self.o_sistem}.
Имеет объем встроенной памяти: {self.memory_capa} Гб; Текущий заряд: {self.charge}%; Состояние: {self.current_state}."""

    def switching(self, command: Literal['y', 'n']):  # Метод вкл / выкл. смартфона

        if command == 'y' and self.current_state == False:
            self.current_state = True
            return "Смартфон включен"

        elif command == 'y' and self.current_state == True:
            return "Смартфон уже включен"

        elif command == 'n' and self.current_state == True:
            self.current_state = False
            return "Смартфон выключен"

        return "Смартфон уже выключен"

    def new_os(self, new_os: str):  # Метод установки нов. OS

        if new_os.lower() != self.o_sistem.lower():
            self.o_sistem = new_os
            return f"Операционная система переустановлена на {self.o_sistem}"

        return f"Операционная осталась прежней {self.o_sistem}"

    def set_application(self, command: bool):  # Метод установки нов. приложения

        if command == True:
            return "Установлено новое приложение"

        return "Отказались от установки нового приложения"

    def set_charge(self):  # Метод зарядки смартфона

        if self.charge == 100:
            return f"Смартфон заряжен полностью: {self.charge} %"

        return f"Смартфон требуется подзарядить. Текущий заряд: {self.charge} %"

    def status_smart(self):  # Метод опроса состояния смартфона Вкл/Выкл

        if self.current_state == True:
            return "Смартфон включен"

        return "Смартфон выключен"

    def current_charge(self):  # Метод опроса текущего заряда

        if self.current_state == False:
            return "Для начала включите смартфон"

        return f"Текущий заряд смартфона: {self.charge} %"


# Задача №3
# Создайте класс для моделирования зелья в Хогвартсе. В качестве полей задаются: название зелья, ингредиенты (список),
# сложность приготовления (по шкале от 1 до 10), эффект зелья, состояние "приготовлено/не приготовлено".
# Реализовать операции: добавление ингредиента, удаление ингредиента, изменение сложности приготовления зелья,
# изменение эффекта зелья, опрос состояния зелья (приготовлено или не приготовлено), опрос текущих ингредиентов.
# Операция вывода на экран ( ) должна аккумулировать состояние полей объекта.

class Potion:
    potion_view: str
    ingredients: list[str]
    difficulty: int
    potion_effect: str
    state: bool

    def __init__(self, potion_view: str, ingredients: list[str], difficulty: int, potion_effect: str, state: bool):
        self.potion_view = potion_view
        self.ingredients = [i.lower() for i in ingredients]
        self.difficulty = difficulty
        self.potion_effect = potion_effect.capitalize()
        self.state = state

        if self.difficulty < 1 or self.difficulty > 10:
            raise ValueError("Сложность задается в диапазоне от 1 - 10")

    def __str__(self):
        return f"""Зелье: {self.potion_view}. Имеет в своем составе ингредиенты {self.ingredients};
сложность приготовления: {self.difficulty} бал.; эффект зелья: {self.potion_effect}; состояние: {self.state}"""

    def add_ingredient(self, ingredient: str): # Метод добавления ингредиента

        ingredient = ingredient.lower()
        if not ingredient in self.ingredients:
            self.ingredients.append(ingredient)
            return f"Ингредиент {ingredient}, добавлен"

        return "Данный ингредиент, уже в списке"

    def deletion_ingredient(self, ingredient: str): # Метод удаления ингредиента

        ingredient = ingredient.lower()
        if ingredient in self.ingredients:

            self.ingredients.remove(ingredient)
            return f"Ингредиент {ingredient} удален из списка"

        return f"Ингредиент {ingredient}, отсутствует в списке ингредиентов"

    def change_difficulty(self, param: int): # Метод изменения сложности приготовления зелья

        param = int(param)
        if param < 1 or param > 10:
            raise ValueError("Вводимые значения должны быть в диапазоне <1-10>")

        if not param == self.difficulty:

            self.difficulty = param
            return f"Выставлен новый уровень сложности приготовления зелья: {self.difficulty} бал."

        return f"Уже выставлен данный уровень сложности"

    def change_effect(self, new_effect: str): # Метод изменения эффекта зелья

        new_effect = new_effect.capitalize()
        if new_effect != self.potion_effect:

            self.potion_effect = new_effect
            return f"Установлен новый эффект зелья: {self.potion_effect}"

        return "Зелье уже имеет данный эффект"

    def status_state(self): # Состояние зелья (приготовлено/не приготовлено)

        return f"Состояние зелья: {self.state}"

    def status_ingredients(self): # Текущие ингредиенты

        return f"Список ингредиентов зелья: {self.ingredients}"


# Задача №4
# Создайте классы Library, Book, User для моделирования библиотечной системы. В классе Library задаются поля:
# название библиотеки, адрес, список книг (список объектов класса Book), список зарегистрированных пользователей
# (список объектов класса User).
# В классе задаются поля: название книги, автор, год издания, жанр, состояние "в наличии/выдана", текущий пользователь
# (объект класса User или None, если книга в наличии).
# В классе User задаются поля: имя пользователя, номер читательского билета, список взятых книг
# (список объектов класса Book).
#
# Реализовать операции для класса Library:
# добавление книги в библиотеку, удаление книги из библиотеки, регистрация
# пользователя, выдача книги пользователю (с проверкой на наличие книги),
# возврат книги от пользователя, опрос текущего состояния книг и пользователей.
#
# Для класса Book: изменение состояния книги (в наличии/выдана), назначение
# текущего пользователя, изменение жанра, опрос текущего состояния книги.
#
# Для класса User: добавление книги в список взятых, удаление книги из списка
# взятых, опрос текущего списка взятых книг.

# Операции вывода на экран (__str__ ) для всех классов должны аккумулировать состояние полей объектов.

# Методы класса Library :
# 1. add_book(book: Book):
# • Добавляет книгу в список книг библиотеки.book
# • Проверяет, что книга не дублируется в библиотеке.
# 2. remove_book(book: Book):
# • Удаляет книгу из списка книг библиотеки.book
# • Проверяет, что книга существует в библиотеке.
# 3. register_user(user: User):
# • Регистрирует нового пользователя user в библиотеке, добавляя его в список пользователей.
# • Проверяет, что пользователь не дублируется в библиотеке.
# 4. issue_book(book: Book, user: User)
# • Выдает книгу book пользователю user, если книга в наличии.
# • Обновляет состояние книги на "выдана" и назначает текущего пользователя.
# • Добавляет книгу в список взятых книг пользователя.
# 5. return_book(book: Book, user: User)
# • Возвращает книгу book от пользователя user обратно в библиотеку.
# • Обновляет состояние книги на "в наличии" и снимает назначение текущего пользователя.
# • Удаляет книгу из списка взятых книг пользователя.
# 6. get_books_status() -> str
# • Возвращает строку, содержащую состояние всех книг в библиотеке
# (название книги, автор, состояние, текущий пользователь).
# 7. get_users_status() -> str
# • Возвращает строку, содержащую состояние всех зарегистрированных
# пользователей (имя, номер читательского билета, список взятых книг).


class User:
    name: str
    library_card_number: int
    list_book_user: list[Book]

    def __init__(self, name: str, library_card_number: int):

        self.name = name
        self.library_card_number = library_card_number
        self.list_book_user = []

        pass

class Book:
    title: str
    autor: str
    year: int
    genre: str
    status_book: str
    current_user: [User]

    def __init__(self, title: str, autor: str, year: int, genre: str):

        self.title = title
        self.autor = autor
        self.year = year
        self.genre = genre
        self.status_book = "В наличии"
        self.current_user = None

        pass

class Library:

    library_name: str
    library_address: str
    book_list: list[Book]
    user_list: list[User]

    def __init__(self, library_name: str, library_address: str):

        self.library_name = library_name
        self.library_address = library_address
        self.book_list = []
        self.user_list = []

        pass
