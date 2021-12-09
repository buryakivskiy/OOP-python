from math import gcd

class Rational:
    def __init__(self, numer = 1, denomin = 1):
        if not isinstance(numer, int) or not isinstance(denomin, int):
            raise TypeError("Uncorrect type")
        if not denomin:
            raise ZeroDivisionError("Zero division")
        self.numerator = numer // gcd(numer, denomin)
        self.denominator = denomin // gcd(numer, denomin)

    def reducing(self):
        gc = gcd(self.__numerator,self.__denominator)
        if self.__denominator<0:
            self.__denominator=-self.__denominator
            self.__numerator=-self.__numerator
        self.__numerator //= gc
        self.__denominator //= gc


    @property
    def numerator(self):     
        return self.numerator   

    @property
    def denominator(self):     
        return self.__denominator    

    @numerator.setter
    def numerator(self,numerator):
        if not isinstance(numerator,int):
            raise TypeError("Wrong type")
        self.__numerator = numerator   

    @denominator.setter
    def denominator(self,denominator):
        if not isinstance(denominator,int):
            raise TypeError("Wrong type")
        if not denominator:
            raise ZeroDivisionError("Zero division error")
        self.__denominator = denominator    


    def getFloat(self):
        return self.__numerator/self.__denominator

    def getSimple(self):
        return f'{self.__numerator}/{self.__denominator}'

    def __add__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Rat type only")
        numerator = self.__numerator*other.__denominator + self.__denominator*other.__numerator
        denominator = self.__denominator*other.__denominator
        return Rational(numerator, denominator)
    def __sub__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("Rat type only")
        numerator = self.__numerator*other.__denominator - self.__denominator*other.__numerator
        denominator = self.__denominator*other.__denominator
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

    def __lt__(self,other):
        return self.__numerator * other.__denominator < other.__numerator * self.__denominator
            
    def __gt__(self, other):
        return self.__numerator * other.__denominator > other.__numerator * self.__denominator

    def __le__(self,other):
        self.__numerator * other.__denominator <= other.__numerator * self.__denominator 

    def __ge__(self, other):
        return self.__numerator * other.__denominator >= other.__numerator * self.__denominator  

    def __eq__(self, other):
        return self.__numerator * other.__denominator == other.__numerator * self.__denominator 

    def __ne__(self,other):
        return self.__numerator * other.__denominator != other.__numerator * self.__denominator 

    def __iadd__(self,other):      
        self.__numerator  = self.__numerator * other.__denominator + other.__numerator * self.__denominator
        self.__denominator = self.__denominator*other.__denominator
        self.reducing()
        return self

    def __isub__(self,other):      
        self.__numerator  = self.__numerator * other.__denominator - other.__numerator * self.__denominator
        self.__denominator = self.__denominator*other.__denominator
        self.reducing()
        return self

def main():
    a = Rational(3, 4)
    b = Rational(2, 3)
    print('Add: ', (a + b).getSimple())
    print('Sub: ', (a - b).getSimple())
    print('Mul: ', (a * b).getSimple())
    print('Div: ', (a / b).getSimple())
    a += b
    print('a += b: ', a.getSimple())
    a -= b
    print('a -= b: ', a.getSimple())
    print('a > b: ', a > b)
    print('a >= b: ', a >= b)
    print('a < b: ', a < b)
    print('a <= b: ', a <= b)

main()