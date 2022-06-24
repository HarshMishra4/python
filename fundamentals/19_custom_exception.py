class StudentException(Exception):
    pass

class Student:
    def __init__(self, name, regid):
        self.name = name
        self.regID = regid

class College:
    def __init__(self) -> None:
        self.student_list = []
    
    def add(self, student):
        self.student_list.append(student)
        print("Registered")

    def get_detail(self,student_id):
        for student in self.student_list:
            if student.regID == student_id:
                return student
        raise StudentException("Student Not Found")

student1 = Student("John", 1002)
student2 = Student("Kevin", 1003)
student3 = Student("Mike", 1004)
student4 = Student("Lisa", 1005)

college = College()
college.add(student1)
college.add(student2)
college.add(student3)
college.add(student4)

try:
    result = college.get_detail(1009)
    print(result.regID)
    print(result.name)
except StudentException:
    print('Student Not Found')