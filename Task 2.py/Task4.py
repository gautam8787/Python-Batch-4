# Gautam Task 4

# -------------------------------------------------------

# Question 1: Student Grade Management System (Basic)

class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def display_student(self):         # Instance Method
        print("-----------------------------------------")
        print("Student Details")
        print("-----------------------------------------")
        Student.college_name()
        print(f"Student ID   : {self.student_id}")
        print(f"Student Name : {self.name}")
        print(f"Marks        : {self.marks}")
        Student.pass_marks()
        print("-----------------------------------------\n")

    @classmethod           # Class Method
    def college_name(cls):
        print("College Name : ABC Training Institute")

    @staticmethod           # Static Method
    def pass_marks():
        print("Pass Marks   : 35")

s1 = Student(101, "Rahul", 85)    # Examples
s2 = Student(102, "Priya", 72)
s3 = Student(103, "Sai", 90)
s4 = Student(104, "Anita", 65)
s5 = Student(105, "Kiran", 40)

s1.display_student()
s2.display_student()
s3.display_student()
s4.display_student()
s5.display_student()

# -------------------------------------------------------

# Question 2: Employee Payroll System (Beginner)

class Employee:
    def __init__(self, emp_id, name, dept, salary):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept
        self.salary = salary

    def display_employee(self):            # Instance Method
        print("-----------------------------------------")
        print("Employee Details")
        print("-----------------------------------------")
        Employee.company_name()
        print(f"Employee ID   : {self.emp_id}")
        print(f"Employee Name : {self.name}")
        print(f"Department    : {self.dept}")
        print(f"Salary        : ₹{self.salary:,}")
        print(f"Annual Salary : ₹{self.annual_salary():,}")
        Employee.working_days()
        print("-----------------------------------------\n")

    def annual_salary(self):        # Instance Method
        return self.salary * 12

    @classmethod         # Class Method
    def company_name(cls):
        print("Company Name  : Tech Solutions Pvt Ltd")

    @staticmethod            # Static Method
    def working_days():
        print("Working Days Per Month : 22")

e1 = Employee(1001, "Sairam", "Python", 50000)     # Examples
e2 = Employee(1002, "Priya", "Java", 60000)
e3 = Employee(1003, "Rahul", "Data Science", 70000)
e4 = Employee(1004, "Anita", "Testing", 45000)
e5 = Employee(1005, "Kiran", "DevOps", 55000)

e1.display_employee()
e2.display_employee()
e3.display_employee()
e4.display_employee()
e5.display_employee()

# -------------------------------------------------------

# Q 3: Online Shopping System (Intermediate)

class Product:
    def __init__(self, prod_id, name, qty, price):
        self.prod_id = prod_id
        self.name = name
        self.qty = qty
        self.price = price

    def display_product(self):      # Instance Method
        print("-----------------------------------------")
        print("Product Details")
        print("-----------------------------------------")
        Product.store_name()
        print(f"Product ID : {self.prod_id}")
        print(f"Product Name : {self.name}")
        print(f"Quantity : {self.qty}")
        print(f"Price : ₹{self.price:,}")
        print(f"Total Amount : ₹{self.calculate_bill():,}")
        Product.gst_percentage()
        print("-----------------------------------------\n")

    def calculate_bill(self):        # Instance Method
        return self.qty * self.price

    @classmethod       # Class Method
    def store_name(cls):
        print("Store Name : Python Shopping Mart")

    @staticmethod         # Static Method
    def gst_percentage():
        print("GST : 18%")


p1 = Product("P101", "Laptop", 2, 60000)   # Examples
p2 = Product("P102", "Mobile", 1, 25000)
p3 = Product("P103", "Keyboard", 3, 1500)
p4 = Product("P104", "Mouse", 2, 800)
p5 = Product("P105", "Monitor", 1, 12000)

p1.display_product()
p2.display_product()
p3.display_product()
p4.display_product()
p5.display_product()

# -------------------------------------------------------

# Q 4: Bank Account Management System (Intermediate)

class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def display_account(self):         # Instance Method
        print("-----------------------------------------")
        print("Account Details")
        print("-----------------------------------------")
        BankAccount.bank_name()
        print(f"Account Number : {self.acc_no}")
        print(f"Customer Name : {self.name}")
        print(f"Balance : ₹{self.balance:,}")
        BankAccount.minimum_balance()
        print("-----------------------------------------\n")

    def deposit(self, amount):             # Instance Method
        self.balance += amount
        print(f"Deposited ₹{amount:,} into {self.name}'s account.")

    def withdraw(self, amount):        # Instance Method
        if self.balance - amount >= 1000:
            self.balance -= amount
            print(f"Withdrew ₹{amount:,} from {self.name}'s account.")
        else:
            print("Withdrawal denied. Minimum balance requirement not met.")

    @classmethod            # Class Method
    def bank_name(cls):
        print("Bank Name : National Bank of India")

    @staticmethod         # Static Method
    def minimum_balance():
        print("Minimum Balance : ₹1000")

c1 = BankAccount(12345678, "Ram", 85000)    # Examples
c2 = BankAccount(87654321, "Priya", 120000)
c3 = BankAccount(11223344, "Sai", 45000)

c1.display_account()
c1.deposit(5000)
c1.withdraw(20000)
c1.display_account()

c2.display_account()
c2.withdraw(119500)  # Will fail due to minimum balance
c2.display_account()

c3.display_account()
c3.deposit(10000)
c3.display_account()

# -------------------------------------------------------

# Q 5: Movie Ticket Booking System (Advanced)

class MovieTicket:
    def __init__(self, booking_id, cust_name, movie, tickets, price):
        self.booking_id = booking_id
        self.cust_name = cust_name
        self.movie = movie
        self.tickets = tickets
        self.price = price

    def display_booking(self):           # Instance Method
        print("-----------------------------------------")
        print("Movie Ticket Details")
        print("-----------------------------------------")
        MovieTicket.theatre_name()
        print(f"Booking ID : {self.booking_id}")
        print(f"Customer Name : {self.cust_name}")
        print(f"Movie Name : {self.movie}")
        print(f"Tickets : {self.tickets}")
        print(f"Ticket Price : ₹{self.price}")
        print(f"Total Amount : ₹{self.calculate_bill()}")
        MovieTicket.booking_rules()
        print("-----------------------------------------\n")

    def calculate_bill(self):     # Instance Method
        return self.tickets * self.price

    @classmethod          # Class Method
    def theatre_name(cls):
        print("Theatre Name      : PVR Cinemas")

    @staticmethod     # Static Method
    def booking_rules():
        print("\nBooking Rules")
        print("• Carry a valid ID proof.")
        print("• Tickets cannot be cancelled after the show starts.")
        print("• Entry is not allowed after 30 minutes from the movie start time.")

t1 = MovieTicket("B101", "Sai", "Leo", 3, 250)   # Examples
t2 = MovieTicket("B102", "Rahul", "KGF", 2, 300)
t3 = MovieTicket("B103", "Priya", "RRR", 4, 200)
t4 = MovieTicket("B104", "Anita", "Pushpa", 1, 350)
t5 = MovieTicket("B105", "Kiran", "Baahubali", 5, 150)

t1.display_booking()
t2.display_booking()
t3.display_booking()
t4.display_booking()
t5.display_booking()
