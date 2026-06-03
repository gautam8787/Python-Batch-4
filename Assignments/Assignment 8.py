# Gautam Assignment 8

# ## SECTION 1: BUILT-IN VS USER-DEFINED FUNCTIONS
# =============================================================

# 1. Built-in Functions Practice

# **Question:**
# Write a program that takes a list of numbers and uses built-in functions to print

list = [10, 20, 5, 40]

print("Max : ",max(list))  #  Maximum value
print("Min : ",min(list))  #  Minimum value
print("Sum : ",sum(list))  #  Sum of elements
print("Len : ",len(list))  #  Length of the list

list1 = [3,3,3]

print("Max : ",max(list1))  #  Maximum value
print("Min : ",min(list1))  #  Minimum value
print("Sum : ",sum(list1))  #  Sum of elements
print("Len : ",len(list1))  #  Length of the list

# --------------------------------------------------------------------------------------------

# 2. User-Defined Max, Min, Sum (Without Built-ins)

# Question:
# Create a function with default role.

input1 = [4, 8, 1, 9]

def max(parameter):            # Maximum
    max_Value = parameter[0]
    for i in parameter :
        if max_Value < i :
            max_Value = i
    return max_Value
print("Maximum : ",max(input1))

def min(value):           # Minimum
    min_val = value[0]
    for i in value :
        if min_val > i :
            min_val = i
    return min_val
print("Minimum : ",min(input1))

def sum(value2):        # Sum
    sum1 = 0
    for i in value2:
        sum1 = sum1 +i
    return sum1
print("Sum : ",sum(input1))
    
input2 = [-5, -2, -10]

def max(para):             # Maximum
    max_Value = para[0]
    for i in para :
        if max_Value < i :
            max_Value = i
    return max_Value      
print("Maximum : ",max(input2))

def min(value1):          # Minimum
    min_val = value1[0]
    for i in value1 :
        if min_val > i :
            min_val = i
    return min_val
print("Minimum : ",min(input2))

def sum(value2):        # Sum
    sum1 = 0
    for i in value2:
        sum1 = sum1 +i
    return sum1

print("Sum : ",sum(input2))


# ## SECTION 2: PARAMETERS & ARGUMENTS
# =========================================================================================

#  3. greet(name)

# **Question:**
# Create a function greet(name) that prints a greeting message.

def greet(name):
    print(f"Hello {name}! Welcome to Python class.")

greet("Sairam")
greet("Anjali")

#---------------------------------------------------------------------------

# 4. calculate_total(price, quantity)

# Question:
# Create a function that returns total amount.

def cal_total(price , quantity):
    print(price * quantity)

cal_total(100,3)
cal_total(250,2)

# ----------------------------------------------------------------------------

# 5. create_account(name, role="User")

# **Question:**
# Create a function with default role.

def create_account(name , role = "user"):
    print(f"Account created for {name} with role {role}")


create_account("Rahul")
create_account("AdminUser","Admin")


# ## SECTION 3: RETURN VS PRINT
# ===========================================================================

# 6. Print vs Return (Square)

# **Question:**
# Create:

# Test Case 1:
def square(num):   # One function that prints square
    print(num**2)
square(5)

def squarereturn(num):  #  One function that returns square
    return num**2

res = squarereturn(5)
print(res * 10)

# Test Case 2:
def square(num):   # One function that prints square
    print(num**2)
square(3)

# -------------------------------------------------------------------

# 7. Function Chaining

# Question:
# Create two functions: add(a, b) and multiply(a, b).

def add(a,b):
    return (a + b)

def multiply(a , b):
    return a * b
      
# Call multiply using result of add.

print(multiply(add(2,3) ,4))
print(multiply(add(10,5),2))


# ## SECTION 4: LOGICAL THINKING WITH FUNCTIONS
# ===================================================================

# 8. Even & Odd Counter

# Question:
# Write a function that returns count of even and odd numbers.

def Even_Odd(value):
    Even_count = 0
    Odd_count = 0
    for i in value:
        if i % 2 == 0:
            Even_count += 1
        else :
            Odd_count += 1

    print("Even no :", Even_count)        
    print("Odd No : ", Odd_count)
    
Even_Odd([1,2,3,4,5])
Even_Odd([2,4,6])

# ----------------------------------------------------------

# 9. Palindrome Checker

# Question:
# Create function is_palindrome(word).

def palindrome(spell):
    if(spell == spell[::-1]):
        return True
    else :
        return False
print(palindrome("madam"))
print(palindrome("python"))

