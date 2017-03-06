import sys


class ComplexNumber:
    def __init__(self, real=0.0, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        result = ComplexNumber()
        result.real = self.real + other.real
        result.imaginary = self.imaginary + other.imaginary
        return result

    def __sub__(self, other):
        result = ComplexNumber()
        result.real = self.real - other.real
        result.imaginary = self.imaginary - other.imaginary
        return result

    def __mul__(self, other):
        result = ComplexNumber()
        result.real = self.real * other.real - self.imaginary * other.imaginary
        result.imaginary = (self.real * other.imaginary +
                            self.imaginary * other.real)
        return result

    def __div__(self, other):
        result = ComplexNumber()
        t = other.real * other.real + other.imaginary * other.imaginary
        result.real = (self.real * other.real +
                       self.imaginary * other.imaginary) / t
        result.imaginary = (self.imaginary * other.real -
                            self.real * other.imaginary) / t
        return result

    def __str__(self):
        if self.imaginary == 0:
            result = '%.2f' % self.real
        elif self.real == 0:
            result = '%.2fi' % self.imaginary
        elif self.imaginary < 0:
            result = '%.2f - %.2fi' % (self.real, self.imaginary * -1)
        else:
            result = '%.2f + %.2fi' % (self.real, self.imaginary)
        return result


f = open("input.txt")
if __name__ == "__main__":
    for line in f:
        print eval(line.strip())
f.close()
