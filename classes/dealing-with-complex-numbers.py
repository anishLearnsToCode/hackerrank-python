import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return Complex(
            self.real * other.real - self.imaginary * other.imaginary, 
            self.real * other.imaginary + self.imaginary * other.real
        )

    def __truediv__(self, other):
        other_mod_2 = other.mod_square()
        answer = Complex(self.real / other_mod_2, self.imaginary / other_mod_2) * other.conjugate()
        return Complex(round(answer.real, 2), round(answer.imaginary, 2))

    def mod(self):
        return Complex(round(math.sqrt(self.mod_square()), 2), 0.00)

    def mod_square(self):
        return round(self.real * self.real + self.imaginary * self.imaginary, 2)

    def conjugate(self):
        return Complex(self.real, -self.imaginary)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
