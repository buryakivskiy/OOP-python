from math import gcd

class Rational:
    def __init__(self, numerator = 1, denominator = 1):
        if denominator and isinstance(numerator,int) and isinstance(denominator,int):
            self.__numerator = numerator/gcd(numerator, denominator)
            self.__denominator = denominator/gcd(numerator, denominator)
        else:
            return None

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
    try:
        a1, a2 = map(int, input().split('/'))
        b1, b2 = map(int, input().split('/'))
        a = Rational(a1, a2)
        b = Rational(b1, b2)
        print('Add: ', (a + b).getSimple())
        print('Sub: ', (a - b).getSimple())
        print('Mul: ', (a * b).getSimple())
        print('Div: ', (a / b).getSimple())
    except:
        print('Something went wrong!')

main()