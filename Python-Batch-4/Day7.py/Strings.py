
# STRINGS 

# STRINGS IN PYTHON

## What is a String?

# A "string" is an immutable sequence of Unicode characters.

name = "Python"
city = 'Hyderabad'

age = 99
print(age)



# **Immutable** → once created, it cannot be changed.

## Real-Time Uses

# User names
# Emails
# Passwords
# File paths
# API responses
# Messages & logs


## Example 1: User Name Storage

username = "sairam"
print(username)


## Example 2: Multiline String


address = """Hyderabad
Telangana
India"""
print(address)


## Example 3: Length of String

msg = "Welcome to Python"
print(len(msg))


## Example 4: Accessing a Character

language = "Python is my Favourite language."  # start from (0) last value in the positive index(n-1) 
print(language[0])
print(language[-1]) # start value in the negative index(-1) last value in -ve index(n)


## Example 5: Immutability Proof

s = "Hello"
s = s + " World"
print(s)



# STRING METHODS (VERY IMPORTANT 🔥)

## Case Conversion Methods

# Example 1: `upper()` and `lower()`

text = "PythON"
print(text.upper())

print(text.lower())


## Example 2: `capitalize()` and `title()`


sentence = "python programming language"
print(sentence.capitalize()) # first word first letter will beconme capital (upper)
print(sentence.title())

## Whitespace & Replace Methods

## Example 3: `strip()`

email = "  user@gmail.com  "
print(email.strip())


## Example 4: `replace()`


msg = "I love Java"
print(msg.replace("Java", "Python"))

## Searching & Splitting

## Example 5: `find()` and `count()`


data = "python is easy"
print(data.find("is"))
print(data.count("o"))

## Example 6: `split()`

csv = "apple,banana,mango"
print(csv.split(","))



## Real-Time Example: Email Validation

email = "test@gmail.com"

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")



## INDEXING IN STRINGS

## What is Indexing?

# Accessing characters using **position numbers**.
# Index starts from **0** ends at (n-1) ----> positive index
# Index starts from **-1** ends at (n) ----> negative index

## Example 1: Positive Indexing

word = "Python"
print(word[0])
print(word[3])


## Example 2: Negative Indexing

print(word[-1])
print(word[-3])


## Example 3: First and Last Character

name = "Sairam"
print(name[0] ,name[1])
print(name[-1])


## Example 4: Iterate Using Index

text = "Python"

#for i in range(len(text)):
    # print(text[i])


for char in "Python":
    print(char)



## Example 5: Character Validation

password = "admin123"
print(password[0].isupper())

name = "Sairam is a super man"
print(name[12],name[13],name[14],name[15],name[16],name[17])



# SLICING IN STRINGS (to extract a substring from a string)
#Syntax

# string[start : end : step]

## Example 1: Basic Slicing

word = "Python"
print(word[5:15])


## Example 2: Omit Start / End

print(word[:6])
print(word[2:])
'''
## Example 3: Negative Slicing

print(word[-4:-1])

## Example 4: Step Value

print(word[::2])

## Example 5: Reverse String

print(word[::-1])

## Example: Mask Account Number

acc = "123456789012"
print("********" + acc[-4:])



#  STRING IMMUTABILITY

s = "Python"
print(id(s))

s = s + "3"
print(id(s))



s="sairam"
print(s)
s=s+"Hero"
print(s)

msg = "Welcome to Python"
print(len(msg))


text = "PythoN"
print(text.upper())
print(text.lower())


sentence = "python programming language"
print(sentence.capitalize()) # first word first letter will beconme capital (upper)
print(sentence.title())


csv = "apple banana mango sairam"
print(csv.split(" "))


# reverse of a string ??

name="Bahubali"
rev=" "
for char in name:
    rev=char+rev
print(rev)   

#username=" Sairam Merugumalla"

#for i in username:
    #print(username[-1])

## Example 4: Iterate Using Index

text = "Python"

for i in range(len(text)):
    print(text[i])

'''

# String Formatting : the process of inserting varibales / expressions in a string 

# format ?? 

name = "nag mama"
print(name ,"is a super hero")

print(f"i love python {name}")

# 3 types of string formatting 

# f-strings(formatted string literals)

# f"text"{variable}
'''
names = "sairam"
job= "trainer"
print(f"i love python {names}")

print(f"im {names} and im a python {job}")

fries = int(input("enter price item 1"))
lays =  int(input("enter price item 2"))
biryani =  int(input("enter price item 3"))

print(f"total bill : {fries + lays + biryani}")
'''
 
for i in range(5):
    print(f"loop {i}")

# str.fortmat() 

name ="chiru"
print("hello {}".format(name))

print("Name : {}, job : {}".format("Deepika", "Python Developer"))

print("Name : {1}, job : {0}".format("Deepika", "Python Developer"))

for i in range(5):
    print("loop {}".format(i))


# % formatting(old style)


name ="chiru"
films = 155.00
print("Name : %s, Films : %d" %(name ,films))



print(10/2) # 5.0

