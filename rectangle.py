import logging
import argparse


logging.basicConfig(filename='rectangle.log', encoding='utf-8', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class NegativeValueError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
        super().__init__(f"{self.message}, а не {self.value}")
        logging.error(f"{self.message}, а не {self.value}")

class Rectangle:
    def __init__(self, width, height=None):
        try:
            if width <= 0:
                raise NegativeValueError("Ширина должна быть положительной", width)
            if height is not None and height <= 0:
                raise NegativeValueError("Высота должна быть положительной", height)
            self.width = width
            if height is None:
                self.height = width
            else:
                self.height = height
        except NegativeValueError as err:
            print(err)
            logging.error(err)

    def set_width(self, width):
        try:
            if width < 0:
                raise NegativeValueError("Ширина должна быть положительной", width)
            self.width = width
        except NegativeValueError as err:
            print(err)
            logging.error(err)

    def set_height(self, height):
        try:
            if height < 0:
                raise NegativeValueError("Высота должна быть положительной", height)
            self.height = height
        except NegativeValueError as err:
            print(err)
            logging.error(err)

    def perimeter(self):

        return 2 * (self.width + self.height)

    def area(self):

        return self.width * self.height

    def add(self, other):

        try:
            width = self.width + other.width
            perimeter = self.perimeter() + other.perimeter()
            height = perimeter // 2 - width
            return Rectangle(width, height)
        except Exception as err:
            print(err)
            logging.error(err)

    def sub(self, other):

        try:
            if self.perimeter() < other.perimeter():
                self, other = other, self
            width = abs(self.width - other.width)
            perimeter = self.perimeter() - other.perimeter()
            height = perimeter // 2 - width
            return Rectangle(width, height)
        except Exception as err:
            print(err)
            logging.error(err)

    def lt(self, other):

        try:
            return self.area() < other.area()
        except Exception as err:
            print(err)
            logging.error(err)

    def eq(self, other):

        try:
            return self.area() == other.area()
        except Exception as err:
            print(err)
            logging.error(err)

    def le(self, other):

        try:
            return self.area() <= other.area()
        except Exception as err:
            print(err)
            logging.error(err)

    def __str__(self):

        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):

        return f"Rectangle({self.width}, {self.height})"
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Вычисление параметров прямоугольника')
    parser.add_argument('width', type=int, help='Ширина прямоугольника')
    parser.add_argument('height', type=int, nargs='?', default=None, help='Высота прямоугольника (по умолчанию равна ширине)')
    args = parser.parse_args()

    try:
        rectangle = Rectangle(args.width, args.height)
        print(f"Периметр прямоугольника: {rectangle.perimeter()}")
        print(f"Площадь прямоугольника: {rectangle.area()}")
    except ValueError:
        print("Ошибка: Ширина и высота должны быть целыми числами")



'''
Пример запуска кода:                     python rectangle.py 10 5
'''