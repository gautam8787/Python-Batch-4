#Day 4
#==================


# Operators in python  ---> operators are symbols used to perform specific task on variables / values 


# types of operators 

# Arithemetic operators   ---> + ,-,*,
# /  --> division  --> quocient 
# % --- > modulas   ---> remainder 
# ** --> power  
# // --> floor division  ---> quocient floor value --> value before the decimal point 

a=10
print(a%2)  # rem=0
print(a/2)  # q = 5.0  ---> division operators always gives float value as output 
print(a/3)  # 3.933...
print(a//3) # 3

print(3**2) # ---> 9


# Relational (comparision ) operators 

# == , != , > , < >= ,<=


x=100
y = 99

print(x==y) #  False
print(x!=y) #  True
print(x>y) # True

print(x<y) #  False
print(x>=y) # True
print(x<=y) # False


# Logical operators ---> checks the condition and gives boolean output 
# and ---> both conditions should be true ---> True or else False 
# or  ---> at least oen condition is true ---> True or else False 
# not ---> if True it give False , if False it gives True 


age = 30
print(age > 18 and age <= 30)

age = 36
print(age < 35 or age > 40)

# assignment operators 

# = , += ,-= ,*= ,/= , %= ,**= ,//=

a=20
a+=10  # 20 +10 = 30 --> a
# a = a + 10
a-=10 # 20 
a-=10
print(a)

