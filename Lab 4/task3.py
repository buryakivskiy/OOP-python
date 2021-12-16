from abc import ABC, abstractmethod

class ICourseFactory(ABC):
    @abstractmethod
    def setSpecialty():
        pass

class ICourse(ICourseFactory):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def setTeacher(self):
        pass

    @abstractmethod
    def setPlan(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class ITeacher(ICourseFactory):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def setName(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ILocalCourse(ICourse):
  @abstractmethod
  def setAuditory(self):
    pass


class IOffsiteCourse(ICourse):
  @abstractmethod
  def setPlace(self):
    pass

    
class Course(ICourseFactory):
    def __init__(self,specialization,teacher,plan):
        if not (isinstance(specialization,str) and isinstance(teacher,Teacher) and isinstance(plan,list)):
            raise TypeError('Wrong type')
        if teacher.specialization != specialization:
            raise ValueError('Wrong specialization')
        self.specialization = specialization
        self.teacher = teacher
        self.plan = plan   

    def setSpecialty(self,specialization):
        self.specialization = specialization
    
    def setTeacher(self,teacher):
        self.teacher = teacher

    def setPlan(self,plan):
        self.plan = plan

    def __str__(self):
        return f'Specialization: {self.specialization}\nPlan: {self.plan}\n'

class LocalCourse(Course):  
    def __init__(self, specialization, teacher, plan,auditory):
        if not isinstance(auditory, int):
            raise TypeError("Wrong type")
        super().__init__(specialization, teacher, plan)
        self.auditory = auditory

    def setAuditory(self,auditory):
        self.auditory = auditory
    
    def __str__(self):
        return f'Specialization: {self.specialization}\nPlan: {self.plan}\nAuditory: {self.auditory}\n'


class OffsiteCourse(Course):  
    def __init__(self, specialization, teacher, plan,place):
        if not isinstance(place, str):
            raise TypeError("Wrong type")
        super().__init__(specialization, teacher, plan)
        self.place = place

    def setPlace(self,place):
        self.place = place

    def __str__(self):
        return f'Specialization: {self.specialization}\nPlan: {self.plan}\Place: {self.place}\n'  

class Teacher(ICourseFactory):
    def __init__(self, specialization, name):
        if not (isinstance(specialization, str) and isinstance(name, str)):
            raise TypeError('Wrong type')
        self.setSpecialty(specialization)
        self.setName(name)  

    def setSpecialty(self,specialization):
        self.specialization = specialization
    
    def setName(self, name):
        self.name = name

    def __str__(self):
        return f'Name: {self.name}\nSpecialization: {self.specialization}\n'
    
class LocalTeacher(Teacher):  
    def __init__(self, specialization, name):
        super().__init__(specialization, name)

class OffsiteTeacher(Teacher):  
    def __init__(self, specialization, name):
        super().__init__(specialization, name)


teacher = LocalTeacher("it", "Serhiy") 
print(teacher)

course = LocalCourse("it", teacher, ['math', 'eng'], 156)
print(course)

# err (Wrong type)
# course2 = OffsiteCourse("it", teacher, ['math', 'eng'], 156)


    
