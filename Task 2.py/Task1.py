# Gautam Task 1

# -------------------------------------------------------

# Q 1: Student Profile System (Basic)

class Student:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def display_details(self):
        print("---------------------------------")
        print("Student Details")
        print("---------------------------------")
        print(f"Student ID      : {self.student_id}")
        print(f"Student Name    : {self.name}")
        print(f"Course          : {self.course}")
        print("---------------------------------\n")

s1 = Student(101, "Rahul", "Python Full Stack")   # Create Student objects
s2 = Student(102, "Priya", "Java Full Stack")
s3 = Student(103, "Sai", "Data Science")

s1.display_details()       # Display student details
s2.display_details()
s3.display_details()

# -------------------------------------------------------

# Q 2: Employee ID Card Generator (Beginner)

class Employee:
    def __init__(self, emp_id, name, dept, salary):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept
        self.salary = salary

    def generate_id_card(self):
        print("---------------------------------")
        print("EMPLOYEE ID CARD")
        print("---------------------------------")
        print(f"Employee ID     : {self.emp_id}")
        print(f"Employee Name   : {self.name}")
        print(f"Department      : {self.dept}")
        print(f"Salary          : ₹{self.salary:,}")
        print("---------------------------------\n")

e1 = Employee(1001, "Sairam", "Python", 50000)       # Examples
e2 = Employee(1002, "Priya", "Java", 60000)
e3 = Employee(1003, "Rahul", "Data Science", 70000)
e4 = Employee(1004, "Anita", "Testing", 45000)
e5 = Employee(1005, "Kiran", "DevOps", 55000)

e1.generate_id_card()
e2.generate_id_card()
e3.generate_id_card()
e4.generate_id_card()
e5.generate_id_card()

# -------------------------------------------------------

# Q 3: Product Catalog System (Intermediate)

class Product:
    def __init__(self, prod_id, name, brand, price):
        self.prod_id = prod_id
        self.name = name
        self.brand = brand
        self.price = price

    def display_product(self):
        print("---------------------------------")
        print("Product Details")
        print("---------------------------------")
        print(f"Product ID      : {self.prod_id}")
        print(f"Product Name    : {self.name}")
        print(f"Brand           : {self.brand}")
        print(f"Price           : ₹{self.price:,}")
        print("---------------------------------\n")

p1 = Product(201, "Laptop", "Dell", 55000)        # Examples
p2 = Product(202, "Mobile", "Samsung", 25000)
p3 = Product(203, "Keyboard", "Logitech", 1500)
p4 = Product(204, "Mouse", "HP", 800)
p5 = Product(205, "Monitor", "LG", 12000)

p1.display_product()
p2.display_product()
p3.display_product()
p4.display_product()
p5.display_product()

print(f"Total Products Created : 5")

# -------------------------------------------------------

# Q 4: Bank Customer Information System (Intermediate)

class BankCustomer:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def display_customer(self):
        print("---------------------------------")
        print("Customer Details")
        print("---------------------------------")
        print(f"Customer Name   : {self.name}")
        print(f"Account Number  : {self.acc_no}")
        print(f"Account Type    : {self.acc_type}")
        print(f"Balance         : ₹{self.balance:,}")
        print("---------------------------------\n")

    def check_balance(self):
        print(f"Available Balance for {self.name}: ₹{self.balance:,}\n")

c1 = BankCustomer(12345678, "Ram", "Savings", 85000)       # Examples
c2 = BankCustomer(87654321, "Priya", "Current", 120000)
c3 = BankCustomer(11223344, "Sai", "Savings", 45000)
c4 = BankCustomer(44332211, "Anita", "Salary", 95000)

c1.display_customer()
c1.check_balance()

c2.display_customer()
c2.check_balance()

c3.display_customer()
c3.check_balance()

c4.display_customer()
c4.check_balance()

# -------------------------------------------------------

# Q 5: Food Delivery Order System (Advanced)

class FoodOrder:
    def __init__(self, order_id, cust_name, restaurant, food_item, qty, price_per_item):
        self.order_id = order_id
        self.cust_name = cust_name
        self.restaurant = restaurant
        self.food_item = food_item
        self.qty = qty
        self.price_per_item = price_per_item

    def calculate_bill(self):
        return self.qty * self.price_per_item

    def display_order(self):
        print("---------------------------------")
        print("Food Order Details")
        print("---------------------------------")
        print(f"Order ID        : {self.order_id}")
        print(f"Customer Name   : {self.cust_name}")
        print(f"Restaurant      : {self.restaurant}")
        print(f"Food Item       : {self.food_item}")
        print(f"Quantity        : {self.qty}")
        print(f"Price per Item  : ₹{self.price_per_item}")
        print(f"Total Bill      : ₹{self.calculate_bill()}")
        print("---------------------------------\n")


o1 = FoodOrder(1001, "Sai", "Paradise", "Chicken Biryani", 2, 350)     # Examples
o2 = FoodOrder(1002, "Rahul", "Dominos", "Pizza", 1, 500)
o3 = FoodOrder(1003, "Priya", "Burger King", "Veg Burger", 3, 120)
o4 = FoodOrder(1004, "Anita", "KFC", "Zinger Burger", 2, 250)
o5 = FoodOrder(1005, "Kiran", "CCD", "Cold Coffee", 2, 150)

o1.display_order()
o2.display_order()
o3.display_order()
o4.display_order()
o5.display_order()

