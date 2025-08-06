                    # Abstraction...............................


class Car:
     def __init__(self):
         self.acc=False
         self.brk=False
         self.clutuc=False
         self.gear=False

     def start(self):
         self.brk=True
         self.clutuc=True
         self.acc=True
         print("Car started....")

car1=Car()
car1.start()     


                    # Encapsulation...............................

                   

                    # Inheritance...............................
                    # Single_level / Multi_level................

class Utencil:

    @staticmethod
    def color():
        print("Grey")

    @staticmethod
    def purp():
        print("For Writing")


class Pencil(Utencil):

    def __init__(self, name ,price):
        self.name=name
        self.price=price

class Pen(Pencil):

    def __init__(self, production):
        self.prod=production


p1=Pencil("Dollar SP_10", 65)
print(p1.color())
print(p1.purp())
print("The",p1.name,"Price is =>",p1.price)
        

                    # Super...............................
                    
                    
class Utencil:
    
    def __init__(self,type):
        self.type=type

    @staticmethod
    def color():
        print("Grey")

    @staticmethod
    def purp():
        print("For Writing")  
        
        
class Pen(Utencil):
    
    def __init__(self, name,type):
        self.name=name
        super().__init__(type)
        
                   
p1=Pen("Dollar Sp_10","Pen")
print(p1.type)
print(p1.name)



                    # Polymorphism...............................
                    
                    
                    
class Complex:
    
    def __init__(self, real, imagenry):
        self.real=real
        self.imagenry=imagenry
        
        
    def display(self):
        print(self.real,"i +", self.imagenry, "j")    
        
        
    def __add__(self, i2):
        newReal = self.real + i2.real
        newImg =  self.imagenry + i2.imagenry
        return Complex(newReal, newImg)
    
    
    def __sub__(self, i2):
        newReal = self.real - i2.real
        newImg =  self.imagenry - i2.imagenry
        return Complex(newReal, newImg)
    
    
    def __mul__(self, i2):
        newReal = self.real * i2.real
        newImg =  self.imagenry * i2.imagenry
        return Complex(newReal, newImg)
    
    
    def __mod__(self, i2):
        newReal = self.real % i2.real
        newImg =  self.imagenry % i2.imagenry
        return Complex(newReal, newImg)
            
        
i1 = Complex(4, 7)
i1.display()   

i2 = Complex(9, 17)
i2.display()     

# i3 = i1.add(i2)
i3 = i1 + i2
i3.display() 
 
i3 = i1 - i2
i3.display() 

i3 = i1 * i2
i3.display() 
      
i3 = i1 % i2
i3.display() 


                    # Problem...............................


class Circle:
    
    def __init__(self, radius):
        self.radius=radius
        
        
    def area(self):
       return (3.14 * (self.radius ** 2 )) 
         
    def parameter(self):
        return (2 * 3.14 * self.radius )   
    
c1 = Circle( 14 ) 
print(c1.area())   
print(c1.parameter())


                    # Problem...............................


class Employee:
    
    def __init__(self, role, depart, salary):
        self.role = role
        self.depart = depart
        self.salary = salary 
        
    def showdetails(self):
        print("Employee's role is =>",self.role)  
        print("Employee's department is =>",self.depart)
        print("Employee's salary is =>",self.salary)     
        
class Engineer(Employee):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "1,22,000")
        
Eng1 = Engineer("WAli", "19")
Eng1.showdetails()


                    # Problem...............................


class Order:
    
    def __init__(self, item, price):
        self.item = item
        self.price = price
        
        
    def __gt__(self, order2):
       return self.price > order2.price   
           
order1 = Order("Biscuits", "40")
order2 = Order("Lays", "70")          

print(order1 > order2)        