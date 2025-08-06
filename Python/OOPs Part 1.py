
                    # Class and object...............................


class Car:
    brand="Honda"
    color="White"
    model="City"

c1=Car()
print(c1.brand)
print(c1.model)
print(c1.color)


                    # Constructor...............................


class Student:
    college="Apna College"

    def __init__(self,Name,Marks):
        self.name=Name
        self.marks=Marks
        print("Adding new Objects to class.......")

s1=Student("Wali", 43)
print(s1.name, s1.marks, s1.college)

s2=Student("Zain", 46 )
print(s2.name, s2.marks, s2.college)

s3=Student("ALi", 44)
print(s3.name, s3.marks, s3.college)


                    # Methods...............................


class Student:

    college="Apna School"

    def __init__(self, Name, Marks): #Constructor
        self.name=Name
        self.mark=Marks       

    def Hello(self): #Method
        print("Hello, Welocme to Student's class,",self.name)

    def get_mark(self):
        return(self.mark)    

s1=Student("Wali", 43)
s1.Hello()
print(s1.get_mark())


                    # Problem...............................


class Student:

    def __init__(self, Name, Mark):
        self.name=Name
        self.mark=Mark

    def cal_avg(self):
        sum=0
        for i in self.mark:
            sum+=i
        print ("Hi",self.name,"Your average score is =>",sum/6)


s1=Student("Wali Muhammad", [94,91,83,95,76,90])
s1.cal_avg()


                    # Static Method...............................


class Student:

    @staticmethod
    def hello():
        print("Helo students")
    college="Apna College" 

    def __init__(self,Name,Marks):
        self.name=Name
        self.marks=Marks
        print("Adding new Objects to class.......")

s1=Student("Wali", 43)
s1.hello()
print(s1.name, s1.marks, s1.college)


                    # Problem...............................


class Account():

    def __init__(self, name, account, balance):
        self.name=name
        self.acc=account
        self.bal=balance

    def cal_debit(self, amount):
        self.bal -= amount
        print("Rs =>",amount,"Debited.....")

    def cal_credit(self, amount):
        self.bal += amount
        print("Rs =>",amount,"Credited....") 
   
    
    def get_balance(self):
        print("Your Balance is =>", self.bal)
        return


acc1= Account("Walli Muhammad" ,"PK24************7491" ,0)
print("HI",acc1.name)    
print("Your Account No is => ",acc1.acc)   
print("Available Balance is => ",acc1.bal)    

acc1.cal_credit(671079)
acc1.get_balance()
acc1.cal_debit(124500)
acc1.get_balance()

