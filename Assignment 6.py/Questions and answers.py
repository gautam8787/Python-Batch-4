#  1.Write a program to print numbers from 1 to 10 using a for loop.

for i in range(1,11):
    print(i)


# 2.Write a program to print even numbers between 1 and 50 using a loop.

for i in range(1,51):
    if i%2==0:
        print(i)     
        
        
# 3.Write a program to calculate the sum of first N natural numbers using a while loop.

n = int(input("Enter a Number : "))
total = 0
i = 1
while i <= n:
    total = total + i
    i = i + 1

print(f"Sum of {n} natural number is : {total}")


# 4.Write a program to display the multiplication table of a given number using a for loop.


n = int(input("Enter a Number :"))
j = 10
for i in range(1 , j +1):
    print(f" { n } * { i } : {i*n}")

# 5.Write a program to count the number of digits in a given number using a loop.


number = int(input("Enter a Number : "))
count = 0
if number == 0:
    count= 1
else:
    for i in number , 0:
        number = number//10
        count = count + 1
print("Count of number : ",count)

# 6.Write a program to reverse a number using a while loop.


num = 4321
i = 0
while num > 0:
    digit = num % 10       
    i = i * 10 + digit 
    num = num // 10 
print("Reverse no is : ",num)

# 7.Write a program to print the following pattern using nested loops:
'''
*
* *
* * *
* * * *
* * * * *
'''


for i in range(1,6):
    print(" * "*i)

# 8.Write a program to check whether a given number is a prime number using loops.


n = int(input("Enter a Number : "))
if n <=1 :
    print("Not Prime")
else :
    for i in range(2, n):
        if n % i == 0 :
         print("Not Prime ")
         break
    else:
        print("Number is Prime")

# 9.Write a program to demonstrate the use of break and continue statements with a loop.


n = int(input("Enter a Number : "))
i = 1
while i <= n:
    if i == 5:
        break
    print(i)
    i += 1
print("------------------------")

k = int (input("Enter a Number : "))
while i <= k:
    if i == 10 :
        i += 1
        continue
    print(i)
    i +=1

# 10.Write a program to find the factorial of a given number using a loop.

n = int(input("Enter a Number : "))
total = 1
for i in range(1,n+1):
    total = i * total
print(total)