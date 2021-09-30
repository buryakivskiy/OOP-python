class Student:
    count = 0

    def __new__(cls, fName, **kwargs):
        if cls.count == 10:
            return None
        else: 
            return super(Student, cls).__new__(cls)

    def __init__(self, firstName, **kwargs):
        self.method()
        self.firstName = firstName
        for indx in kwargs:
            self.__dict__[indx] = kwargs[indx]

    @classmethod
    def method(cls):
        cls.count += 1

def main():
    c1 = Student('Serhiy', age=19)
    c2 = Student('Serhiy', age=20)
    c3 = Student('Serhiy', age=21)
    c4 = Student('Serhiy', age=21)
    c5 = Student('Serhiy', age=21)
    c6 = Student('Serhiy', age=21)
    c7 = Student('Serhiy', age=21)
    c8 = Student('Serhiy', age=21)
    c9 = Student('Serhiy', age=21)
    c10 = Student('Serhiy', age=21)
    c11 = Student('Serhiy', age=21)
    print(Student.count)
    print(c11)

main()