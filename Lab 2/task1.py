class Rectangle:
    lenght: float
    width: float
    def __init__(self, lenght=1, width=1):
        self.lenght = lenght
        self.width = width
    def perimeter(self):
        return (self.width + self.lenght)*2
    def area(self):
        return self.width * self.lenght
    def getlen(self):
        return self.lenght
    def getWid(self):
        return self.width
    def setLen(self, value):
        if (value > 0 and value < 20):
            self.lenght = value
        else:
            return None
    def setWid(self, value):
        if (value > 0 and value < 20):
            self.width = value
        else:
            return None

def main():
    try:
        while(True):
            print('Enter length and width: ')
            len, wid = map(float, input().split())
            if (len <= 0 or wid <= 0):
                print('Uncorrect values!\n')
            else: 
                break
        rectangle = Rectangle()
        rectangle.setLen(len)
        rectangle.setWid(wid)
        print('Lenght is: ', rectangle.getlen())
        print('Width is: ', rectangle.getWid())
        print('perimeter is: ', rectangle.perimeter())
        print('area is: ', rectangle.area())
    except:
        print('Something went wrong!')

main()