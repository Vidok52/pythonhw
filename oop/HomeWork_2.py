class Department(object):
    def __init__(self,DepName):
        self.DepName = DepName
        self.ManList = []
    
    def get_salary(self):
        for i in self.ManList:
            i.get_salary()
            for j in i.Subordinates:
                j.get_salary()

    
    
class Employee(object):
    def __init__(self,Name,Surname,Experience,Profession,Salary,Manager=None):
        self.Name = Name
        self.Surname = Surname
        self.Experience = Experience
        self.Salary = Salary
        self.Manager = Manager
        self.Subordinates = []
        self.Profession = Profession

        self.counter()

    
    def counter(self):
        if self.Manager:
            self.Manager.Subordinates.append(self)



class manager(Employee):

    def __init__(self,Name,Surname,Experience,Profession,Salary,Department,Manager=None):
        super(manager, self).__init__(Name,Surname,Experience,Profession,Salary,Manager)
        self.Department = Department

        self.counter()
        self.group()

    def group(self):
        self.Department.ManList.append(self)

    def get_salary(self):
        counter = 0
        dev = 0
        des = 0 
        for i in self.Subordinates:
            counter +=1
            if i.Profession == "Designer": des += 1
            else: dev += 1
        if dev > counter / 2:
            self.Salary = self.Salary * 1.1
        if counter >= 5:
            self.Salary = self.Salary + 200
        elif counter >= 10:
            self.Salary = self.Salary + 300
        
        print("{0} {1} got salary: {2}$".format(self.Name,self.Surname,self.Salary))

class developer(Employee):     
    def get_salary(self):
        if self.Experience >= 2:
            self.Salary =  self.Salary + 200
        elif self.Experience >=5:
            self.Salary = self.Salary * 1.2 + 500
        print("{0} {1} got salary: {2}$".format(self.Name,self.Surname,self.Salary))

class designer(Employee):
    def __init__(self,Name,Surname,Experience,Profession,Salary,coefficient,Manager=None):
        super(designer, self).__init__(Name,Surname,Experience,Profession,Salary,Manager)
        self.coefficient = coefficient

    def get_salary(self):
        self.Salary = self.Salary * self.coefficient
        print("{0} {1} got salary: {2}$".format(self.Name,self.Surname,self.Salary))


IT = Department("IT")
Anton = manager("Anton","Golovin",5,"Manager",1500,IT)
Vitaliy = developer("Vitaliy","Lysenko",1,"Developer",1500,Manager=Anton)
Artem = designer("Artem","Kubrachenko",3,"Designer",1200,0.8,Manager=Anton)
Vadim = developer("Vadim","Ostachinskiy",2,"Developer",1300,Manager=Anton)

IT.get_salary()

# for i in Anton.Subordinates:
#     print(i.Name)