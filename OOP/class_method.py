

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    # instances method

    def get_info(self):
        return f'{self.name} {self.gpa}'

    # class method

    @classmethod
    def get_count(cls):
        return f'Total # of students: {cls.count}'

    @classmethod
    def gpa_count(cls):
        if cls.count == 0:
            return 0
        else:
            return f'Average GPA : {cls.total_gpa / cls.count:.2f}'


stud1 = Student('Gilbert', 5.0)
stud2 = Student('Gerald', 4.0)
stud3 = Student('Raffy', 3.0)

stud = Student.get_count()
gpa = Student.gpa_count()
print(stud)
print(gpa)
