class Figure:
    _unit = 'cm'
    @classmethod
    def get_unit(cls):
        return cls._unit
    @classmethod
    def set_unit(cls, new_unit):
        if new_unit in ('cm', 'mm'):
            cls._unit = new_unit
        else:
            raise ValueError("Допустимые значения: 'cm' или 'mm'")
    def __init__(self):
        pass
    def calculate_area(self):
        raise NotImplementedError
    def info(self):
        raise NotImplementedError

class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length
    def calculate_area(self):
        return self.__side_length ** 2
    def info(self):
        print(f"Square side length: {self.__side_length}{self.get_unit()}, area: {self.calculate_area()}{self.get_unit()}.")
class Rectangle(Figure):
    def __init__(self,length,width):
        super().__init__()
        self.__length = length
        self.__width = width
    def calculate_area(self):
        return self.__length * self.__width
    def info(self):
        print(f'Rectangle length: {self.__length}{self.get_unit()}, width: {self.__width}{self.get_unit()},  area: {self.calculate_area()}{self.get_unit()}')

Square_1 = Square(6)
Square_2 = Square(15)
Rectangle_1 = Rectangle(12,3)
Rectangle_2 = Rectangle(23,14)
Rectangle_3 = Rectangle(14,25)
figure = [Square_1,Square_2,Rectangle_1,Rectangle_2,Rectangle_3]
for i in figure:
    i.info()