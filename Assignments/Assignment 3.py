#Gautam Assignment 3

#============================================================================================================

#1.Create a list of 5 student names

students = ["Asha", "Bablu", "Chandu", "Dravid", "Shanti"]
students.append("Rohan")
students.remove("Chandu")
print("Final list of students:", students)

#============================================================================================================

#2.Write a program to find the largest and smallest elements in a list without using built-in functions.

numbers = [12, 45, 7, 23, 89, 34]
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("List:", numbers)
print("Largest element:", largest)
print("Smallest element:", smallest)        

#============================================================================================================

#3.Create a tuple with mixed data types 

# Step 1: 
my_tuple = (10, "Hello", 3.14, True, [1, 2, 3])
print("First element:", my_tuple[0])   
print("Second element:", my_tuple[1]) 
print("Last element:", my_tuple[-1])  

# Step 2: 
          #Tuples are immutable, meaning once created, their elements cannot be changed directly.
          #For example, trying to do: my_tuple[1] = "World" will raise an error.

# Step 3: 
temp_list = list(my_tuple)   # Convert tuple to list
temp_list[1] = "World"       # Modify an element
new_tuple = tuple(temp_list) # Convert back into tuple

print("Modified tuple:", new_tuple)

#============================================================================================================

#4.Write a program to remove duplicate values from a list using a set.

numbers = [10, 20, 30, 20, 40, 10, 50, 30]
unique_set = set(numbers)
unique_list = list(unique_set)
print("Original list:", numbers)
print("List after removing duplicates:", unique_list)

#============================================================================================================

#5.Create a dictionary with employee details (id, name, salary).

employee = {"id": 101,"name": "Archana", "salary": 50000}
employee["department"] = "HR"
employee["salary"] = 60000
del employee["department"]
print("Final Employee Details:", employee)

#============================================================================================================

#6.Write a program to iterate through a dictionary and print: Keys, Values ,Key-value pairs.

employee = {"id": 101, "name": "Alice", "salary": 60000}
print("Keys:")
for key in employee.keys():
    print(key)
print("Values:")
for value in employee.values():
    print(value)
print("Key-Value Pairs:")
for key, value in employee.items():
    print(key, ":", value)

#============================================================================================================

#7.Declare two sets, perform and display: Union, Intersection, Difference.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_result = set1 | set2                 #  set1.union(set2)
intersection_result = set1 & set2          #  set1.intersection(set2)
difference_result = set1 - set2            #  set1.difference(set2)
print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", union_result)
print("Intersection:", intersection_result)
print("Difference (Set1 - Set2):", difference_result)

#============================================================================================================

#8.Write a program to count the frequency of each element in a list using a dictionary.

numbers = [10, 20, 10, 30, 20, 40, 10, 30, 50]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1                # Increment count if already exists
    else:
        frequency[num] = 1                 # Initialize count if first occurrence
print("Original list:", numbers)
print("Frequency of each element:")
for key, value in frequency.items():
    print(key, ":", value)

#============================================================================================================

#9.Explain the difference between list, tuple, set, and dictionary with one real-time example each

#1.List:
 #        Definition:  An ordered, mutable collection that allows duplicate elements.

  #       Key Features:
                         #Preserves order of insertion.
                         #Elements can be changed, added, or removed.

         #Real-time Example: A shopping cart in an online store.
       
shopping_cart = ["apple", "banana", "apple", "milk"]   # python code

#2.Tuple:
        # Definition: An ordered, immutable collection that allows duplicates.

         #Key Features:
                        #Preserves order.
                        #Cannot be modified after creation.

         #Real-time Example: GPS coordinates (latitude, longitude).

location = (19.2813, 73.0483)         # python code

#3.Set:
        ##Key Features:
                      #No duplicates.
                      #Order is not guaranteed.

        #Real-time Example: Unique student IDs in a class.

student_ids = {101, 102, 103, 101}    # python code

#4.Dictionary:
               #Definition: A collection of key-value pairs, mutable, unordered (in older versions, ordered in Python 3.7+).

               #Key Features:
                              #Fast lookups using keys.
                              #Keys must be unique.

               #Real-time Example: Employee record system.

employee = {"id": 101, "name": "Alice", "salary": 60000}   # python code


