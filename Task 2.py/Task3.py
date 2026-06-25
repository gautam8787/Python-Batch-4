# Gautam Task 3

# -------------------------------------------------------

# Q 1: Student Batch Management System (Basic)

class Student:
    institute_name = "ABC Training Institute"         # Class Variable

    def __init__(self, student_id, name, course):
        self.student_id = student_id             # Instance Variables
        self.name = name
        self.course = course

    def display_student(self):
        print("-----------------------------------------")
        print("Student Details")
        print("-----------------------------------------")
        print(f"Institute Name : {Student.institute_name}")
        print(f"Student ID     : {self.student_id}")
        print(f"Student Name   : {self.name}")
        print(f"Course         : {self.course}")
        print("-----------------------------------------\n")

s1 = Student(101, "Rahul", "Python Full Stack")     # Examples
s2 = Student(102, "Priya", "Java Full Stack")
s3 = Student(103, "Sai", "Data Science")
s4 = Student(104, "Anita", "AI & ML")
s5 = Student(105, "Kiran", "Cloud Computing")

s1.display_student()
s2.display_student()
s3.display_student()
s4.display_student()
s5.display_student()

# -------------------------------------------------------

# Q 2: Employee Information System (Beginner)

class Employee:
    company_name = "Tech Solutions Pvt Ltd"          # Class Variable

    def __init__(self, emp_id, name, dept, salary):
        self.emp_id = emp_id                # Instance Variables
        self.name = name
        self.dept = dept
        self.salary = salary

    def display_employee(self):
        bonus = 5000               # Local Variable
        print("-----------------------------------------")
        print("Employee Details")
        print("-----------------------------------------")
        print(f"Company Name   : {Employee.company_name}")
        print(f"Employee ID    : {self.emp_id}")
        print(f"Employee Name  : {self.name}")
        print(f"Department     : {self.dept}")
        print(f"Salary         : ₹{self.salary:,}")
        print(f"Bonus          : ₹{bonus:,}")
        print("-----------------------------------------\n")

e1 = Employee(1001, "Sairam", "Python", 50000)     # Examples
e2 = Employee(1002, "Priya", "Java", 60000)
e3 = Employee(1003, "Rahul", "Data Science", 70000)
e4 = Employee(1004, "Anita", "Testing", 45000)

e1.display_employee()
e2.display_employee()
e3.display_employee()
e4.display_employee()

# -------------------------------------------------------

# Q 3: Bank Customer Management System (Intermediate)

BANK_NAME = "National Bank of India"      # Global Variable

class Customer:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no                 # Instance Variables
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def display_account(self):
        print("-----------------------------------------")
        print("Bank Customer Details")
        print("-----------------------------------------")
        print(f"Bank Name       : {BANK_NAME}")
        print(f"Account Number  : {self.acc_no}")
        print(f"Customer Name   : {self.name}")
        print(f"Account Type    : {self.acc_type}")
        print(f"Balance         : ₹{self.balance:,}")
        print("-----------------------------------------\n")

c1 = Customer(12345678, "Priya", "Savings", 85000)       # Examples
c2 = Customer(87654321, "Rahul", "Current", 120000)
c3 = Customer(11223344, "Sai", "Savings", 45000)
c4 = Customer(44332211, "Anita", "Salary", 95000)
c5 = Customer(99887766, "Kiran", "Savings", 150000)

c1.display_account()
c2.display_account()
c3.display_account()
c4.display_account()
c5.display_account()

# -------------------------------------------------------

# Q 4: Online Shopping Inventory System (Intermediate)

class Product:
    GST = "18%"           # Class Variable

    def __init__(self, prod_id, name, brand, price):
        self.prod_id = prod_id              # Instance Variables
        self.name = name
        self.brand = brand
        self.price = price

    def display_product(self):
        discount = "10%"                  # Local Variable
        print("-----------------------------------------")
        print("Product Details")
        print("-----------------------------------------")
        print(f"Product ID      : {self.prod_id}")
        print(f"Product Name    : {self.name}")
        print(f"Brand           : {self.brand}")
        print(f"Price           : ₹{self.price:,}")
        print(f"GST             : {Product.GST}")
        print(f"Discount        : {discount}")
        print("-----------------------------------------\n")

p1 = Product("P101", "Laptop", "Dell", 65000)         # Examples
p2 = Product("P102", "Mobile", "Samsung", 25000)
p3 = Product("P103", "Keyboard", "Logitech", 1500)
p4 = Product("P104", "Mouse", "HP", 800)
p5 = Product("P105", "Monitor", "LG", 12000)

p1.display_product()
p2.display_product()
p3.display_product()
p4.display_product()
p5.display_product()

# -------------------------------------------------------

# Q 5: Hospital Management System (Advanced)

HOSPITAL_NAME = "City Care Hospital"  # Global Variable

class Patient:
    doctor_name = "Dr. Sharma"        # Class Variable

    def __init__(self, patient_id, name, age, disease, fee):
        self.patient_id = patient_id             # Instance Variables
        self.name = name
        self.age = age
        self.disease = disease
        self.fee = fee

    def display_patient(self):
        room_charge = 1000                # Local Variable
        print("-----------------------------------------")
        print("Hospital Details")
        print("-----------------------------------------")
        print(f"Hospital Name      : {HOSPITAL_NAME}")
        print(f"Doctor Name        : {Patient.doctor_name}")
        print(f"Patient ID         : {self.patient_id}")
        print(f"Patient Name       : {self.name}")
        print(f"Age                : {self.age}")
        print(f"Disease            : {self.disease}")
        print(f"Consultation Fee   : ₹{self.fee:,}")
        print(f"Room Charge        : ₹{room_charge:,}")
        print("-----------------------------------------\n")

    def display_hospital(self):
        print(f"Hospital: {HOSPITAL_NAME}, Doctor: {Patient.doctor_name}\n")

p1 = Patient("P101", "Ramesh", 42, "Viral Fever", 700)     # Examples
p2 = Patient("P102", "Priya", 28, "Diabetes", 1000)
p3 = Patient("P103", "Sai", 40, "Hypertension", 1200)
p4 = Patient("P104", "Anita", 30, "Migraine", 800)
p5 = Patient("P105", "Kiran", 50, "Arthritis", 1500)

p1.display_patient()
p2.display_patient()
p3.display_patient()
p4.display_patient()
p5.display_patient()
