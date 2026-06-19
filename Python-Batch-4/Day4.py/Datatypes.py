'''
# Datatypes 

# A datatypes means what kind of value a variable is holding and what operations it can perform . 

# numeric datatypes : int , float , complex (numbers)
# intergers : like whole numbers (+ve or 0 or _ve )
# float : decimal numbers 
# complex : 3+4j (imaginary numbers)

a="python"
# sequence datatype : string , list , tuple, range

# string : all the text (group of characters) ' ' or " " or ''' '''
# supporst indexes 
# mutable 


# list : ordered collection of data 
        # list is declared inside []
        # in this list u can have string , nuumeric 
        # allows duplicates
        # mutable means it can be changed (it will not create new objects) 
        # indexes 

name="sairam"
name="navven"

l=[1,2,3,4,5,5,"sairam",99.9]
print(l)
print(type(l))
print(l[0])
print(l[4])
print(l[-1])

# tuple : ordered collection of data 
        # immutable (new objects are created)(can not change)
        #allows duplictes 
        # indexes

t=("sairam", 'keerthi','python', 66,7674.86)
print(t)
print(type(t))

# range :  supports indexes 

# range(start, stop , step)

# default start value : 0
# default stop value : end of the range (n-1)
# default step value : 1

# for i in range(0,5):
        
# boolen data type : True or False 

# Dictionary : stores the values in form of key value pairs  (mapping datatype)
# ordered 
# mutable
# keys unique 
# {}

d={"trainer":"sairam","trainee":"keerthi","course":"python"}
print(d)

# set : unordered collection  of data 
# {} 
# not duplictes 
# mutable 
# no index 
s={1,1,2,2,3,4,3,4,45,5,6,6}
print(s)

# collection datatypes ?? 
# # list : [] , ordered , mutable, allows duplicates, mixed datatypes , indexes 
# append()
l=[1,2,3,4,5,5,"sairam",99.9]
# # tuple : () ordered , immutable, allows duplicates, mixed datatypes , indexes 
# # set : {} unordered , mutable, no duplicates, mixed datatypes , no indexes
# # dictionary : {"key:value"}  ordered , mutable, allows duplicates,keys unique, mixed datatypes


# nested list  : list inside the list 
l1=[[1,2,3,4],[4,5,6,7],[8,9,0]]
print(l1)

print(l1[0][0])
print(l1[0][1])
print(l1[0][2])


# git clone "http link"

s={1,1,2,2,3,4,3,4,45,5,6,6}
print(s)


l=[1,2,3,4,5,5,"sairam",99.9,99.9]
print(set(l))

'''
# Datatypes in python 

# what is a datatype ?? 
# what kind of data a variable is holding and what operations have to performed on that variable. 

a=100  # ---> numeric datatype 
b= "sai"   #---> sequence datatype 
# res= a + b 
# print(res)


# types to datatypes 
# Numeric datatype  ----> mathematical operations 
        # intergers ---> 0 , +ve , -ve 
        # float  ---> value with decimal points , 10.99 , 99977.876854 
        # complex ---> imaginary numbers (a+jb , 3+4j , 8-7j)

# sequence datatype 
# string  ---> group of characters 
name = "sairam" , "shiva"  # ('sairam', 'shiva')
print(name)

# print(name[0])
# print(name[1])
# print(name[-1])

# indexing ---> +ve index  ---> starts from 0 to n-1 (n is lenght of the string)
# -ve index ---> -1 to end the string 


# list  ---> 
# tuple  ---> () 
# range --->

# collection datatypes ---> multiple value as a collection 
 
# list  ---> [] ---> square brackets  
# multiple values of different datatypes 
# mutable sequence 
# it can be changed 
# ordered collection of data 
# allows duplicate values 


names = [["keerthi", "sairam", "naveen"], ["sumit", 98] ,[100 , 67 , 99796.9877]]
print(names)

print(names[0][0])


# list methods 
print(names.append(7777))
print(names)

#print(names.remove(98))
print(names)

print(names.append(7777))
print(names)


# tuple 
# --->() ---> multiple values 
# ordered collection 
# immutable 
# allows duplicates 
# faster than ist 


t=("keerthi", "sairam", "naveen", "sumit", 98, 100 , 67 , 99796.9877)
print(t)


# nested list 

#names = [["keerthi", "sairam", "naveen"], ["sumit", 98] ,[100 , 67 , 99796.9877]]
#print(names)


print(names[0][0])



# set ---> {}
# unordered collection data
# uniques elements 
# not allow duplictes 

s={101 , 102 , 103 , 101 ,102}
print(s)


y=[1,1,1,3,4,5,6,5,4,5,4,5,5,5,5]
print(type(y))

print(type(set(y)))


# dictionary  --> stores the data in the form of key-value pair 

# key-value pair -------> "name"="sairam" ,"age" = 29

dict={"id":101 , "name":"sairam" ,"age" : 29}
print(dict)

