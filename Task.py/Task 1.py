# Gautam Task 1
# -------------------------------------------------------

## 1. Program to Calculate Total Shopping Bill

# Problem Statement: Write a program to calculate the total bill amount for a customer. The program should take prices of three items as input and display the total amount.

item1 = int(input("Enter a item 1 price : "))
item2 = int(input("Enter a item 2 price : "))
item3 = int(input("Enter a item 3 price : "))

total = item1 + item2 +item3

print("Total bill amount : ",total)

# -------------------------------------------------------------

## 2. Program to Calculate Employee Salary with Bonus

# Problem Statement: Write a program to calculate the final salary of an employee by adding a 10% bonus to the base salary.

salary = int(input("Enter a Base Salary :"))
bonus = salary * 10/100
Total_Salary = salary + bonus
print("Final Salary by Adding 10% bonus : ",Total_Salary)

# -------------------------------------------------------------

# 3. Program to Check Even or Odd Number

# Problem Statement: Write a program to check whether a given number is even or odd.

num = int(input("Enter a Number : "))

if(num % 2 == 0):
    print("Number is Even.")
else:
    print("Number is Odd.")

# -------------------------------------------------------------

# 4. Program to Convert Temperature

# Problem Statement: Write a program to convert temperature from Celsius to Fahrenheit.

temp = int(input("Enter a temperature in celsius : "))

fahr = 9/5 * temp +32
print("Celsius to Fahrenheit Temp : ",fahr)

# -------------------------------------------------------------

# 5. Program to Swap Two Numbers

# Problem Statement: Write a program to swap two numbers entered by the user.

s = int(input("Enter a Number for s : "))
f = int(input("Enter a Number for f : "))

a , b = s, f
print("a : ",f, " b : ", s)

# -------------------------------------------------------------

# 6. Program to Find Largest of Three Numbers

# Problem Statement: Write a program to find the largest among three numbers.

a = int(input("Value for A : "))
b = int(input("Value for B : "))
c = int(input("Value for C : "))
if(a>b and a>c):
    print("A is Largest number : " ,a)
elif(b>a and b >c):
    print("B is Largest Number : ", b)
elif(c>a and c>b):
    print("C is Largest Number : ", c)
else:
    print("a, b , c are same",a,b,c)

# -------------------------------------------------------------

# 7. Program to Calculate Simple Interest

# Problem Statement: Write a program to calculate simple interest using the formula SI = (P × T × R) / 100.

P = int(input("Enter a P : "))
T = int(input("Enter a T : "))
R = int(input("Enter a R : "))

SI = (P*T*R)/100
print("Simple Interest : " , SI)

# -------------------------------------------------------------

# 8. Program to Convert Minutes to Hours and Minutes

# Problem Statement: Write a program to convert total minutes into hours and remaining minutes.

min = int(input("Enter a Min : "))

hr_res = min / 60
min_res = min % 60

print(f"{int(hr_res)} Hours {min_res} Minutes")

# -------------------------------------------------------------

# 9. Program to Check Voting Eligibility

# Problem Statement: Write a program to check whether a person is eligible to vote based on age.

age = int(input("Enter a age : "))

if age>= 18:
    print("Eligible")
else:
    print("Not Eligible")

# -------------------------------------------------------------

# 10. Program to Implement Grade System

# Problem Statement: Write a program to assign grades based on marks.

marks = int(input("Enter Marks : "))
if marks>=90:
    print("Grade A")
elif (marks >= 80):
    print("Grade B")
elif(marks>=70):
    print("Grade C ")
else:
    print("Fail")


