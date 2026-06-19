# Nested loops
# loop inside a loop 


for i in range(1,4): # 4-1 =3
    for j in range(1,5):   # 5-1 =4
        print(i,j)
        print()

    print()
print("nested loop executed")

# 1,1   
# 1,2
# 1,3
# 1,4

# 2,1
# 2,2
# 2,3
# 2,4

# 3,1
# 3,2 
# 3,3
# 3,4

for i in range(1,4): # 4-1 =3
    for j in range(1,5):   # 5-1 =4
        print(i, "," ,j, " " , end=" ")

    print()


# 1,1 1,2 1,3 1,4


for i in range(1,5):
    print("*" * i )


for i in range(1,5):
    print(" * " * i )


for i in range(4, 0,-1):  
    print("*" * i)

for i in range(4, 0,-1): 
    print(" * " * i) 



for i in range(1,5):  # right aligned triangle 
    print(" " * (4-i) + "*" * i)



# pyramid
 
for i in range(1,5):  # 1 , 3 ,5 ,7
    print(" " * (4-i) + "*" * (2*i -1))



for i in range(1,5):  # no of rows 
    for j in range(1, i+1):   
        print("*" * j ,end="")
    print()


for i in range(4):  # (0,1,2,3)
    for j in range(4):  # (0,1,2,3)
        print(" * ", end="")
    print()

print("out of the loop")



for i in range(1,5):  # (1,2,3,4)
    for j in range(10):  # (1,2,3,4)
        print("*" , end=" ")
    print()

