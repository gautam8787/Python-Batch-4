# Gautam Task 2

# -------------------------------------------------------

# 21. Program to Calculate Factorial of a Number

# Problem Statement: Write a program to calculate the factorial of a given number using a loop.

num = int(input("Enter a Number : "))
count = 1

if num ==  0 or num == 1:
    print("1")
    
else:
    for i in range(2,num+1):
        count *= i

    print(count)
    
# -------------------------------------------------------

# 22. Program to Generate Multiplication Table

# Problem Statement: Write a program to generate the multiplication table of a given number up to 10.

num = int(input("Enter Number : "))

for i in range(1,11):
    print(f"{num}*{i} : {num* i}")
    
# -------------------------------------------------------

# 23. Program to Reverse a Number

# Problem Statement: Write a program to reverse the digits of a number.

num = int(input("Enter a Number : "))

while num != 0:
    digit = num % 10
    new = digit
    num = num // 10
    print(new, end="")
    
# -------------------------------------------------------

# 24. Program to Count Digits in a Number

# Problem Statement: Write a program to count the number of digits in a given number.


num = int(input("Enter Number : "))
count = 0

if num == 0 :
    print("1")
    
else:
    while num != 0:
        num = num // 10
        count += 1
    print(count)
    
# -------------------------------------------------------

# 25. Program to Generate Fibonacci Series

# Problem Statement: Write a program to generate Fibonacci series up to N terms.

num  = int(input("Enter Number : "))

a , b = 0,1

for i in range (a,num):
    print(a, end = " ")
    c = a+ b
    a = b
    b = c
    
# -------------------------------------------------------

# 26. Program to Check Prime Number

# Problem Statement: Write a program to check whether a given number is prime.

num = int(input("Enter a Number : "))

if (num <= 1 ):
    print("Not Prime")
    
else:
    for i in range(2,num):
        
        if(num % i == 0):
            print("Not Prime.")
            break
        
    else:
        print("Prime Number")
        
# -------------------------------------------------------

# 27. Program to Print Prime Numbers in a Range

# Problem Statement: Write a program to print all prime numbers between two given numbers.

number_1 = int(input("Enter Number : "))
number_2 = int(input("Enter Number : "))
prime = []

for i in range (number_1 , number_2 + 1):
    if i > 1 : 
        for j in range(2 , i):
            if (i % j == 0 ):
             break
        else:
            prime.append(i)
print(prime)
    
# -------------------------------------------------------

# 28. Program to Find Sum of Digits

# Problem Statement: Write a program to calculate the sum of digits of a number.

num = int(input("Enter a Number : "))
sum = 0

while(num != 0):
    dig = num % 10 
    sum = sum + dig  
    num = num // 10 

print(sum)

# -------------------------------------------------------

# 29. Program to Print Star Pattern

# Problem Statement: Write a program to print the following pattern based on given number of rows.

num = int(input("Enter row : "))

for i in range(1, num+1):
    print("*"*i)
    
# -------------------------------------------------------

# 30. Program to Reverse a String using Loop

# Problem Statement: Write a program to reverse a given string without using built-in reverse functions.

str = input("Enter a String : ")

print(str[::-1])

