# Encapsulation in python : wrapping up data(variables) and methods in a single unit called class and restricting direct access 
# means Data Hiding --> we protect some important from direct modification 


# why ?? 
# data security 
# controlled access : allows access only through methods 
# prevent accidental changes : others can not modify important data directly 

# Access specifiers 
'''

# public access specifiers  : 

class Parent:
    publicdata = "Sairam"
    def publicmethod(self):
        print(self.publicdata)

class Child(Parent):
    def method(self):
        print(self.publicdata)

obj=Parent()
print(obj.publicdata)
obj.publicmethod()

obj1=Child()
obj1.method()
print(obj1.publicdata)
'''

# protected access specifiers : put (_)underscore before data and method to declare it as protected access sepcifiers  
# they can be access only by the superclass and subclass (subclass which is derived from the superclass) 
'''
class Parent:   # super class
    _protecteddata = "Sairam"
    def protectedmethod(self):
        print(self._protecteddata)

class Child(Parent):   # subclass 0r derived class
    def method(self):
        print(self._protecteddata)


class Sample(Child):   # normal 
    def display(self):
        print()
        print(self._protecteddata)

obj=Parent()
print(obj._protecteddata)
obj.protectedmethod()

obj1=Child()
obj1.method()
print(obj1._protecteddata)

obj2=Sample()
obj2.display()
print(obj2._protecteddata)
obj2.method()    #

'''
# private access specifiers : data can be accessed by only the superclass 
# (__) double underscore 
#if you want to access private data then you can only access through methods of super class  
# we can not access the private data through objects 


class Parent:   # super class
    __privatedata = "Sairam"
    def privatemethod(self):
        print(self.__privatedata)

class Child(Parent):   # subclass 0r derived class
    def method(self):
        print(self.__privatedata)


obj=Parent()
obj.privatemethod()
# print(obj.__privatedata)

obj1=Child()
obj1.method()

