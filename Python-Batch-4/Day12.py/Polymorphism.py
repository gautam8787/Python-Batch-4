# polymorphism in python  : one thing behaving in multile forms 
# it is a greek work 

# ploy --> many 
# morphs--> forms 

# polymorphism : same method / function / operator behaves differently based on object , data type or class

# code flexibity 
# resuability
# clean code 

# print() --> 
print()
print(10)
print(10+20)
print(10,"sairam",99.00, True)

k=[1,2,3,4,5,6,7,8]
print(len(k))
print(len("sairam"))

# operator overloading : one operator behaving differently for different datatypes 

# "+"
print(100+99) # + ---> addition operator 
print("sairam"+" is a superman") # concatination operator 

k=[1,2,3,4,5,6,7,8]
l =[99,88,77]   
print(k+l) # joins 

#  " * "
 
print(10*2) # multiplication operator 

print("sai " * 3) # repetation 
 
# *args ---> multiple parameters (packing and unpacking arguments)

# if a function handles more than one datatype or different parameter size, then it is also called as ploymorphism 

def sample(*a):
    print(a)

sample(10,30,40,67)


# method overloading 

class A:
    def demo(self):
        print("class A method")

class B:
    def demo(self):
        print("class B method")

class C:
    def demo(self):
        print("class C method")

def poly(obj):
    obj.demo()

obj1=A()
obj2=B()
obj3=C()

poly(obj1)
poly(obj2)

# method overriding :  subclass methods overrided by parent class methods 

class parent:
    def method1(self,name):
        print(name)
        print("this is parent class method")

    def display(self):
        print("this is parent class method")

class child(parent):
    def method1(self,salary):
        print(salary)
        print("this is child  class method")

c= child()
c.method1("sairam")
c.method1(70000)
c.display()

