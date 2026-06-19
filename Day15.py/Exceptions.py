# Exception handling in python 

# Errors ---> which are made by programmer

# logical errors 
# syntax errors 
# complietime errors 

# Runtime errors ---> mistakes made by the user ---> exceptions handling   

'''
age = int(input("enter your age : "))
after10 = age + 10
print(after10)


a=10
b=5
try:
    res=a/b
    print(res)

except Exception as e:
    print("zero division error",e)

print("end of the program")


'''
# try block  ---> logic where there is a chance of getting an error 
# except block ---> leave it as an exception 

'''
a=int(input("enter a value : "))
b=int(input("enter b value : "))
res=a/b
print(res)

'''

try:
    a=int(input("enter a value : "))
    b=int(input("enter b value : "))
    res=a/b
    print(res)

except ZeroDivisionError as zde:
    print(zde)

except ValueError as ve:
    print(ve)

except Exception as y:
    print("unexpected error",y)

finally:
    print("end of the program")


