class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def get_cpu(self):
        return self.__cpu

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def get_memory(self):
        return self.__memory

    def set_memory(self, memory):
        self.__memory = memory

    def make_computations(self):
        return {
            'sum': self.__cpu + self.__memory,
            'difference': self.__cpu - self.__memory,
            'product': self.__cpu * self.__memory,
            'quotient': self.__cpu / self.__memory if self.__memory != 0 else 'Undefined'
        }

    def __str__(self):
        return f"Computer: CPU = {self.__cpu}, Memory = {self.__memory}"

    def __eq__(self, other):
        if isinstance(other, Computer):
            return self.__memory == other.get_memory()
        return False

    def __ne__(self, other):
        if isinstance(other, Computer):
            return self.__memory != other.get_memory()
        return False

    def __lt__(self, other):
        if isinstance(other, Computer):
            return self.__memory < other.get_memory()
        return False

    def __le__(self, other):
        if isinstance(other, Computer):
            return self.__memory <= other.get_memory()
        return False

    def __gt__(self, other):
        if isinstance(other, Computer):
            return self.__memory > other.get_memory()
        return False

    def __ge__(self, other):
        if isinstance(other, Computer):
            return self.__memory >= other.get_memory()
        return False


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def get_sim_cards_list(self):
        return self.__sim_cards_list

    def set_sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def call(self, sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}")
        else:
            print("Неверный номер сим-карты")

    def __str__(self):
        return f"Phone: SIM Cards = {', '.join(self.__sim_cards_list)}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Симуляция построения маршрута до локации: {location}")
        print("Поиск маршрута...")
        print(f"Маршрут до {location} успешно построен.")

    def __str__(self):
        return f"SmartPhone: {Computer.__str__(self)}, {Phone.__str__(self)}"

computer = Computer(2.5, 8)
phone = Phone(['SIM1', 'SIM2'])
smartphone1 = SmartPhone(2.5, 4, ['SIM1', 'SIM2'])
smartphone2 = SmartPhone(3.0, 6, ['SIM3', 'SIM4'])

print(computer)
print(computer.make_computations())

print(phone)
phone.call(1, '+996707157023')
phone.call(2, '+9960707072341')

print(smartphone1)
smartphone1.use_gps('Бишкек')
print(smartphone1.make_computations())

print(smartphone2)
smartphone2.use_gps('Ош')
print(smartphone2.make_computations())

print(computer == smartphone1)
print(computer != smartphone2)
print(computer < smartphone1)
print(computer <= smartphone2)
print(computer > smartphone1)
print(computer >= smartphone2)
