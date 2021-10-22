"""
7.	Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def complex_number(self):
        if self.y == 0:
            return self.x
        return (self.x, self.y)

    def __add__(self, other):
        return ComplexNumber(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return ComplexNumber(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return ComplexNumber(self.x * other.x - self.y * other.y, self.x * other.y + other.x * self.y)

    def __truediv__(self, other):
        if other.x == 0 and other.y == 0:
            raise ArithmeticError
        return ComplexNumber((self.x * other.x + self.y * other.y) / (other.x ** 2 + other.y ** 2),
                             (other.x * self.y - self.x * other.y) / (other.x ** 2 + other.y ** 2))


a = ComplexNumber(0, 1)
b = ComplexNumber(0, 1)
c = a * b
print(str(c.complex_number))


a = ComplexNumber(23, 7)
b = ComplexNumber(13, 56)
c = a / b
print(str(c.complex_number))

a = ComplexNumber(3, 7)
b = ComplexNumber(1, 6)
c = a + b
print(str(c.complex_number))

a = ComplexNumber(3, 7)
b = ComplexNumber(1, 6)
c = a - b
print(str(c.complex_number))