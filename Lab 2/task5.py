from os import name
import statistics

MAX_STUDENTS = 20
 
class Student:
    surname_name = []
    def __init__(self, name, surname, recordBookId, grades):
        if not isinstance(name, str) or not isinstance(surname, str) or not isinstance(recordBookId, int) or not all(isinstance(mark, int) for mark in grades):
             raise TypeError("Uncorrect type")
        if f'{name}{surname}' in self.surname_name:
            raise ValueError("Uncorrect name and surname")
        self.name = name
        self.surname = surname
        self.surname_name.append(f'{name}{surname}')
        self.recordBookId = recordBookId
        self.grades = grades
        self.averageMark = statistics.mean(grades)
    
    def __str__(self):
        return f'{self.name} {self.surname}'
        

class Group:
    def __init__(self, students):
        if not all(isinstance(student, Student) for student in students):
            raise TypeError("Uncorrect type")
        if len(students) > MAX_STUDENTS:
            raise ValueError("Uncorrect number of students")
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

for i in range(5):
    print(f'{i+1}) {group.bestFive[i]}')