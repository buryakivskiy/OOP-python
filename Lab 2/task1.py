class Rectangle:
    def __init__(self, lenght=1, width=1):
        self.__lenght = lenght
        self.__width = width

    @property
    def lenght(self):
        return self.__lenght

    @lenght.setter
    def lenght(self, len):
        if isinstance(len, float) and len > 0 and len < 20:
            self.__lenght = len
        else:
            return TypeError
    
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, wid):
        if isinstance(wid, float) and wid > 0 and wid < 20:
            self.__width = wid
        else:
            return TypeError

    def perimeter(self):
        return (self.width + self.lenght)*2
        
    def area(self):
        return self.width * self.lenght

def main():
    try:
        print('Enter length and width: ')
        len, wid = map(float, input().split())
        rectangle = Rectangle()
        rectangle.lenght = len
        rectangle.width = wid
        print('Lenght is: ', rectangle.lenght)
        print('Width is: ', rectangle.width)
        print('perimeter is: ', rectangle.perimeter())
        print('area is: ', rectangle.area())
        return { "success": True }
    except:
        return TypeError

print(main())