class Rational:
    def __init__(self, numerator = 1, denominator = 1):
        if denominator and isinstance(numerator,int) and isinstance(denominator,int):
            self.__numerator = numerator/mostCommon(numerator, denominator)
            self.__denominator = denominator/mostCommon(numerator, denominator)
        else:
            return None
    def getFloat(self):
        return self.__numerator/self.__denominator
    def getSimple(self):
        return str(int(self.__numerator)) + '/' + str(int(self.__denominator))

def mostCommon(a, b):
    if a % b == 0:
        return b
    else:
        return mostCommon(b, a % b)

def main():
    try:
        userInut = input()
        a, b = map(int, userInut.split('/'))
        fraction = Rational(a, b)
        print(fraction.getFloat())
        print(fraction.getSimple())
    except:
        print('Something went wrong!')

main()
    
