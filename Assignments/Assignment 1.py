#Gautam_Assignment 1

#===========================================================================================================

 #1. Program to Calculate the Area of a Circle

pi = 3.14159
R = float(input("Enter the radius = "))
Area = pi*R**2
print("area of circle = ", Area)

#===========================================================================================================

 #2. Program to Calculate Total Cost After Discount

op = float(input("Enter original price: "))
dp = float(input("Enter discount : "))
final_price = op - (op * dp / 100)
print("Final Price =", final_price)

#===========================================================================================================

 #3. Program to Calculate Simple Interest

principle=int(input("enter principal amount ="))
rate=int(input("enter rate of intrest ="))
time=int(input("enter time ="))
simple_intrest = (principle*time*rate)/100
print ("simple intrest is =" ,int(simple_intrest))

#===========================================================================================================

 #4. Program to Calculate Total Salary

basic_salary = int(input("Enter a Basic Salary : "))
hra = int(input("Enter a House Rent Allowance : "))
da = int(input("Enter a Dearness Allowance : " ))
total_salary = basic_salary + hra + da
print("Total Salary of Employee : ",total_salary)

#===========================================================================================================

#5. Program to Calculate Distance Traveled

speed = float(input("Enter speed: "))
time = float(input("Enter time: "))
distance = speed * time
print("Distance =", distance)

#===========================================================================================================

#6. Program to Convert Temperature from Celsius to Fahrenheit

temp_celcius = float(input("enter celsius: "))
fahrenheit = (temp_celcius * 9/5) + 32
print("Fahrenheit =", fahrenheit)

#===========================================================================================================

#7 .Program to Find the Maximum of Two Numbers Using Ternary Operator

a = int (input("Enter a 1st Number : "))
b = int (input("Enter a 2nd Number : "))

if(a>b):
    print("A is Large Number and Value of A is :",a)
elif(a<b):
    print("B is Large and value of B is : ",b)
elif(a==b):
    print("A and B is Equal and Value is : ",a)

#===========================================================================================================

#8. Swap Two Numbers

a=int(input("enter a value = "))
b=int(input("enter b value = "))
a,b=b,a
print("a = ",a)
print("b = ",b)

#===========================================================================================================

#9.  Next Multiple of 100

num = int(input("Enter a number: "))
next_multiple = (num // 100 + 1) * 100
print("Next multiple of 100 =", next_multiple)

#===========================================================================================================

#10. Splitting into the Teams

people = int(input("Enter number of people: "))
teams = people // 2
left = people % 2
print("Teams formed:", teams)
print("People left without team:", left)



#===========================================================================================================

#----------------------------------------------END----------------------------------------------------------

#===========================================================================================================

