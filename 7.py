# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return str(complex(self.real, self.imag))

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return Complex(self.real*other.real - self.imag*other.imag, self.real*other.imag + self.imag*other.real)

first = Complex(1, 2)
second = Complex(3, 4)
print(first + second)
print(first * second)
