#Gautam Assignment 11

# Section 1: ERRORS VS EXCEPTIONS
#------------------------------------------------

# 1. Identify Error Type

#Question:
#Write a program that intentionally produces:

# Syntax Error Example 

print("Hello")  

# Runtime Exceptions

try:
    result = 10 / 0   # ZeroDivisionError
except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero.")

try:
    print(x)   # NameError (x not defined)
    
except NameError:
    print("NameError: Variable not defined.")
    
    
#-----------------------------------------------------------------

# 2. Division Calculator with Exception Handling

# Question:
# Write a program that:

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a / b
   
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Invalid input. Please enter numbers only.")
    
#================================================================

# SECTION 2: try, except, else, finally

#================================================================

# 3. Number Validation Program

#Question:
#Take input from user and:

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input: Please enter a valid integer.")
else:
    print("Square:", num ** 2)
finally:
    print("Execution completed.")
    
#-----------------------------------------------------------------

# 4. File Reader with finally

# Question:
# Write a program to:

try:
    f = open("sample.txt", "r")
    print(f.read())
    
except FileNotFoundError:
    print("Error: File not found.")
    
finally:
    
    try:
        f.close()
        print("File closed.")
        
    except:
        print("No file to close.")
        
#-----------------------------------------------------------------

# 5. Multiple Exception Handling

# Question:
# Write a program that:

my_list = [10, 20, 30]

try:
    index = int(input("Enter index: "))
    print("Element:", my_list[index])
    
except IndexError:
    print("Error: Index out of range.")
    
except ValueError:
    print("Error: Invalid index input.")

#-----------------------------------------------------------------
    
# 6. ATM Withdrawal Simulation

# Question:
# Simulate ATM withdrawal:

balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))
    if amount > balance:
        raise Exception("Insufficient balance.")
    balance -= amount
    print("Withdrawal successful. Remaining balance:", balance)
    
except ValueError:
    print("Error: Invalid input.")
    
except Exception as e:
    print("Error:", e)
    
#-----------------------------------------------------------------

# 7. Login System with Limited Attempts

#Question:
#Create login system:

password = "admin123"
attempts = 0

while attempts < 3:
    user_input = input("Enter password: ")
    if user_input == password:
        print("Access granted.")
        break
   
    else:
        attempts += 1
        print("Incorrect password.")

else:
    raise Exception("Access denied after 3 failed attempts.")

#================================================================

## SECTION 3: CUSTOM EXCEPTIONS
#================================================================

# 8. Custom Age Validation Exception

# Question:
# Create custom exception:

class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")
    print("Access granted.")
    
except InvalidAgeError as e:
    print("InvalidAgeError:", e)
    
#-----------------------------------------------------------------

# 9. Custom Login Exception

# Question:
# Create custom exception:

class LoginError(Exception):
    pass

try:
    username = input("Enter username: ")
    if username != "admin":
        raise LoginError("Invalid username")
    print("Login successful.")
    
except LoginError as e:
    print("LoginError:", e)
    
#-----------------------------------------------------------------

# 10. Bank Minimum Balance Exception

# Question:
# Create custom exception:

class MinimumBalanceError(Exception):
    pass

balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))
    if balance - amount < 1000:
        raise MinimumBalanceError("Balance cannot go below 1000.")
    balance -= amount
    print("Withdrawal successful. Remaining balance:", balance)

except MinimumBalanceError as e:
    print("MinimumBalanceError:", e)
    
#-----------------------------------------------------------------

# 11. Negative Number Not Allowed

# Question:
# Create custom exception:

class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise NegativeNumberError("Negative numbers not allowed.")
    print("Number entered:", num)
    
except NegativeNumberError as e:
    print("NegativeNumberError:", e)
    
#-----------------------------------------------------------------

# 12. Student Marks Validation

# Question:
# Create custom exception:

class InvalidMarksError(Exception):
    pass

try:
    marks = int(input("Enter marks: "))
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")
    print("Valid marks.")
    
except InvalidMarksError as e:
    print("InvalidMarksError:", e)
    
#================================================================

# SECTION 4: INTERMEDIATE LOGIC-BASED EXCEPTION HANDLING

#================================================================

# 13. Nested Try-Except Block

# Question:
# Create program:

try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Division result:", result)

    try:
        val = int(input("Enter another number: "))
        print("Converted:", val)
        
    except ValueError:
        print("Inner Error: Invalid input.")
        
except ZeroDivisionError:
    print("Outer Error: Cannot divide by zero.")
    
#-----------------------------------------------------------------

# 14. Custom Exception with finally Block

# Question:
# Create custom exception:

class PasswordLengthError(Exception):
    pass

try:
    password = input("Enter password: ")
    if len(password) < 6:
        raise PasswordLengthError("Password must be at least 6 characters.")
    print("Password accepted.")
    
except PasswordLengthError as e:
    print("PasswordLengthError:", e)
    
finally:
    print("Validation process completed.")
    
#-----------------------------------------------------------------

# 15. Mini Project: Online Payment System

# Question:
# Simulate payment system:
    
class InvalidCardError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

balance = 10000

try:
    card = input("Enter card number: ")
    if len(card) != 16 or not card.isdigit():
        raise InvalidCardError("Card number must be 16 digits.")
    amount = input("Enter amount: ")
    
    if not amount.isdigit():
        raise InvalidAmountError("Amount must be numeric.")
    amount = int(amount)

    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance.")
    balance -= amount
    print("Payment successful.")
    
except InvalidCardError as e:
    print("InvalidCardError:", e)
    
except InvalidAmountError as e:
    print("InvalidAmountError:", e)
    
except InsufficientBalanceError as e:
    print("InsufficientBalanceError:", e)
    
finally:
    print("Transaction completed.")