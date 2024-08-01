"""
Complex Numbers
@author Alejandro Serna
"""

class Complex:
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Complex(self.real + other, self.imag)
        elif isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        else:
            raise TypeError("Unsupported operand type(s) for +")

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Complex(self.real - other, self.imag)
        elif isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        else:
            raise TypeError("Unsupported operand type(s) for -")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Complex(self.real * other, self.imag * other)
        elif isinstance(other, Complex):
            return Complex(self.real * other.real - self.imag * other.imag,
                           self.real * other.imag + self.imag * other.real)
        else:
            raise TypeError("Unsupported operand type(s) for *")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Complex(self.real / other, self.imag / other)
        elif isinstance(other, Complex):
            denom = other.real ** 2 + other.imag ** 2
            return Complex((self.real * other.real + self.imag * other.imag) / denom,
                           (self.imag * other.real - self.real * other.imag) / denom)
        else:
            raise TypeError("Unsupported operand type(s) for /")

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return Complex(other) - self

    def __rmul__(self, other):
        return self * other

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            denom = self.real ** 2 + self.imag ** 2
            return Complex(other * self.real / denom, -other * self.imag / denom)
        else:
            raise TypeError("Unsupported operand type(s) for /")

    def __str__(self):
        real_str = f"{self.real:.0f}" if self.real.is_integer() else f"{self.real}"
        imag_str = f"{self.imag:.0f}" if self.imag.is_integer() else f"{self.imag}"
        return f"({real_str} + {imag_str}i)"

if __name__ == '__main__':
    a = Complex(1.0, 2.0)
    b = Complex(3.0, 4.0)
    i = 5

    print(f'{a} + {b} = {a + b}')
    print(f'{a} - {b} = {a - b}')
    print(f'{a} * {b} = {a * b}')
    print(f'{a} / {b} = {a / b}')

    print(f'{a} + {i} = {a + i}')
    print(f'{a} - {i} = {a - i}')
    print(f'{a} * {i} = {a * i}')
    print(f'{a} / {i} = {a / i}')

    print(f'{i} + {a} = {i + a}')
    print(f'{i} - {a} = {i - a}')
    print(f'{i} * {a} = {i * a}')
    print(f'{i} / {a} = {i / a}')
