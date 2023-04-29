'''7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения
 комплексных чисел. Проверьте работу проекта, создав экземпляры
 класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
  Проверьте корректность полученного результата.'''


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real,
                             self.imaginary + other.imaginary)

    def __mul__(self, other):
        # z1 = a1 + b1*i, z2 = a2 + b2*i
        # a1*a2 - b1*b2 + (a1.b2 + b1*a2)i
        return ComplexNumber(
            self.real * other.real - self.imaginary * other.imaginary,
            self.real * other.imaginary + self.imaginary * other.real)

    def __str__(self):
        if self.imaginary > 0:
            return f"{self.real}+{self.imaginary}i"
        elif self.imaginary < 0:
            return f"{self.real}{self.imaginary}i"
        else:
            return f"{self.real}"


# проверка работы класса
a = ComplexNumber(2, 3)
b = ComplexNumber(4, -5)
print(a + b)  # должно вывести "6-2i"
# a1*a2 - b1*b2 + (a1.b2 + b1*a2)i
# 2*4 - 3* (-5) + (2*(-5) + 3*4)i
print(a * b)  # должно вывести "23+2i"
print(ComplexNumber(4, 0))