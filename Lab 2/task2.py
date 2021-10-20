from math import gcd

class Rational:
    def __init__(self, numerator = 1, denominator = 1):
        if isinstance(numerator, int) and isinstance(denominator, int):
            if denominator:
                self.__numerator = numerator // gcd(numerator, denominator)
                self.__denominator = denominator // gcd(numerator, denominator)
            else:
                raise ZeroDivisionError("Zero division")
        else:
            raise TypeError("Uncorrect type")

    def getFloat(self):
        return self.__numerator/self.__denominator

    def getSimple(self):
        return f'{int(self.__numerator)}/{int(self.__denominator)}'

    def __add__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Rat type only")
        numerator = int(self.__numerator*other.__denominator + self.__denominator*other.__numerator)
        denominator = int(self.__denominator*other.__denominator)
        return Rational(numerator, denominator)
    def __sub__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Rat type only")
        numerator = int(self.__numerator*other.__denominator - self.__denominator*other.__numerator)
        denominator = int(self.__denominator*other.__denominator)
        return Rational(numerator, denominator)

    def __mul__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Rat type only")
        denominator = int(self.__denominator * other.__denominator)
        numerator = int(self.__numerator * other.__numerator)
        return Rational(numerator, denominator)

    def __truediv__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Rat type only")
        denominator = int(self.__denominator * other.__numerator)
        numerator = int(self.__numerator * other.__denominator)
        return Rational(numerator, denominator)

def main():
    a = Rational(3, 4)
    b = Rational(2, 3)
    print('Add: ', (a + b).getSimple())
    print('Sub: ', (a - b).getSimple())
    print('Mul: ', (a * b).getSimple())
    print('Div: ', (a / b).getSimple())

main()