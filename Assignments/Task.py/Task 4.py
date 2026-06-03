# Gautam Task 2

# -------------------------------------------------------

# 31. Program to Check Palindrome String

# Problem Statement: Write a program to check whether a given string is a palindrome (same forward and backward).

string = input("Enter a String : ")

if (string == string[::-1]):
    print("Given String is Palindrome.")
    
else:
    print("Given string is not Palindrome")
    
# -------------------------------------------------------

# 32. Program to Count Vowels in a String

# Problem Statement: Write a program to count the number of vowels in a given string.

count = 0
string = input("Enter string : ")

vowel = "aeiouAEIOU"
for i in string:
    if( i in vowel):
        count+=1

print(count)

# -------------------------------------------------------

# 33. Program to Count Words in a Sentence

# Problem Statement: Write a program to count the number of words in a sentence.

string = input("Enter a string : ")
word = string.split()
count = len(word)

print(count)

# -------------------------------------------------------

## 34. Program to Replace Spaces with Hyphen

# Problem Statement: Write a program to replace all spaces in a string with hyphens (-).

text = input("Enter string : ")
text_1 = text.replace(" ","-")

print(text_1)

# -------------------------------------------------------

## 35. Program to Find Maximum Element in a List

# Problem Statement: Write a program to find the maximum element in a list.

list = [1,2,3,5,70,2]
print(max(list))

val = list[1]

for i in list:
    if val < i:
        max_value = i

print(max_value)

# -------------------------------------------------------
## 36. Program to Remove Duplicates from a List

# Problem Statement: Write a program to remove duplicate elements from a list.

list = [10,20,50,10,80,40,80]

print(list)
text = set(list)
print(text)

unique = []

for i in list:
    if(i not in unique):
        unique.append(i)

print(unique)

# -------------------------------------------------------

# 37. Program to Find Second Largest Number in a List

# Problem Statement: Write a program to find the second largest number in a list.

list = [10,50,20,40,60,20]
list.sort()

print(list[-2])

# -------------------------------------------------------

# 38. Program to Merge Two Lists

# Problem Statement: Write a program to merge two lists into one list.

list_1 = [10,20,50,40]
list_2 = [8,4,7,50,60]

print(list_1+list_2)

# -------------------------------------------------------

# 39. Program to Check Prime Number using Function

# Problem Statement: Write a function to check whether a number is prime.

num = int(input("Enter a Number : "))
 
def prime(num):
    if num <= 1 :
        prime("True")
    else:
        for i in range(2,num): 
            if(num % i == 0):
                print("False")
                break
        else:
            print("True")

prime(num)

# -------------------------------------------------------

# 40. Program to Create Calculator using Functions

# Problem Statement: Write a program using functions to perform basic arithmetic operations (addition, subtraction, multiplication, division).

def add(a,b):
    print("Add : ",a+b)

add(10,20)

def sub (a,b):
    print("Sub : ",a-b)
    
sub(20,10)

def mul(a,b):
    print("Mul : ",a*b)
    
mul(5,2)


def div(a,b):
    print("Div : ",a/b)
    
div(40,2)
