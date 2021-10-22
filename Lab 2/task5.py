from os import name, pread
import statistics

MAX_STUDENTS = 20
 
class Student:
    def __init__(self, name, surname, recordBookId, grades):
        if not isinstance(name, str) or not isinstance(surname, str) or not isinstance(recordBookId, int) or not all(isinstance(mark, int) for mark in grades):
             raise TypeError("Uncorrect type")
        self.__name = name
        self.__surname = surname
        self.__recordBookId = recordBookId
        self.__grades = grades
        self.averageMark = statistics.mean(self.__grades)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Uncorrect type")
        if not name:
            raise ValueError("Uncorrect value")
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("Uncorrect type")
        if not surname:
            raise ValueError("Uncorrect value")
        self.__surname = surname

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, grades):
        if not all(isinstance(mark, int) for mark in grades):
            raise TypeError("Uncorrect type")
        self.__grades = grades

    
    def __str__(self):
        return f'{self.__name} {self.__surname}'

class Group:
    surname_name = []
    def __init__(self, students):
        if not all(isinstance(student, Student) for student in students):
            raise TypeError("Uncorrect type")
        if len(students) > MAX_STUDENTS:
            raise ValueError("Uncorrect number of students")
        self.surname_name.append(students)
        for i in range(len(students)):
            for j in range(len(students)):
                if f'{students[i]}' == f'{students[j]}' and i!=j:
                    raise ValueError("Uncorrect name and surname")
        self.students = students
        self.bestFive = self.__top5__()
    
    def __top5__(self):
        rate = sorted(self.students, key = lambda student: student.averageMark, reverse = True)
        return rate[0:5]

student1 = Student("Maks", "Brydiyuk", 1, [68, 45, 89, 100, 77])
student2 = Student("Serhiy", "Buryakivskiy", 1, [70, 55, 89, 100, 70])
student3 = Student("Artem", "Tarasov", 1, [65, 44, 89, 100, 85])
student4 = Student("Pavlo", "Nedashivskiy", 1, [68, 45, 89, 100, 83])
student5 = Student("Maks", "Klapatiuk", 1, [34, 45, 89, 77, 76])
student6 = Student("Denis", "Zaharia", 1, [78, 45, 89, 54, 55])
student7 = Student("Vitalya", "Kovalov", 1, [98, 45, 100, 100, 61])
student8 = Student("Roma", "Tkachenko", 1, [76, 45, 43, 100, 91])
student9 = Student("Vasya", "Pavliuk", 1, [57, 45, 89, 65, 85])
student10 = Student("Yarik", "Duhanov", 1, [86, 45, 89, 100, 55])

group = Group([student1, student2, student3, student4, student5, student6, student7, student8, student9, student10])

for i in range(len(group.bestFive)):
    print(f'{i+1}) {group.bestFive[i]}')