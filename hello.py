class salary:
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return(self.pay*12) + self.bonus

class Employee:
    def __init__(self,name,age,pay,bonus):
        self.name = name
        self.age = age
        self.obj_salary = salary (pay, bonus)

    def total_salary(self):
        return self.obj_salary.annual_salary()

emp = Employee('Moses', 25, 150000, 10000)
print(emp.total_salary())