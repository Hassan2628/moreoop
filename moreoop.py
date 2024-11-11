class Employee:
    def __init__(self,name,role,salary,DoB):
        self.name = name
        self.role = role
        self.salary = salary
        self.DoB = DoB
    def increase_salary(self):
        increase = int(input("How much of a percentage increase would you like for your salary?:  "))
        self.salary = ((increase)+100/100)*self.salary
        print(f"Your new salary is:{self.salary}")
    def calculate_age(self):
        

        