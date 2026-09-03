# dunnder = double underscore
# from car import Car

# car1 = Car("BMW", 2026, "Yellow", True)
# car2 = Car("Mustang", 2026, "blue", True)
# car3 = Car("Ford", 2026, 'red', True)

# print(car3.model)
# print(car3.year)
# print(car3.color)
# print(car3.for_sale)

# car1.describe()


class Student:

    class_year = 2026
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("Gilbert", 23)
student2 = Student("Gerald", 20)
student3 = Student("raffy", 14)

print(Student.class_year)
print(Student.num_students)

print(
    f"My graduating class of {Student.class_year} has {Student.num_students} students")
