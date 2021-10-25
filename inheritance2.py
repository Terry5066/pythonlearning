class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)

x=person("terence","mpofu")
x.printname()

class student(person):
    pass

class student(person):
    def __init__(self,fname,lname):
        person.__init__(self,fname,lname)


class child(person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)

class Student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.gradyear=year

    def welcome(self):
        print('welcome',self.firstname,self.lastname,"to the class of",self.gradyear)

a=Student('terence','mpofu',2010)
a.welcome()
