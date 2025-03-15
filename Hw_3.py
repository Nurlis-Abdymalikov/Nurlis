# 1. Создать класс Computer (компьютер) с приватными атрибутами cpu и memory.
# 2. Добавить сеттеры и геттеры к существующим атрибутам.
# 3. Добавить в класс Computer метод make_computations, в котором бы выполнялись арифметические вычисления с атрибутами объекта cpu и memory.
# 4. Создать класс Phone (телефон) с приватным полем sim_cards_list (список сим-карт)
# 5. Добавить сеттеры и геттеры к существующему атрибуту.
# 6. Добавить в класс Phone метод call с входящим параметром sim_card_number и call_to_number, в котором бы распечатывалась симуляция звонка в зависимости от переданного номера сим-карты .
# 7. Создать класс SmartPhone и наследовать его от 2-х классов Computer и Phone.
# 8. Добавить метод в класс SmartPhone use_gps с входящим параметром location, который бы распечатывал симуляцию построения маршрута до локации.
# 9. В каждом классе переопределить магический метод __str__ которые бы возвращали полную информацию об объекте.
# 10. Перезаписать все магические методы сравнения в классе Computer (6 шт.), для того чтоб можно было сравнивать между собой объекты, по атрибуту memory.
# 11. Создать 1 объект компьютера, 1 объект телефона и 2 объекта смартфона
# 12. Распечатать информацию о созданных объектах.
# 13. Опробовать все возможные методы каждого объекта (например: use_gps, make_computations, call, а также магические методы).
class Computer:
    def __init__(self,cpu,memory):
        self.__cpu = cpu
        self.__memory = memory
    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__memory = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return {'sum': self.__memory + self.__cpu or self.__cpu + self.__memory,
                'difference':self.__memory - self.__cpu or self.__cpu - self.__memory,
                'product':self.__memory * self.__cpu,
                'quotient':self.__cpu / self.__memory if self.__memory != 0 else 'Undefined'\
                or self.__memory / self.__cpu if self.__cpu != 0 else 'Undefined'}

class Phone:
    def __init__(self,sim_cards_list):
        self.__sim_cards_list = sim_cards_list
    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value
        # (например: если при вызове метода передать число 1 и номер телефона, распечатывается текст “Идет звонок на номер +996 777 99 88 11” с сим-карты-1 - Beeline)

    def call(self, sim_cards_list, call_to_number):
        print(f'"Идет звонок на номер {call_to_number}с сим-карты -{sim_cards_list}"')
a = Phone(12)
print(f'{a}')




