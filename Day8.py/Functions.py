'''
# what is a FUNCTION ?? 
# is a block of code that performs a specific task.
# once a function is defined then we can use it multiple times 
# if you want to use that function then we have to call it.

# why functions ??
# reduce repitative code
# code readabilty 

# where we can use this functions concept ??
# 

print("hello") #--->calling function


# def function_name(): function definition 
    #block of code 
    #block of code 
    #block of code 
    #block of code 

# function_name() ---> function calling

def is_even(): # user defined function
    num = 20
    if num % 2==0:
        print("even")
    else: 
        print("odd")

is_even()


# In built functions  ---> print() , len() , type() , int() ,float() , set() , input() , list() , max(), min(),

# parameters ?? ---> variables in a function   num = 21
# arguments  ?? ---> actual value 

# parameters are used for dynamic programming --> 

def add(a,b): # parameters 
    c=a+b
    print(c)

add(999,787) # arguments 
add(99,78) # arguments 
add(9,7) # arguments 

def login(user_name,pswd):
    if user_name == "admin":
        if pswd == "1234":
            print("login success")
        else:
            print("wrong password")
    else:
        print("user_name not matched")

# login("sairam" ,"1235")

login("admin" ,1234)

# any function should return something (value , function , file , path , anything)
# return ---> keyword 


def is_even(): # user defined function
    num = 20
    if num % 2==0:
        print("even")
    else: 
        print("odd")

print(is_even())   #----> None


def is_even(num): # user defined function
    if num % 2==0:
        return "even number"
    else: 
        return "odd number"

print(is_even(20))


'''

# prime number 

# a num which is only divided by 1 and itself --->> every number is prime number ?? 

# 99 --> 99 , 1 ---> only 2 factors 

# 2 , 3 , 5, 7, 11 , 13 , 17, 19 , 23 , 29,31

# 5 --> 1, 5 ( 2 factors)


# 5 % 2==0 ?? (3rd factor)
# 5 % 3==0 ??
# 5 % 4==0 ??


def is_prime(num):
    if num <=1:
        return "number should be greater than 1"
    else :
        for i in range(2,num): #2,3,4,5,6,7,8
            if num % i == 0:
                return "not prime"
                
        return "prime number"

print(is_prime(18))




# reverse of a number

# input 1234 --- output 4321
'''
num = 1234

1234 % 10 = 4 = digit
123%10 = 3
12%10 = 2
1 %10 = 1

reverse = 0 * 10 + digit

num // 10 = 

4321
1234/10 = 123.4

'''

num = 0
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print(rev)


def reverse(num):
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    return rev

print(reverse(4687))

