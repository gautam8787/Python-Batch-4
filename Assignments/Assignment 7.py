# Gautam Assignment 7

# -------------------------------------------------------

## 1.Write a program to print numbers from 1 to N using a loop.
##   (N is given by the user)


user = int (input("Enter a Number : "))
for i in range (1,user+1):
    print(i)

   
# 2.Write a program to find the sum of all even numbers between 1 and N using a loop.

n = int(input("Enter a Number : "))
total = 0

for i in range (1,n+1):
    if i % 2 == 0 :
        total = i + total 

print(total)


# 3.Write a program to reverse a given number using a loop.
# Example: Input → 1234, Output → 4321

number = int(input("Enter a Number : "))

reverse = 0
while number > 0:
    dig = number % 10
    reverse = reverse *10 +dig
    number = number // 10
print(reverse)


# 4.Write a program to count the number of digits in a given number using a loop.

number = int(input("Enter a Number : "))
count = 0 
while number > 0:
    number = number// 10
    count += 1
print(count)


"""
5.Write a program to generate the multiplication table of a given number up to 10.
expected output : 
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
.
.
.
5 * 10 = 50
"""


number = int(input("Enter a Number : "))

for i in range(1,11):
    print(f"{ number } * { i } = {number*i}")
    

"""
6.Write a program to print a square pattern of stars of size N:

****
****       
****
****

and 

* * * *
* * * *       
* * * *
* * * *
"""


number = int(input("Enter a Number : "))
for i in range (1,number+1):
    print("*"*number)
print("---------------------------------")
for j in range(0 , number):
    print(" * "*number)
    
   
"""
7.Write a python program to print a complete diamond shape using stars (*) with nested loops.

    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""
row = int (input("Enter a Number : "))
for i in range (1, row+1 ,+1):
    for j in range (row-i):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    print()

for i in range (row-1,0,-1):
    for j in range(row-i):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    print()
    
"""
8.Write a python program to display this table using nested loops.
1 2 3 4 5 
6 7 8 9 10 
11 12 13 14 15
16 17 18 19 20
"""


number = 1
for i in range(0,4):
    for j in range (5):
        print(number,end=" ")
        number +=1
    print()

