#Gautam Assignment 4

#===========================================================================================================

#1.Write a program to demonstrate all arithmetic operators using two user-defined numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)            # Normal division
print("Floor Division:", a // b)     # Division without decimal part
print("Modulus:", a % b)             # Remainder
print("Exponentiation:", a ** b)     # Power (a raised to b)


#===========================================================================================================

#2.Write a program to compare two numbers using relational operators and display the result.

a = int(input("Enter first number: ")) 
b = int(input("Enter second number: "))

print("a == b:", a == b)   # Equal
print("a != b:", a != b)   # Not equal
print("a > b:", a > b)     # Greater than
print("a < b:", a < b)     # Less than
print("a >= b:", a >= b)   # Greater than or equal
print("a <= b:", a <= b)   # Less than or equal


#===========================================================================================================

#3.Explain logical operators (and, or, not) with a truth table and a sample program.

x = True
y = False

print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)


#===========================================================================================================

#4.Write a program to check whether a number lies between 10 and 50 using logical operators.

num = int(input("Enter a number: "))

if num >= 10 and num <= 50:
     print("The number lies between 10 and 50")
else:
     print("The number is outside the range")


#===========================================================================================================

#5.Demonstrate the use of assignment operators (=, +=, -=, *=, /=) with examples.

x = 10        # =
x += 5        # x = x + 5
x -= 3        # x = x - 3
x *= 2        # x = x * 2
x /= 4        # x = x / 4

print("Final value of x:", x)


#===========================================================================================================

#6.Write a program to check whether a given value exists in a list using membership operators.

numbers = [1, 2, 3, 4, 5]
val = int(input("Enter a value: "))

if val in numbers:
     print(val, "exists in the list")
else:
     print(val, "does not exist in the list")


#===========================================================================================================

#7.What is the difference between == and is operators?
#  Write a program to prove it.

# == → checks value equality.
# is → checks object identity (whether both refer to the same memory location).

a = [1, 2, 3]
b = [1, 2, 3]

print("a == b:", a == b)   # True 
print("a is b:", a is b)   # False 

c = a
print("a is c:", a is c)   # True 

#===========================================================================================================

#8.Write a program to check whether a number is even or odd using operators.

num = int(input("Enter a number: "))

if num % 2 == 0:
     print(num, "is Even")
else:
     print(num, "is Odd")

#===========================================================================================================

#9.Write a program to calculate the area of a rectangle using arithmetic operators and user input.

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
print("Area of rectangle:", area)

#===========================================================================================================

#10.Explain operator precedence in Python and write a program showing how precedence affects the result.

# Precedence order: Parentheses > Exponentiation > Multiplication/Division > Addition/Subtraction

# Example:
result1 = 10 + 2 * 3       # Multiplication first → 10 + 6 = 16
result2 = (10 + 2) * 3     # Parentheses first → 12 * 3 = 36
result3 = 2 ** 3 * 2       # Exponentiation first → 8 * 2 = 16

print("Result1:", result1)
print("Result2:", result2)       
print("Result3:", result3)

