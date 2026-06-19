# Lambda function ??

# Anonymous function which is defined by lambda keyword 
# single line function 
# which is used for smaller functions 

def add(a,b):
    c=a+b
    return c
print(add(10,20))

print((lambda a,b : a+b)(30,40))  # single



# Syntax : 

# lambda parameters : expression  ----> declaration 

# how to call ?? 

# (lambda parameters : expression)(arguments) ---> declaration + calling 


(lambda num : print("Even") if num%2==0 else print("odd"))(22)


# write a lambda function for multiple conditions (elif) grade system ()

def is_even(num):
    if num %2 ==0 :
        print("even")

    else: 
        print("odd")

is_even(9)

