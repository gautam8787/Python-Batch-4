# Gautam Task 2

# -------------------------------------------------------

# Q 1: Student Admission System (Basic)

class Student:
    def __init__(self, student_id, name, course, fee):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.fee = fee

    def display_student(self):
        print("-----------------------------------------")
        print("Student Details")
        print("-----------------------------------------")
        print(f"Student ID      : {self.student_id}")
        print(f"Student Name    : {self.name}")
        print(f"Course          : {self.course}")
        print(f"Course Fee      : ₹{self.fee:,}")
        print("-----------------------------------------\n")

s1 = Student(101, "Rahul", "Python Full Stack", 45000)   # Examples
s2 = Student(102, "Priya", "Java Full Stack", 40000)
s3 = Student(103, "Sai", "Data Science", 60000)
s4 = Student(104, "Anita", "AI & ML", 75000)

s1.display_student()
s2.display_student()
s3.display_student()
s4.display_student()

# -------------------------------------------------------

# Q 2: Employee Salary System (Beginner)

class Employee:
    def __init__(self, emp_id, name, dept, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept
        self.basic_salary = basic_salary

    def display_employee(self):
        print("-----------------------------------------")
        print("Employee Details")
        print("-----------------------------------------")
        print(f"Employee ID     : {self.emp_id}")
        print(f"Employee Name   : {self.name}")
        print(f"Department      : {self.dept}")
        print(f"Basic Salary    : ₹{self.basic_salary:,}")
        print(f"Annual Salary   : ₹{self.annual_salary():,}")
        print("-----------------------------------------\n")

    def annual_salary(self):
        return self.basic_salary * 12

e1 = Employee(1001, "Sairam", "Python", 50000)   # Examples
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

# Q 3: Online Shopping Order System (Intermediate)

class Order:
    def __init__(self, order_id, cust_name, product, qty, price_per_item):
        self.order_id = order_id
        self.cust_name = cust_name
        self.product = product
        self.qty = qty
        self.price_per_item = price_per_item

    def calculate_total(self):
        return self.qty * self.price_per_item

    def display_order(self):
        print("-----------------------------------------")
        print("Order Details")
        print("-----------------------------------------")
        print(f"Order ID        : {self.order_id}")
        print(f"Customer Name   : {self.cust_name}")
        print(f"Product Name    : {self.product}")
        print(f"Quantity        : {self.qty}")
        print(f"Price Per Item  : ₹{self.price_per_item:,}")
        print(f"Total Amount    : ₹{self.calculate_total():,}")
        print("-----------------------------------------\n")

o1 = Order("ORD101", "Priya", "Laptop", 2, 55000)  # Examples
o2 = Order("ORD102", "Rahul", "Mobile", 1, 25000)
o3 = Order("ORD103", "Sai", "Keyboard", 3, 1500)
o4 = Order("ORD104", "Anita", "Mouse", 2, 800)
o5 = Order("ORD105", "Kiran", "Monitor", 1, 12000)

o1.display_order()
o2.display_order()
o3.display_order()
o4.display_order()
o5.display_order()

# -------------------------------------------------------

# Q 4: Hospital Patient Registration System (Intermediate)

class Patient:
    def __init__(self, patient_id, name, age, disease, fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.fee = fee

    def display_patient(self):
        print("-----------------------------------------")
        print("Patient Details")
        print("-----------------------------------------")
        print(f"Patient ID          : {self.patient_id}")
        print(f"Patient Name        : {self.name}")
        print(f"Age                 : {self.age}")
        print(f"Disease             : {self.disease}")
        print(f"Consultation Fee    : ₹{self.fee:,}")
        print("-----------------------------------------\n")

    def display_fee(self):
        print(f"Consultation Fee for {self.name}: ₹{self.fee:,}\n")

p1 = Patient("P101", "Ramesh", 35, "Viral Fever", 700)   # Examples
p2 = Patient("P102", "Priya", 28, "Diabetes", 1000)
p3 = Patient("P103", "Sai", 40, "Hypertension", 1200)
p4 = Patient("P104", "Anita", 30, "Migraine", 800)
p5 = Patient("P105", "Kiran", 50, "Arthritis", 1500)

p1.display_patient()
p2.display_patient()
p3.display_patient()
p4.display_patient()
p5.display_patient()

# -------------------------------------------------------

# Q 5: Hotel Room Booking System (Advanced)

class HotelBooking:
    def __init__(self, booking_id, cust_name, room_type, days, rent_per_day):
        self.booking_id = booking_id
        self.cust_name = cust_name
        self.room_type = room_type
        self.days = days
        self.rent_per_day = rent_per_day

    def calculate_bill(self):
        return self.days * self.rent_per_day

    def display_booking(self):
        print("-----------------------------------------")
        print("Hotel Booking Details")
        print("-----------------------------------------")
        print(f"Booking ID         : {self.booking_id}")
        print(f"Customer Name      : {self.cust_name}")
        print(f"Room Type          : {self.room_type}")
        print(f"Number of Days     : {self.days}")
        print(f"Rent Per Day       : ₹{self.rent_per_day:,}")
        print(f"Total Bill         : ₹{self.calculate_bill():,}")
        print("-----------------------------------------\n")



b1 = HotelBooking("B101", "Sai", "Deluxe", 3, 2500)    # Examples
b2 = HotelBooking("B102", "Rahul", "Suite", 2, 5000)
b3 = HotelBooking("B103", "Priya", "Standard", 4, 1500)
b4 = HotelBooking("B104", "Anita", "Executive", 5, 3500)
b5 = HotelBooking("B105", "Kiran", "Luxury", 2, 8000)

b1.display_booking()
b2.display_booking()
b3.display_booking()
b4.display_booking()
b5.display_booking()
