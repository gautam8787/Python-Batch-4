# Gautam Assignment 9

# ==================================================

# LAMBDA & HIGHER-ORDER FUNCTIONS ASSIGNMENT

# -----------------------------------------------------------------------

# SECTION 1: LAMBDA FUNCTIONS

# -------------------------------------------------------------

#  1. Basic Lambda Function

# Question: Create a lambda function to find the square of a number.

square = lambda x : print(x * x )

square(5)
square(8)


# -----------------------------------------------------------------------

# 2. Program to Calculate Employee Salary with Bonus

# Problem Statement: Write a program to calculate the final salary of an employee by adding a 10% bonus to the base salary.

base_sal = int(input("Enter a Base Salary :"))
final_Sal = base_sal + base_sal/10
print("Final Salary by Adding 10% bonus : ",final_Sal)

# -----------------------------------------------------------------------

## 3. Program to Check Even or Odd Number

# Problem Statement:  Write a program to check whether a given number is even or odd.

num = int(input("Enter a Number : "))

if(num % 2 == 0):
    print("Number is Even.")
else:
    print("Number is Odd.")
    
# -----------------------------------------------------------------------

## SECTION 2: HIGHER-ORDER FUNCTIONS
# (A higher-order function is a function that takes another function as an argument.)

# -----------------------------------------------------------------------

# 4. Function as Argument

# Question: Create a function apply_operation(func, a, b) It should take a function and two numbers.

def add (a , b):
    return a+b

def sub (a , b):
    return a - b

def apply_operation (func , a , b):
    return func(a,b)

add_res = apply_operation(lambda x, y: x + y,5,3)
print(add_res)

sub_res = apply_operation(lambda x, y: x - y,50,6)
print(sub_res)

# -----------------------------------------------------------------------

# 5. Returning a Function

# Question: Create a function multiplier(n) that returns a function to multiply any number by n.

def double (n):
    return(n*2)

def triple (n):
    return (n*3)

def multiplier(func , n):
    return func(n)

double_res = (multiplier(double , 5))
print(double_res)

triple_res = (multiplier(triple, 4))
print(triple_res)

# -----------------------------------------------------------------------

## SECTION 3: map()

# -----------------------------------------------------------------------

# 6. Square All Numbers Using map()

# Question: Given a list of numbers, use map() to return a list of squares.

numbers1 = [1, 2, 3, 4]
numbers2 = [5, 6, 7]

result1 = list(map(lambda l : l ** 2 ,numbers1 )) 
result2 = list(map(lambda l : l ** 2 ,numbers2 ))

print(result1)
print(result2)

# -----------------------------------------------------------------------

# 7. Convert Strings to Uppercase Using map()

# Question: Convert a list of names to uppercase using map().

input1 = ["sairam", "anjali", "rahul"]
input2 = ["python", "django"]

upper_case1 = list(map(lambda l : l.upper() , input1))
upper_case2 = list(map(lambda l : l.upper() , input2))

print(upper_case1)
print(upper_case2)

# -----------------------------------------------------------------------

## SECTION 4: filter()

# -----------------------------------------------------------------------

# 8. Filter Even Numbers

# Question: Use filter() to extract even numbers from a list.

input1 =  [1,2,3,4,5,6]
input2 =  [10,15,20,25]

result1 = list(filter (lambda l : l % 2 ==0 ,input1))
result2 = list(filter (lambda l : l % 2 ==0 ,input2))

print(result1)
print(result2)

# -----------------------------------------------------------------------

# 9. Filter Students with Passing Marks

# Question: Given a list of marks, filter students who scored 50 or above.

input1 = [45, 67, 80, 30, 55]
input2 = [90, 40, 49, 75]

result1 = list(filter(lambda l : l >= 50 , input1))
result2 = list(filter(lambda l : l >= 50 , input2))

print(result1)
print(result2)

# -----------------------------------------------------------------------

## SECTION 5: reduce()
# (Note: Import reduce from functools)

# -----------------------------------------------------------------------

# 10. Find Sum of List Using reduce()

# Question: Use reduce() to find sum of elements.

from functools import reduce

input1 = [1,2,3,4]
input2 = [5,5,5]

result1 = reduce(lambda a , b : a + b, input1)
result2 = reduce(lambda a , b : a + b, input2)

print("Sum of Numbers : ",result1)
print("Sum of Numbers : ",result2)

# -----------------------------------------------------------------------

# 11. Find Product of List Using reduce()

# Question: Use reduce() to find product of elements.

from functools import reduce

input1 = [1,2,3,4]
input2 = [2,3,5]

result1 = reduce(lambda a , b:a * b ,input1)
result2 = reduce(lambda a , b:a * b ,input2)

print(result1)
print(result2)

# -----------------------------------------------------------------------

# SECTION 6: PRACTICAL REAL-TIME EXAMPLES

# -----------------------------------------------------------------------

# 12. Apply 10% Discount Using map()

# Question: Given a list of prices, apply 10% discount to each price.

input1 = [100, 200, 300]
input2 = [500, 1000]

result1 = list(map(lambda l : l - (10/100) *l ,input1))
result2 = list(map(lambda l : l - (10/100) *l ,input2))

print(result1)
print(result2)

# -----------------------------------------------------------------------

# 13. Filter High Salary Employees

# Question: Given a list of salaries, filter salaries above 50,000.

input1 = [30000, 60000, 45000, 80000]
input2 = [55000, 40000, 75000]

result1 = list(filter(lambda l : l > 50000 , input1))
print(result1)

result2 = list(filter(lambda l : l > 50000 , input2))
print(result2)

# -----------------------------------------------------------------------

#  14. Calculate Total Bill Using reduce()

# Question: Given a list of item prices in cart, calculate total bill.

from functools import reduce

input1 = [250, 150, 100]
input2 = [999, 1]

result1 = reduce(lambda a , b : a + b , input1)
print(result1)

result2 = reduce(lambda a , b : a + b , input2)
print(result2)

# -----------------------------------------------------------------------

# 15. Combined Example (map + filter)

# Question: Given a list of numbers:

# First filter even numbers
input1 = [1,2,3,4,5,6]
input2 = [10,15,20]

filter_result1 = list(filter(lambda l : l % 2 == 0 , input1))
filter_result2 = list(filter(lambda l : l % 2 == 0 , input2))

# Then square them using map()
map_square1 = list(map(lambda l : l **2 , filter_result1))
map_square2 = list(map(lambda l : l **2 , filter_result2))

print(map_square1)
print(map_square2)
