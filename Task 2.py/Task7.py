# Gautam Task 7

# -------------------------------------------------------

# Q 1: Employee Management System (Single Inheritance)

class Employee:
    def __init__(self, emp_id, name, dept):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept

    def employee_details(self):
        print("-----------------------------------------")
        print("Employee Details")
        print("-----------------------------------------")
        print(f"Employee ID        : {self.emp_id}")
        print(f"Employee Name      : {self.name}")
        print(f"Department         : {self.dept}")


class Developer(Employee):
    def __init__(self, emp_id, name, dept, language, experience, salary):
        super().__init__(emp_id, name, dept)
        self.language = language
        self.experience = experience
        self.salary = salary

    def developer_details(self):
        self.employee_details()
        print(f"\nProgramming Lang.  : {self.language}")
        print(f"Experience         : {self.experience} Years")
        print(f"Salary             : ₹{self.salary:,}")
        print("-----------------------------------------\n")



d1 = Developer("EMP101", "Rahul Sharma", "Information Technology", "Python", 4, 850000)   # Example
d1.developer_details()

# -------------------------------------------------------

# Q 2: Banking System (Multilevel Inheritance)

class Customer:
    def __init__(self, cust_id, name):
        self.cust_id = cust_id
        self.name = name

    def customer_details(self):
        print("-----------------------------------------")
        print("Customer Details")
        print("-----------------------------------------")
        print(f"Customer ID      : {self.cust_id}")
        print(f"Customer Name    : {self.name}")


class Account(Customer):
    def __init__(self, cust_id, name, acc_no, acc_type, balance):
        super().__init__(cust_id, name)
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.balance = balance

    def account_details(self):
        self.customer_details()
        print(f"\nAccount Number   : {self.acc_no}")
        print(f"Account Type     : {self.acc_type}")
        print(f"Balance          : ₹{self.balance:,}")


class Loan(Account):
    def __init__(self, cust_id, name, acc_no, acc_type, balance, loan_amount, interest_rate):
        super().__init__(cust_id, name, acc_no, acc_type, balance)
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate

    def loan_details(self):
        self.account_details()
        print(f"\nLoan Amount      : ₹{self.loan_amount:,}")
        print(f"Interest Rate    : {self.interest_rate}%")
        print("-----------------------------------------\n")

l1 = Loan("C101", "Sai Ram", "2345678901", "Savings", 75000, 500000, 9)    # Example
l1.loan_details()

# -------------------------------------------------------

# Q 3: Vehicle Showroom (Hierarchical Inheritance)

class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def vehicle_details(self):
        print("-----------------------------------------")
        print("Vehicle Details")
        print("-----------------------------------------")
        print(f"Brand             : {self.brand}")
        print(f"Model             : {self.model}")
        print(f"Price             : ₹{self.price:,}")


class Car(Vehicle):
    def __init__(self, brand, model, price, doors):
        super().__init__(brand, model, price)
        self.doors = doors

    def car_details(self):
        self.vehicle_details()
        print(f"Doors             : {self.doors}")
        print("-----------------------------------------\n")


class Bike(Vehicle):
    def __init__(self, brand, model, price, engine_capacity):
        super().__init__(brand, model, price)
        self.engine_capacity = engine_capacity

    def bike_details(self):
        self.vehicle_details()
        print(f"Engine Capacity   : {self.engine_capacity} CC")
        print("-----------------------------------------\n")


class Truck(Vehicle):
    def __init__(self, brand, model, price, load_capacity):
        super().__init__(brand, model, price)
        self.load_capacity = load_capacity

    def truck_details(self):
        self.vehicle_details()
        print(f"Load Capacity     : {self.load_capacity} Tons")
        print("-----------------------------------------\n")

c1 = Car("Hyundai", "Creta", 1600000, 5)   # Examples
c1.car_details()

b1 = Bike("Royal Enfield", "Classic 350", 220000, 349)
b1.bike_details()

# -------------------------------------------------------

# Q 4: College Management System (Multiple Inheritance)

class Academic:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def academic_details(self):
        print(f"Student Name     : {self.name}")
        print(f"Roll Number      : {self.roll}")
        print(f"Marks            : {self.marks}")


class Sports:
    def __init__(self, sport, medal):
        self.sport = sport
        self.medal = medal

    def sports_details(self):
        print(f"\nSport            : {self.sport}")
        print(f"Medal            : {self.medal}")


class Student(Academic, Sports):
    def __init__(self, name, roll, marks, sport, medal, grade):
        Academic.__init__(self, name, roll, marks)
        Sports.__init__(self, sport, medal)
        self.grade = grade

    def student_report(self):
        print("-----------------------------------------")
        print("Student Report")
        print("-----------------------------------------")
        self.academic_details()
        self.sports_details()
        print(f"\nGrade            : {self.grade}")
        print("-----------------------------------------\n")

s1 = Student("Arjun", "21EC101", 92, "Cricket", "Gold", "A+")   # Example
s1.student_report()

# -------------------------------------------------------

# Q 5: Hospital Management System (Hybrid Inheritance)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_details(self):
        print(f"Name              : {self.name}")
        print(f"Age               : {self.age}")


class Doctor(Person):
    def __init__(self, name, age, doc_id, specialization):
        super().__init__(name, age)
        self.doc_id = doc_id
        self.specialization = specialization

    def doctor_details(self):
        print(f"Doctor Name       : {self.name}")
        print(f"Doctor ID         : {self.doc_id}")
        print(f"Specialization    : {self.specialization}")


class Patient(Person):
    def __init__(self, name, age, patient_id, disease):
        super().__init__(name, age)
        self.patient_id = patient_id
        self.disease = disease

    def patient_details(self):
        print(f"Patient Name      : {self.name}")
        print(f"Patient ID        : {self.patient_id}")
        print(f"Disease           : {self.disease}")


class MedicalReport(Doctor, Patient):
    def __init__(self, doc_name, doc_age, doc_id, specialization,
                 pat_name, pat_age, patient_id, disease, report_status):
        Doctor.__init__(self, doc_name, doc_age, doc_id, specialization)
        Patient.__init__(self, pat_name, pat_age, patient_id, disease)
        self.report_status = report_status

    def report_details(self):
        print("-----------------------------------------")
        print("Medical Report")
        print("-----------------------------------------")
        self.doctor_details()
        print()
        self.patient_details()
        print(f"\nReport Status      : {self.report_status}")
        print("-----------------------------------------\n")

# Example
mr1 = MedicalReport("Dr. Sharma", 50, "D101", "Cardiology", "Ravi Kumar", 45, "P501", "Heart Disease", "Completed")
mr1.report_details()
