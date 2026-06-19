# OOPS concepts :

# Object Oriented Programming System

# paradigms ??? approach / style / way

# procedural approach ?? step by step approach  ( c lang )
# functional approach  ?? pure functions  
# object oriented approach ?? using objects 


# Object ?? ---> is a by product /instance of a class  
# Class --- > design / blue print for creating objects 

#object ---> properties and bevaviour  

# pen 
# properties ---> color , material , size , brand , design 
# behavior / functionally --> used to write , used to read 


# variables / parameters  ---> attributes ---> properties 
# functions ---> methods -->  behaviour


# class Classname:   # attributes and methods (parameters and functions ) ---> class definition 
    #pass 

# obj = Classname() # creating object


class Employee:
    name = "Rocky123"
    salary = 50000


obj = Employee()
print(obj.name)
print(obj.salary)


obj2 = Employee()
obj2.name ="sairam"
print(obj2.name)
print(obj2.salary)


obj1 = Employee()
print(obj1.name)
print(obj1.salary)

class Student:
    name = "deepika"
    roll_no = 501
    marks = 99

    def function1(self):
        name = "saiarm"
        roll_no = 502
        marks = 100
        print("congrats",name)
        print(roll_no)
        print(marks)

'''    
s1 = Student()
print(s1.name) # ojects can access attributes of the class 
print(s1.name)
print(s1.function1)  # object can access medthos of the class 

# print(Student.name) # access using class name 

s2 = Student()
s2.name="sumit"
print(s2.name)
'''
s3 = Student()
print(s3.name)
s3.function1()


class Sample:
    names= "pawan kalyan"
    def sampleFunction(self):
        name = "chiru"
        print(name)
        print("self demo")

obji = Sample()
obji.names = "monalisa"
print(obji.names)
obji.sampleFunction()


def sampleMethod():
    print("with out self ")

sampleMethod()


# constructor (__init__) : a function which is called automatically while creating objects 
# this __init__ method is used to store the initial attributes in an object 
# constructor will intialize the attributes 

'''
syntax :

class ConstructorClass:

    def __init__(self,paramter1 , parameter2 ):
        self.parameter1= paramter1
        self.parameter2= parameter2

obj = ConstructorClass()

'''

# ac_no , ac_name , ifsccode , balance

class BankAccount:

    def __init__(self , ac_no , ac_name , ifscocode , balance):
        self.ac_no = ac_no
        self.ac_name = ac_name
        self.ifsccode = ifscocode
        self.balance = balance

    def AcBalance(self):
        print(self.ac_name ,"Your account balance is :", self.balance)

    
    def deposite(self ,amount):
        self.balance += amount

    
    def withdraw(self , amount):
        if amount <= self.balance:
            self.balance-= amount
        else:
            print("insufficient balance")

sairam = BankAccount(101011202099 , "sairam", "BNK1020" , 50000)
sairam.AcBalance()

rocky = BankAccount(101011202098 , "Rocky", "BNK1020" , 100000)
rocky.AcBalance()
rocky.deposite(10000)
rocky.AcBalance()

deepika = BankAccount(101011202097 , "Deepika", "BNK1020" , 70000)
deepika.withdraw(30000)
deepika.AcBalance()


