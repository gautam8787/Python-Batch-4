#Gautam Assignment 5

#============================================================================================================

# 1. Convert string to uppercase and lowercase
 
s = input("Enter a string: ")
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())

#============================================================================================================

# 2. Count vowels in a string

s = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for ch in s:
     if ch in vowels:
         count += 1
print("Number of vowels:", count)

#============================================================================================================

# 3. Check if string starts with a specific word

s = input("Enter a string: ")
word = input("Enter the word to check: ")
print("Starts with word?", s.startswith(word))

#============================================================================================================

# 4. Replace spaces with hyphen

s = input("Enter a string: ")
print("String with hyphens:", s.replace(" ", "-"))

#============================================================================================================

# 5. Find length of string without len()

s = input("Enter a string: ")
count = 0
for _ in s:                            # iterating counts characters
     count += 1
print("Length of string:", count)

#============================================================================================================

# 6. Check if string is palindrome

s = input("Enter a string: ")
if s == s[::-1]:
     print("Palindrome")
else:
     print("Not a palindrome")

#============================================================================================================

# 7. Count number of words in a sentence

s = input("Enter a sentence: ")
words = s.split()
print("Number of words:", len(words))

#============================================================================================================

# 8. Count occurrences of a character

s = input("Enter a string: ")
ch = input("Enter a character: ")
print("Occurrences of", ch, ":", s.count(ch))

#============================================================================================================

# 9. Remove leading and trailing spaces

s = input("Enter a string with spaces: ")
print("Trimmed string:", s.strip())

#============================================================================================================

# 10. Check if string contains only digits
 
s = input("Enter a string: ")
print("Contains only digits?,", s.isdigit())

