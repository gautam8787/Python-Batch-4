# Advance python concepts 

# Iterators 
# Generators
# Decorators

# used in 
# data science 
# API's
# Backend systems 
# frameworks 
# memory optimization 

'''
# Iterators : 

# __iter__()  ---> return iterator  
# __next__() ---> it will fetch next element / value

l =["sairam","sumit","sai","deepika"]
it = iter(l)
for i in l:
    print(next(it))


# Generators : it is a special function that returns the values one by one using yield keyword 

def gene():
    for i in range(10000):
        yield i

res = gene()
for value in range(10000):
    print(next(res))



def numbers():
    yield "sai"
    yield 1
    yield 2
    yield 3
    yield 4

for i in numbers():
    print(i)


# Decorators : is a func which modifies another function without changing the original code 

# decorator means wrapper 

# gift --> watch --> box --> wrapper / giftcover 

def outer():

    def inner():
        return "inner function"
    return inner()

print(outer())


def wrapper(yy):
    def sample():
        print("before function")
        yy()
        print("aFTER FUNCTION ")
    return sample

@wrapper
def demoyy():
    print("this is demoyy function")
demoyy()


'''
def wrapper(func):
    def sample(args):
        print("before function")
        func(args)
        print("aFTER FUNCTION ")
    return sample

@wrapper
def demoyy(args):
    print("this is demoyy function")
    print("msg : ",args)
demoyy("this is a very big headache")

@wrapper
def demo(args):
    print("this is demo function")
    print("msg : ",args)
demo("this is demo function msg ")

# want to create multiple decorators ??? if yes --> how ?? demonstrate 

# if no --> then y ???? explaination 

