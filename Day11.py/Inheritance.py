# Inheritance  : ability to use methods and attributes from one class to anthother class 
#  ability to use methods and attributes in a newly created class from already existing class 

# Single inheritance 
class A:
    def sample(self):
        print("class A")


class B(A):
    def demo(self):
        print("class B")

obj =B()
obj.demo()

obj.sample()

o1=A()
o1.sample()
# o1.demo() ---> can not access 



class parent:
    def method1(self):
        print("this is parent class method")

    def display(self):
        print("this is parent class method")

class child(parent):
    def method2(self):
        print("this is child  class method")

c= child()
c.method1()
c.display()
c.method2()

# Multiple inheritance  : a child class inheriting the properties of two or more parent classes 


class Father:
    def method1(self):
        print("this is parent class method")

    def display(self):
        print("this is father display class method")

class Mother:
    def method2(self):
        print("this is parent class method")

    def display(self):
        print("this is mother display class method")

class child1(Father,Mother):
    def method3(self):
        print("this is child  class method")


c1= child1()
c1.method1()
c1.display()   
c1.method2()
c1.method3()


# Multi level inheritance : grandfather <----Father class<----child1 class 

class GrandFather:
    def method1(self):
        print("this is parent class method")

    def display(self):
        print("this is grandfather display class method")

class Father1(GrandFather):
    def method2(self):
        print("this is parent class method")

    def display(self):
        print("this is father display class method")

class child11(Father1):
    def method3(self):
        print("this is child  class method")


c11= child11()
c11.method1()
c11.display()   
#c11.method2()
c11.method3()


# Hierarical inheritance

class parent12:
    def method11(self):
        print("this is parents class")

class child12(parent12):
    def method12(self):
        print("this is parents class")

class child13(parent12):
    def method13(self):
        print("this is parents class")

# hybrid inheritance ---> combination of more that one type of inheritance 