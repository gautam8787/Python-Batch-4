# Gautam Task 9

# -------------------------------------------------------

# Q 1: Student Information System (Public Members)

class Student:
    def __init__(self, student_id, name, course, marks):
        # Public Members
        self.student_id = student_id
        self.name = name
        self.course = course
        self.marks = marks

    def display_student_details(self):
        print("-----------------------------------------")
        print("Student Details")
        print("-----------------------------------------")
        print(f"Student ID      : {self.student_id}")
        print(f"Student Name    : {self.name}")
        print(f"Course          : {self.course}")
        print(f"Marks           : {self.marks}")
        print("-----------------------------------------\n")

s1 = Student("ST101", "Sai Ram", "Python Full Stack", 92)    # Example
s1.display_student_details()

print(f"Access Outside Class -> Name: {s1.name}, Marks: {s1.marks}")   # Accessing public members directly

# -------------------------------------------------------

# Q 2: Employee Payroll System (Protected Members)

class Employee:
    def __init__(self, emp_id, name, salary):
        self._employee_id = emp_id         # Protected Members
        self._employee_name = name
        self._salary = salary

    def _display_employee(self):
        print(f"Employee ID      : {self._employee_id}")
        print(f"Employee Name    : {self._employee_name}")
        print(f"Salary           : ₹{self._salary:,}")


class Manager(Employee):
    def __init__(self, emp_id, name, salary, designation):
        super().__init__(emp_id, name, salary)
        self.designation = designation

    def display_manager_details(self):
        print("-----------------------------------------")
        print("Employee Details")
        print("-----------------------------------------")
        self._display_employee()
        print(f"Designation      : {self.designation}")
        print("-----------------------------------------\n")

m1 = Manager("EMP101", "Rahul Sharma", 75000, "Manager")     # Example
m1.display_manager_details()

# -------------------------------------------------------

# Q 3: Bank Account System (Private Members)

class BankAccount:
    def __init__(self, acc_no, holder, balance):
        self.__account_number = acc_no     # Private Members
        self.__account_holder = holder
        self.__balance = balance

    def display_account_details(self):
        print("-----------------------------------------")
        print("Bank Account Details")
        print("-----------------------------------------")
        print(f"Account Holder    : {self.__account_holder}")
        print(f"Account Number    : {self.__account_number}")
        print(f"Balance           : ₹{self.__balance:,}")
        print("-----------------------------------------\n")

b1 = BankAccount("1234567890", "Ravi Kumar", 125000)    # Example      
b1.display_account_details()

# Attempting direct access (will cause error)
# print(b1.__balance)  # AttributeError

# -------------------------------------------------------

# Q 4: Hospital Management System (Public, Protected & Private Members)

class Patient:
    def __init__(self, name, doctor, history):
        self.patient_name = name   # Public
        self._doctor_name = doctor # Protected
        self.__medical_history = history  # Private

    def display_patient(self):
        print("-----------------------------------------")
        print("Patient Details")
        print("-----------------------------------------")
        print(f"Patient Name       : {self.patient_name}")
        print(f"Doctor Name        : {self._doctor_name}")
        print(f"Medical History    : {self.__medical_history}")
        print("-----------------------------------------\n")

p1 = Patient("Arjun", "Dr. Sharma", "Diabetes")     # Example
p1.display_patient()

print(f"Access Outside Class -> Patient Name: {p1.patient_name}")     # Public accessible

print(f"Access Outside Class -> Doctor Name: {p1._doctor_name}")   # Protected accessible 

# Private not accessible directly
# print(p1.__medical_history)  # AttributeError

# -------------------------------------------------------

# Q 5: Online Shopping Application (Access Modifiers Combined)

class Customer:
    def __init__(self, name, email, card_number, balance):
        self.customer_name = name    # Public
        self._email = email      # Protected
        self.__card_number = card_number   # Private
        self.__wallet_balance = balance

    def display_customer_details(self):
        print("-----------------------------------------")
        print("Customer Details")
        print("-----------------------------------------")
        print(f"Customer Name      : {self.customer_name}")
        print(f"Email              : {self._email}")
        print(f"Wallet Balance     : ₹{self.__wallet_balance:,}")
        print("-----------------------------------------\n")

    def update_wallet_balance(self, amount):
        self.__wallet_balance += amount
        print("Wallet Updated Successfully!")
        print(f"New Balance        : ₹{self.__wallet_balance:,}\n")

c1 = Customer("Sai Ram", "sairam@gmail.com", "1234-5678-9876", 5000)    # Example
c1.display_customer_details()
c1.update_wallet_balance(2500)

print(f"Access Outside Class -> Name: {c1.customer_name}")    # Public accessible
 
print(f"Access Outside Class -> Email: {c1._email}")     # Protected accessible 

# Private not accessible directly
# print(c1.__card_number)  # AttributeError
