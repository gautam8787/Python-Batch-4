# Gautam Task 2

# -------------------------------------------------------

# 11. Program to Check Divisibility by 3 and 5

# Problem Statement: Write a program to check whether a number is divisible by both 3 and 5.

num1 = int(input("Enter a Number : "))

if(num1%3 == 0 and num1 % 5 == 0):
    print("Number is Divisible by 3 and 5")
    
else:
    print("Not Divisible both")
    
# -------------------------------------------------------

# 12. Program to Validate Login Credentials

# Problem Statement: Write a program to validate a username and password

user_name = input("Enter a User Name : ")
password = input("Enter a Password : ")

if(user_name == "admin" and password == "1234"):
    print("Login Successful.")
    
else:
    print("Invalid Credentials")
    
# -------------------------------------------------------

# 13. Program to Check Leap Year

# Problem Statement: Write a program to check whether a given year is a leap year.

year = int(input("Enter a year : "))

if(year% 2 == 0):
    print("Leap Year")
    
else:
    print("Not Leap Year")
    
# -------------------------------------------------------

# 14. Program to Simulate ATM Withdrawal

# Problem Statement: Write a program to simulate ATM withdrawal. 

balance_money = int(input("Enter a Balance : "))
withdrawal_money = int(input("Enter a Withdrawal amount : "))

if (balance_money >= withdrawal_money):
    print("Transaction Successful.")
    
else :
    print("Insufficient Balance")
    
# -------------------------------------------------------

# 15. Program to Check Palindrome Number

# Problem Statement: Write a program to check whether a number is a palindrome.

number = int(input("Enter a Number : "))
original_value = number

reverse = 0
while number > 0 :
    digit = number % 10
    reverse = reverse *10 + digit
    number = number // 10
    
if original_value == reverse :
    print("Palindrome")
    
else:
    print("Not Palindrome")
    
# -------------------------------------------------------

# 16. Program to Identify Vowel or Consonant

# Problem Statement: Write a program to check whether a character is a vowel or consonant.

a = input("Enter a input : ")
list1 = ["a","e","i","o","u"] 
list2 = ["A","E","I","O","U"]

if(a in list1 or a in list2):
    print("Vowel")
    
else:
    print("Consonant")
    
# -------------------------------------------------------

# 17. Program to Calculate Electricity Bill

# Problem Statement: Write a program to calculate electricity bill 

units = int(input("Enter a Units : "))

if(units < 100):
    print("Low Bill ")
    
elif(units> 100 and units < 200):
    print("Medium Bill")
    
elif(units > 200):
    print("High Bill")
    
# -------------------------------------------------------

# 18. Program to Apply Discount

# Problem Statement: Write a program to apply discount based on purchase amount.

amount_money = int(input("Enter a Amount : "))

if(amount_money > 1000):
    amount_money = amount_money - (amount_money / 10)
    print("10% Discount")
    
elif(amount_money< 1000 and amount_money > 500):
    print("5% Discount")
    
elif(amount_money<500):
    print("No Discount")
    
# -------------------------------------------------------

# 19. Program to Print Numbers from 1 to N

# Problem Statement: Write a program to print numbers from 1 to N using a loop.

number = int(input("Enter a Number : "))

for i in range(1,number+1):
    print(i)
    
# -------------------------------------------------------

# 20. Program to Find Sum of First N Numbers

# Problem Statement: Write a program to calculate the sum of first N

count = 0
num = int(input("Enter a Number : "))

for i in range(1,num+1):
    count += i
    
print(count)
