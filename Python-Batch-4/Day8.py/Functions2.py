'''
# Types of arguments 

# positional arguments 

def add(b,a):
    print(a)
    print(b)
    return a+b

print(add(10,20))

def login(password, username):
    if username == "admin":
        if password == "Rocky":
            return "login success"
        else:
            return "wrong password"
    
    else:
        return "invalid credentials"
    
print(login("admin" , "Rocky"))

print(login("sairam" , "Rocky"))

print(login("admin" , "Rocky"))


# Keyword arguments 

def login(password, username):
    if username == "admin":
        if password == "Rocky":
            return "login success"
        else:
            return "wrong password"
    
    else:
        return "invalid credentials"

print(login(username="admin",password="Rocky"))


# Default arguments 

def login(password, username="admin"):
    if username == "admin":
        if password == "Rocky":
            return "login success"
        else:
            return "wrong password"
    
    else:
        return "invalid credentials"

print(login(username="sairam",password="Rocky"))


# *args --->

def total(*kkk):
    return 

print(total(20,40,50))


def employee(name, *rating):
    return f"{name} : {max(rating)}"

print(employee("Rocky",7,8,4,6,10))

print(employee("sairam",70,8,4,6,100))

# **KWargs ---> keyword args 

def details(**kwargs):
    return kwargs

print(details(name="Rocky",age=28,role="trainer",salary=50000))


'''
def details(beta,*mummy,**papa):
    return beta,mummy,papa

print(details(10,"sumit",22,"python developer" ,name="Rocky",age=28,role="trainer",salary=50000))



def login(**data):
    if data.get("username") == "admin" and data.get("password") == "Rocky123":
        return "login success"
    
    return "login failed"

print(login(username="admin" , password="Rocky123"))
print(login(username="admin" , password="Rocky12"))
