'''
# loops 

# for loop 
 # a for loops is used for iteration over a sequence . (range , list , tuple , string)

# when we know the range (how many times)

#for varibale in sequence:
    #statements 
    #statements 

employees=["sathwik", "sumanth","Naseem", "manasa","sairam"]

for emp in employees:
    print(emp, "is a super man ")

print("come out of dreams")


# strings 

name=input("enter any name")

for x in name:
    print(x)


for i in range(1,11):
    print(i)


'''
# while loop 
# when you dont know the range 
# it excecutes untill the condition is true 

# while condition :
    #statements 
    #statements 
'''
i=1
while i<=5:
    print(i)
    i+=1

'''
# prime number 
# number which is divisible by 1 and itself 

# nested loops 
#loop control statements --- pass , break , continue 
'''

# is prime number or not 

num=int(input("enter any number : "))
count=0

for i in range(1,num+1):
    if num%i==0:
        count+=1

if count==2:
    print(num, "is a prime number")
else:
    print(num, "is a not prime number")




# prime number or not using while loop 

num=int(input("enter any number : "))
count=0
i=1
while i<=num:
    if num%i==0:
        count+=1
    i+=1

if count==2:
    print(num, "is a prime number")
else:
    print(num, "is a not prime number")

'''
# first 10 prime numbers program 

# 2,3,5,7,11,13,17,.......
'''
num=2
count=0
while count<10:
    i=1
    factor=0
    while i<=num:
        if num%i==0:
            factor+=1
        i+=1

    if factor==2:
        print(num)
        count+=1
    num+=1

'''
employees=["sathwik", "sumanth","Naseem", "manasa","sairam"]

for emp in employees:
    print(emp, "is a super man ")

print("come out of dreams")


for i in range(0,10,2):  # (0,2,4, 6, 8)
    print(i)

for i in range(10):  # default start - 0
    print(i)

# range(start , stop , step )
# step - 1 default 

for i in range(4):
    for j in range(4):
        print(i,j)


for i in range(10 , 0 ,-1):  # 0 -(-1) =0+1 =1
    print(i)



# while loop :  runs untill the condition is true 
# when you dont know , how many times you want to iterate 

# while condition :
#   block 

i = 1
while i <= 10:
    print(i)
    i += 1 


# prime no's --- 2 , 3 , 5 , 7 ,11 , 13 , 17 , 19 , 23 , 29 

# prime num  
# divisible by 1 and itself 




# if num divisible by 1 and num  --->

# num =10 ---> 5%2 ==0 ??  5%3 ==0 ??  5%4 ==0 ??  5%5 ==0 ??

# num =37 range(2, 38)
'''

num = int(input("enter any number : "))

if num > 1 :
 
    for i in range(2, num):
        if num % i ==0 :  
            print(num , "is not a prime number ")
            break

    else:
        print(num , "is a prime number")

else : 
    print("not a prime number")


# num = [10, 20, 50 ,5 ,4 , 2]



num = int(input("enter any number : "))
 
if num > 1:

    i = 2
    while i < num : 
        if num % i == 0:
            print(num , " is not a prime number")
            break
        i+=1

    else :
        print(num ,"is a  prime number")

else :
    print("not a prime ")


'''

num = int(input(" enter any munber : "))

count = 0
i = 1

while i <= num :
    if num % i == 0 :
        count += 1
    i+=1

if count==2:   # only 2 
    print(num , " is a prime number")

else:
    print(num , " is not a prime number")





