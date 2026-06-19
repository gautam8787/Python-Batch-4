'''
# Higher order functions : it takes another function as an argument and returns another function as a result 

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def product(a,b):
    return a*b


def calculate(func,x,y):
    return func(x,y)

print(calculate(add ,100 ,99))
print(calculate(sub ,100 ,99))
print(calculate(product ,10,9))


def hello(name):
    return "Hi " + name

def message(func,name):
    return func(name)

print(message(hello,"Rocky Bhai"))



# function returning another function 

def power(n):
    def inner(x):
        return x ** n
    return inner

square = power(2)
print(square(4))



def discount(rate):
    def demo(price):
        return price - price * rate
    return demo

ten_percent = discount(0.1)
print(ten_percent(5000))




# Built in higher order functions 

# map() ---> applies function to each and every element in the group of data 

num =[1,2,3,4,5,6]
l = []
for i in num:
    square = i ** 2
    l.append(square)
print(l)


num =[1,2,3,4,5,6]

result =list(map(lambda a : a**3,num))

print(result)  # [1,4,9,16,25,36]

res=list(map(lambda a : a-1 ,result))
print(res)

# square = [1,4,9,16,25,36]


# filter() : filters the output according to the logic 

square = [1,4,9,16,25,36,58,89,99,100] # find even numbers 

even_num = list(filter(lambda a: a % 2==0 ,square))
print(even_num)

# [4,16,36,58,100]


# reduce() : takes collection data as input and gives a single output 

numbers =[10,30,44,87,96,56,78,100]
# sum_of_number = 10+30+44+87+96+56+78+100


from functools import reduce

numbers =[10,30,44,87,96,56,78,100]
results = reduce(lambda a,b : a+b,numbers)
print(results)


names =["sai" ,"ram" ,"is" ,"superman"]
word = reduce(lambda a,b : a + " " + " " + b,names)
print(word)




'''


# Recursion : A function which calls itself, recursive function.
# instead of sloving the whole problem at a time , 
# it sloves a small part and calls itself for the remaining part
 
def sample():
    name = "rocky"
    print(name)

sample()
sample()


# Factorial --> 5! ---> 5*4*3*2*1 = 120

n=8
res=1
for i in range(1,n+1): # 8*7*6*5*4*3*2*1
   res = res*i

print(8*7*6*5*4*3*2*1)

'''
def functionName():
    if base condition :  # when this recursion should stop 
        return result
    else:
        return functionName(small part of problem)

'''

def Factorial(n):
    if n == 1:
        return 1
    return n * Factorial(n-1)

print(Factorial(5))
print(Factorial(8))

