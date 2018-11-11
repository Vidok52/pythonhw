import sys

class SalaryGivingError(Exception):
    """When manager isnt have subordinates"""
    pass

class WrongEmployeeRoleError(Exception):
    pass

class Department(object):
    def __init__(self,DepName):
        self.DepName = DepName
        self.ManList = []
    
    def get_salary(self):
        for i in self.ManList: 
            i.get_salary()
            for j in i.Subordinates: j.get_salary()

        
class Employee(object):
    def __init__(self,Name,Surname,Experience,Salary,Manager=None):
        self.Name = Name
        self.Surname = Surname
        self.Experience = Experience
        self.Salary = Salary
        self.Manager = Manager
        self.Subordinates = []

        self.counter()
    
        if self.Salary:
            if self.Experience >= 5:
                self.Salary = self.Salary * 1.2 + 500
            elif self.Experience >= 2:
                self.Salary = self.Salary + 200

    def counter(self):
        if self.Manager:
            self.Manager.Subordinates.append(self)


class manager(Employee):
    def __init__(self,Name,Surname,Experience,Salary,Department,Manager=None):
        super(manager, self).__init__(Name,Surname,Experience,Salary,Manager)
        self.Department = Department
        self.counter()
        self.group()


    def group(self):
        self.Department.ManList.append(self)

    def add_employee(self,team):
        """ Define employees(in list format) who you want to add to the manager team"""
        print("Im working")
        for i in team:
            try:
                if isinstance(i,manager):
                    raise WrongEmployeeRoleError
            except WrongEmployeeRoleError:
                print("Employee {0} has an unexpected role!".format(i.Surname))
            else:
                i.Manager = self
                self.Subordinates.append(i)
    
    def get_salary(self):
        counter = len(self.Subordinates)
        try:
            if counter < 1:
                raise SalaryGivingError
        except SalaryGivingError:
            print("This manager didnt have subordinates, please, create them")
            sys.exit(0)
        dev = 0
        for i in self.Subordinates:
            if isinstance(i, developer): dev += 1
        if dev > counter / 2: self.Salary = self.Salary * 1.1
        if counter >= 5: self.Salary = self.Salary + 200
        elif counter >= 10: self.Salary = self.Salary + 300
        
        print("{0} {1} got salary: {2}$".format(self.Name,self.Surname,self.Salary))

class developer(Employee):     
    def get_salary(self):
        print("{0} {1} got salary: {2}$".format(self.Name,self.Surname,self.Salary))

class designer(Employee):
    def __init__(self,Name,Surname,Experience,Salary,coefficient,Manager=None):
        super(designer, self).__init__(Name,Surname,Experience,Salary,Manager)
        self.coefficient = coefficient

    def get_salary(self):
        self.Salary = self.Salary * self.coefficient
        print("{0} {1} got salary: {2}$".format(self.Name,self.Surname,self.Salary))

IT = Department("IT")
Anton = manager("Anton","Golovin",5,1500,IT)
Vitaliy = developer("Vitaliy","Lysenko",1,1500,Manager=Anton)
Artem = designer("Artem","Kubrachenko",3,1200,0.8,Manager=Anton)
Vadim = developer("Vadim","Ostachinskiy",2,1300,Manager=Anton)

Irina = manager("Iryna","Golodivska",10,1500,IT)
Marina = designer("Marina","Ilyna",6,600,1.5)
Natalia = developer("Natalia","Velichenko",10,900)

Irina.add_employee([Marina,Natalia])

IT.get_salary()