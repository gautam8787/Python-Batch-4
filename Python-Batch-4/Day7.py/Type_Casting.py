# Type casting

# it is also called as implicit type conversion 
# happenes when python automatically converts one data type to another during an operation 

'''  
#example :

a=10 
b=99.9
sum=a+b
print(type(sum),sum)

print()

x=True #(1)
y=10
z=x+y
print(type(z),z)

x=False #(0)
y=10
z=x+y
print(type(z),z)

print()

x=10
y=20.0
z=x*y
print(type(z),z)
print()


# Type conversion 

# also called as Explicit conversion 
# developer manually converts the data types 

#int() ----> converts to interger 
#float()--->coverts to float value  
#str() ----> converts to string 
#list()--->coverts to list 
#tuple()---> to tuple 
#set() ---> to set 



# example 

#age=input("enter the age : ")
#age = int(age)
#print(age + 10)


price=99.99
price=int(price)
print(price) # here decimal part is removed not rounded 

lst=[10,10,10,20,20,30,30,40,50]
unique_values=set(lst)
print(type(unique_values),unique_values)



s={40, 10, 50, 20, 30}
print(list(s))

s={50, 40, 30, 20, 10}
print(list(s))
'''
