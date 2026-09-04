

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    # static metohd

    @staticmethod
    def is_valid_position(position):
        valid_positions = ['Manager', 'Cook', 'Cashier', 'Janitor']
        return position in valid_positions


emp = Employee.is_valid_position("cook")
emp1 = Employee("Eugune", "Manager")
emp2 = Employee("Squidward", "Cashier")
emp3 = Employee('SpongeBob', "Cook")

print(emp1.get_info())
print(emp2.get_info())
print(emp3.get_info())
