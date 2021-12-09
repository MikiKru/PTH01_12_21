class Employee:
    def __init__(self, name : str, last_name : str, salary : float):
        self.name = name
        self.last_name = last_name
        self.salary = salary
    def __str__(self):
        return f"[{self.__class__.__name__}] {self.name} {self.last_name}, zarobki: {self.salary}"
class Manager(Employee):
    def __init__(self, first_name, last_name, salary, role, list_employees=[]):
        super().__init__(first_name, last_name, salary)
        self.list_employees = list_employees
        self.role = role
    def __str__(self):
        return f"{super().__str__()} role={self.role} employees={[empl.__str__() for empl in self.list_employees]}"
    def get_empl_by_index(self, index):
        return self.list_employees[index]
    def add_empl(self, employee):
        self.list_employees.append(employee)
    def remove_by_index(self, index):
        self.list_employees.remove(self.get_empl_by_index(index))
class Company:
    def __init__(self, employees):
        self.employees = employees
    def get_employees(self):
        for empl in self.employees:
            print(empl)

p1 = Employee("Jan", "Kowalski", 4000)
p2 = Employee("Janusz", "Kot", 14000)
p3 = Employee("Adam", "Kowal", 8000)
p4 = Employee("Ada", "Nowak", 4500)
p5 = Employee("Anna", "Nowa", 4600)
m1 = Manager("Robert","Sól", 15000, "kierownik zmiany", [p1,p2,p3])
m2 = Manager("Bob","John", 25000, "kierownik działu IT", [p4,p5])
# print(m1)
# print(m2)
# print(m1.get_empl_by_index(0))
# m1.remove_by_index(0)
# m1.add_empl(p1)
# print(m1)
company = Company([p1,p2,p3, p4, p5, m1, m2])
company.get_employees()
