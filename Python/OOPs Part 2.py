                   
                   
                    # del...............................
  

class Student:
    
    def __init__(self, name):
        self.name=name

s1=Student("Wali Muhammad")
print(s1.name)
del s1.name
print(s1.name)      


                    # Private & Public ...............................


class Student:

    def __init__(self,Name,Age):
        self.name=Name
        self.age=Age

    def __hello(self):
        print("HEllo Students.....") 

    def welcome(self):
        self.__hello()


s1=Student("wali", 19)
print(s1.welcome())
print("HI",s1.name,"YOUR AGE IS",s1.age)


                    # Class Method ...............................


class Id:
    number=12345
    
    @classmethod
    def change(cls, number):
        cls.number=number
    #    self.number=number
    #    self.__class__.number(98765)
    #    Id.number=number
        
n1=Id()
n1.change(98765)
print(n1.number) 
print(Id.number)   


                    # Property ...............................



class Student:
    
    def __init__(self,phy,com,mat):
        self.physics=phy
        self.computer=com
        self.math=mat
        
        
    # def cal_percent(self):
    #     self.percentage= str((self.physics + self.computer + self.math) / 3 ) + "%"
    
    @property
    def percentage(self):
        return str((self.physics + self.computer + self.math) / 3 ) + "%"
    
    
s1=Student(67,89,43)
print(s1.percentage)


s1.computer=90
s1.physics=95
s1.math=90
print(s1.percentage)  