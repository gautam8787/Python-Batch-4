# Abstraction in Python :

# hiding internal implementation details and 
# show only the essential features to user

# ATM machine ---> user can see only options   
 
# to implement abstraction ,we should have Abstract classes and abstract methods 

# Abstract class : a class which contains one or more abstract methods 
# abstract method : a method is declared without implimentation 

'''
class A:               # abstract class 
    def method(self):  # abstract method 
        pass

obj=A()     
obj.method() 


from abc import ABC , abstractmethod

class A(ABC):                # abstract class 
    @abstractmethod  
    def method(self):  # abstract method 
        pass

obj = A()
obj.method() 
'''
# concreate method : normal method in a abstract class 

from abc import ABC , abstractmethod

class A(ABC):                # abstract class 
    @abstractmethod  
    def method(self):        # abstract method 
        pass
    
    def sample(self):
        print("this is concrete method")
    
    @abstractmethod  
    def method2(self):        # abstract method 
        pass


class B(A):

    def method(self):
        print("this is method implemented in B class")

    def method2(self):        
        print("this is methood2 implemented by B class")


obj = B()
obj.method() 
obj.sample()
obj.method2()


# libraries ---->packages(folders) ---> modules(files)--->classes---> methods and attributes-->attributes(logic)

