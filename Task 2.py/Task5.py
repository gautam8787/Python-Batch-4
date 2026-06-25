# Gautam Task 5

# -------------------------------------------------------

# Question 1: Student Result Management System (Basic)

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.__marks = None   # Private Variable

    def set_marks(self, marks):       # Setter Method
        self.__marks = marks

    def get_marks(self):       # Getter Method
        return self.__marks

    def display_student(self):
        print("-----------------------------------------")
        print("Student Details")
        print("-----------------------------------------")
        print(f"Student ID      : {self.student_id}")
        print(f"Student Name    : {self.name}")
        print(f"Marks           : {self.get_marks()}")
        print("-----------------------------------------\n")



s1 = Student(101, "Rahul")   # Examples
s1.set_marks(88)

s2 = Student(102, "Priya")
s2.set_marks(92)

s3 = Student(103, "Sai")
s3.set_marks(75)

s4 = Student(104, "Anita")
s4.set_marks(64)

s5 = Student(105, "Kiran")
s5.set_marks(81)

s1.display_student()
s2.display_student()
s3.display_student()
s4.display_student()
s5.display_student()

# -------------------------------------------------------

# Q 2: Bank Account Security System (Beginner)

class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.__balance = balance   # Private Variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

    def display_customer(self):
        print("-----------------------------------------")
        print("Customer Details")
        print("-----------------------------------------")
        print(f"Customer Name   : {self.name}")
        print(f"Account Number  : {self.acc_no}")
        print(f"\nAvailable Balance : ₹{self.get_balance():,}")
        print("-----------------------------------------\n")

c1 = BankAccount(123456789, "Sai", 85000)  # Examples
c2 = BankAccount(987654321, "Priya", 45000)
c3 = BankAccount(112233445, "Rahul", 60000)

c1.deposit(5000)
c1.withdraw(10000)
c1.display_customer()

c2.withdraw(50000)  # Invalid
c2.display_customer()

c3.deposit(15000)
c3.display_customer()

# -------------------------------------------------------

# Q 3: Employee Payroll Security System (Intermediate)

class Employee:
    def __init__(self, emp_id, name, dept):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept
        self.__salary = None   # Private Variable

    def set_salary(self, salary):
        if salary >= 15000:
            self.__salary = salary
        else:
            print("Error: Salary cannot be less than ₹15,000.")

    def get_salary(self):
        return self.__salary

    def display_employee(self):
        print("-----------------------------------------")
        print("Employee Details")
        print("-----------------------------------------")
        print(f"Employee ID      : {self.emp_id}")
        print(f"Employee Name    : {self.name}")
        print(f"Department       : {self.dept}")
        print(f"\nSalary           : ₹{self.get_salary():,}")
        print("-----------------------------------------\n")

e1 = Employee(1001, "Priya", "Python")    # Examples
e1.set_salary(50000) 

e2 = Employee(1002, "Rahul", "Java")
e2.set_salary(14000)  # Invalid

e3 = Employee(1003, "Sai", "Data Science")
e3.set_salary(70000)

e4 = Employee(1004, "Anita", "Testing")
e4.set_salary(45000)

e5 = Employee(1005, "Kiran", "DevOps")
e5.set_salary(55000)

e1.display_employee()
e2.display_employee()
e3.display_employee()
e4.display_employee()
e5.display_employee()

# -------------------------------------------------------

# Q 4: Online Shopping Wallet System (Intermediate)

class CustomerWallet:
    def __init__(self, cust_id, name, balance=0):
        self.cust_id = cust_id
        self.name = name
        self.__wallet_balance = balance   # Private Variable

    def add_money(self, amount):
        if amount > 0:
            self.__wallet_balance += amount
        else:
            print("Invalid amount.")

    def purchase(self, amount):
        if amount <= 0:
            print("Invalid purchase amount.")
        elif amount > self.__wallet_balance:
            print("Insufficient balance.")
        else:
            self.__wallet_balance -= amount

    def check_balance(self):
        return self.__wallet_balance

    def display_customer(self):
        print("-----------------------------------------")
        print("Wallet Details")
        print("-----------------------------------------")
        print(f"Customer ID      : {self.cust_id}")
        print(f"Customer Name    : {self.name}")
        print(f"\nWallet Balance   : ₹{self.check_balance():,}")
        print("-----------------------------------------\n")

w1 = CustomerWallet("C101", "Rahul", 5000)   # Examples
w1.purchase(150)
w1.display_customer()

w2 = CustomerWallet("C102", "Priya", 3000)
w2.add_money(2000)
w2.purchase(4500)
w2.display_customer()

w3 = CustomerWallet("C103", "Sai", 1000)
w3.purchase(1200)  # Insufficient
w3.display_customer()

w4 = CustomerWallet("C104", "Anita", 2500)
w4.add_money(500)
w4.purchase(1000)
w4.display_customer()

w5 = CustomerWallet("C105", "Kiran", 7000)
w5.purchase(2000)
w5.display_customer()

# -------------------------------------------------------

# Q 5: Hospital Patient Record System (Advanced)

class Patient:
    def __init__(self, patient_id, name, age, disease, fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.__medical_history = None   # Private Variable
        self.__consultation_fee = fee   # Private Variable

    def set_medical_history(self, history):       # Setter Method
        self.__medical_history = history

    def get_medical_history(self):        # Getter Method
        return self.__medical_history

    def __calculate_discount(self):      # Private Method
        if self.__consultation_fee > 1000:
            return self.__consultation_fee * 0.10
        return 0

    def final_bill(self):
        discount = self.__calculate_discount()
        return self.__consultation_fee - discount, discount

    def display_patient(self):
        final_amount, discount = self.final_bill()
        print("-----------------------------------------")
        print("Patient Details")
        print("-----------------------------------------")
        print(f"Patient ID          : {self.patient_id}")
        print(f"Patient Name        : {self.name}")
        print(f"Age                 : {self.age}")
        print(f"Disease             : {self.disease}")
        print(f"\nMedical History     : {self.get_medical_history()}")
        print(f"\nConsultation Fee    : ₹{self.__consultation_fee:,}")
        print(f"Discount            : ₹{discount:,}")
        print(f"\nFinal Bill          : ₹{final_amount:,}")
        print("-----------------------------------------\n")


p1 = Patient("P101", "Ramesh", 42, "Viral Fever", 1500)  # Examples
p1.set_medical_history("Available")

p2 = Patient("P102", "Priya", 28, "Diabetes", 900)
p2.set_medical_history("Available")

p3 = Patient("P103", "Sai", 40, "Hypertension", 2000)
p3.set_medical_history("Available")

p4 = Patient("P104", "Anita", 30, "Migraine", 800)
p4.set_medical_history("Available")

p5 = Patient("P105", "Kiran", 50, "Arthritis", 2500)
p5.set_medical_history("Available")

p1.display_patient()
p2.display_patient()
p3.display_patient()
p4.display_patient()
p5.display_patient()
