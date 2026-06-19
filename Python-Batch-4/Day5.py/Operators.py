'''
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

'''
# identity operators 

# is --- returns true if it finds the value  
# is not ---- returns true  if it doesn't find the value 

l = [1,2,3,4]
p= [1,2]
print(p is l) 


# membership operators 
# in ---- returns true if the value is present in  the sequence 
# not in ----returns true , if the value is not present 

names=["deepika", "digvijay", "sumit","gautum"]
print("sumit" in names)
print("sai" not in names)


for i in range(0,5): # start at 0 to n-1 (0,1,2,3,4)
    print(i)


# legal age 21 
# leagl for voting 18 
# AND

'''

#bit wise operators ---> deals with 0's and 1's

# Bit wise AND(&) : sets each bit to 1 , if both are 1 
# Bit wise OR(|) : sets each bit to 1 , if atlease one of the bit is 1 
# Bit wise XOR(^) : sets each bit to 1 , if only one of the bits is 1

#bit wise NOT (~) : changes 1---> 0 , 0---> 1  


a =10 
print(~a)

#bitwise left shift (<<) :left shifts by specified positions 
#bitwise right shift (>>) :right shifts by specified positions 


a =10 
print(a>>1)

print(bin(a))

a =10
print(a<<1)


a = 5
print(bin(a))
b = 3
print(bin(b))
print(a ^ b) # XOR same values --> 0 


a = 5 ---> 0101
b = 3 ---> 0011
        ---------
a&b =      0001
        ---------
a|b =   0111

print(a & b) # AND both of them should be 1 , then 1 

a = 5
b = 3
print(a | b) # OR atleast one is 1 , then 1


'''


'''
# operator precedence 

brackects ()
**

* , / ,// ,%
+ , -
<< , >>
& ---> bit wisw AND 
^ ---> Bitwisw XOR
| --->bitwise OR
== , != ,< , <= ,>,>=,is , is not


'''