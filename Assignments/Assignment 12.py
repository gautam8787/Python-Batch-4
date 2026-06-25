#Gautam Assignment 12

#============================================================================================================

# Q1: Student Marks Management System

class InvalidMarksError(Exception):
    pass

class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if not isinstance(self.marks, (int, float)):
            raise InvalidMarksError("Marks must be a number.")
        if self.marks < 0 or self.marks > 100:
            raise InvalidMarksError("Marks should be between 0 and 100.")

        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "D"

    def display_student(self):
        try:
            grade = self.calculate_grade()
            print("-----------------------------------------")
            print("Student Details")
            print("-----------------------------------------")
            print(f"Student ID : {self.student_id}")
            print(f"Student Name : {self.name}")
            print(f"Marks : {self.marks}")
            print(f"Grade : {grade}")
        except InvalidMarksError as e:
            print(f"Error: {e}")
            
#  student objects with data
s1 = Student(101, "Arun", 95)
s2 = Student(102, "Babu", 78)
s3 = Student(103, "Charlie", 45)
s4 = Student(104, "Dravid", -10)         # Invalid marks example
s5 = Student(105, "Avantika", 105)       # Invalid marks example

# Display details
s1.display_student()
s2.display_student()
s3.display_student()
s4.display_student()
s5.display_student()

#============================================================================================================

# Q2: Bank Account Management System

class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, acc_no, holder, balance=0):
        self.acc_no = acc_no
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        self.balance -= amount

    def display_balance(self):
        print("-----------------------------------------")
        print("Bank Account Details")
        print("-----------------------------------------")
        print(f"Account Holder : {self.holder}")
        print(f"Current Balance : ₹{self.balance}")
        
# Create accounts
acc1 = BankAccount(1001, "Archana", 5000)
acc2 = BankAccount(1002, "Babu", 2000)

# Deposit money
acc1.deposit(1500)   # Archana deposits ₹1500
acc2.deposit(500)    # Babu deposits ₹500

# Withdraw money
try:
    acc1.withdraw(3000)   # Archana withdraws ₹3000
except InsufficientBalanceError as e:
    print(f"Error: {e}")

try:
    acc2.withdraw(3000)   # Babu tries to withdraw ₹3000 (should raise error)
except InsufficientBalanceError as e:
    print(f"Error: {e}")

# Display balances
acc1.display_balance()
acc2.display_balance()
      
#============================================================================================================

# Q3: Employee Salary Calculator

class Employee:
    def __init__(self, name, basic_salary, bonus):
        if basic_salary < 0:
            raise ValueError("Salary cannot be negative.")
        if bonus < 0:
            raise ValueError("Bonus cannot be negative.")
        self.name = name
        self.basic_salary = basic_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.basic_salary + self.bonus

    def display_salary(self):
        print("-----------------------------------------")
        print("Salary Details")
        print("-----------------------------------------")
        print(f"Employee Name : {self.name}")
        print(f"Basic Salary : ₹{self.basic_salary}")
        print(f"Bonus : ₹{self.bonus}")
        print(f"Total Salary : ₹{self.calculate_salary()}")
        
# Create employee objects
emp1 = Employee("Archana", 50000, 10000)
emp2 = Employee("Babu", 40000, 5000)
emp3 = Employee("Chandu", 60000, 0)

# Display salary details
emp1.display_salary()
emp2.display_salary()
emp3.display_salary()

# Example with invalid data
try:
    emp4 = Employee("David", -30000, 5000)  # Negative salary
    emp4.display_salary()
except ValueError as e:
    print(f"Error: {e}")

try:
    emp5 = Employee("Arun", 45000, -2000)  # Negative bonus
    emp5.display_salary()
except ValueError as e:
    print(f"Error: {e}")

#============================================================================================================

# Q4: Online Shopping Cart

class ProductNotFoundError(Exception):
    pass

class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_product(self, name, price, qty):
        if qty <= 0:
            raise ValueError("Invalid quantity.")
        self.cart[name] = {"price": price, "qty": qty}

    def remove_product(self, name):
        if name not in self.cart:
            raise ProductNotFoundError("Product not found in cart.")
        del self.cart[name]

    def checkout(self):
        if not self.cart:
            raise ValueError("Cart is empty.")
        total = sum(item["price"] * item["qty"] for item in self.cart.values())
        print("-----------------------------------------")
        print("Shopping Cart")
        print("-----------------------------------------")
        for name, details in self.cart.items():
            print(f"Product Name : {name}")
            print(f"Quantity : {details['qty']}")
        print(f"Total Amount : ₹{total}")
        print("Checkout Status : Successful")
        
        # Create a shopping cart
cart = ShoppingCart()

# Add products
cart.add_product("Laptop", 50000, 1)
cart.add_product("Headphones", 2000, 2)
cart.add_product("Mouse", 800, 1)

# Remove a product
try:
    cart.remove_product("Mouse")   # Removing Mouse
except ProductNotFoundError as e:
    print(f"Error: {e}")

# Try removing a product not in cart
try:
    cart.remove_product("Keyboard")   # Not in cart
except ProductNotFoundError as e:
    print(f"Error: {e}")

# Checkout
try:
    cart.checkout()
except ValueError as e:
    print(f"Error: {e}")

        
#============================================================================================================

# Q5: ATM Transaction System

class InvalidPINError(Exception):
    pass

class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.attempts = 3

    def login(self, entered_pin):
        if entered_pin != self.pin:
            self.attempts -= 1
            raise InvalidPINError(f"Incorrect PIN. Remaining Attempts : {self.attempts}")
        return True

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid deposit amount.")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

    def check_balance(self):
        print(f"Current Balance : ₹{self.balance}")


atm = ATM(pin=1234, balance=25000)

# Successful login and transaction
try:
    if atm.login(1234):   # Correct PIN
        atm.check_balance()
        atm.withdraw(5000)
        print("\n-----------------------------------------")
        print("ATM Transaction")
        print("-----------------------------------------")
        print("\nLogin Status : Successful")
        print(f"\nCurrent Balance : ₹{atm.balance}")
        print(f"\nWithdrawal : ₹{atm.balance  - 15000}")
        print(f"\nRemaining Balance : ₹{atm.balance}")
except InvalidPINError as e:
    print(f"Error: {e}")
    print("\nLogin Failed.")
    print(f"\nRemaining Attempts : {atm.attempts}")

# Invalid login attempt
try:
    atm.login(1111)   # Wrong PIN
except InvalidPINError as e:
    print(f"\n{e}")
    print("\nLogin Failed.")
    print(f"\nRemaining Attempts : {atm.attempts}")

#============================================================================================================

# Q6: Library Management System

class BookNotAvailableError(Exception):
    pass

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, name, author, copies):
        if copies < 0:
            raise ValueError("Copies cannot be negative.")
        self.books[book_id] = {"name": name, "author": author, "copies": copies}

    def issue_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Invalid Book ID.")
        if self.books[book_id]["copies"] <= 0:
            raise BookNotAvailableError("Book is currently unavailable.")
        self.books[book_id]["copies"] -= 1

    def return_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Invalid Book ID.")
        self.books[book_id]["copies"] += 1

    def display_book_details(self, book_id):
        book = self.books.get(book_id)
        if book:
            print("-----------------------------------------")
            print("Library Management System")
            print("-----------------------------------------")
            print(f"Book ID : {book_id}")
            print(f"Book Name : {book['name']}")
            print(f"Author : {book['author']}")
            print(f"Available Copies : {book['copies']}")
            
                   
library = Library()

# Add a book
library.add_book("BK101", "Python Programming", "Guido Rossum", 5)

# Display details before issuing
library.display_book_details("BK101")

# Issue the book successfully
try:
    library.issue_book("BK101")
    print("\nBook Issued Successfully")
    print(f"\nRemaining Copies  : {library.books['BK101']['copies']}")
except BookNotAvailableError as e:
    print(f"Error: {e}")

# Force an invalid case (issue until unavailable)
library.books["BK101"]["copies"] = 0
try:
    library.issue_book("BK101")
except BookNotAvailableError as e:
    print(f"\nError: {e}")

        
#============================================================================================================

# Q7: Railway Reservation System

class SeatUnavailableError(Exception):
    pass

class TrainReservation:
    def __init__(self, train_no, seats):
        self.train_no = train_no
        self.seats = seats

    def book_ticket(self, passenger_name):
        if self.seats <= 0:
            raise SeatUnavailableError("No seats available for booking.")
        self.seats -= 1
        print("-----------------------------------------")
        print("Railway Reservation")
        print("-----------------------------------------")
        print(f"Passenger Name : {passenger_name}")
        print(f"Train Number : {self.train_no}")
        print("Booking Status : Confirmed")
        print(f"Available Seats : {self.seats}")

# Create train reservation with 50 seats
train = TrainReservation(train_no=12727, seats=50)

# Successful booking
try:
    train.book_ticket("Sai Ram")
    print("\nSeat Number       : S5-28")   # Example seat assignment
except SeatUnavailableError as e:
    print(f"Error: {e}")

# Force invalid case (no seats left)
train.seats = 0
try:
    train.book_ticket("Ravi Kumar")
except SeatUnavailableError as e:
    print(f"\nError: {e}")

#============================================================================================================

# Q8: Hospital Management System

class DoctorUnavailableError(Exception):
    pass

class Hospital:
    def __init__(self):
        self.appointments = {}

    def book_appointment(self, patient_id, patient_name, doctor, time):
        if not patient_name:
            raise ValueError("Patient name cannot be empty.")
        if doctor not in ["Dr. Reddy", "Dr. Sharma"]:
            raise DoctorUnavailableError("Selected doctor is unavailable.")
        self.appointments[patient_id] = {"name": patient_name, "doctor": doctor, "time": time}

    def display_appointment(self, patient_id):
        appt = self.appointments.get(patient_id)
        if appt:
            print("-----------------------------------------")
            print("Appointment Details")
            print("-----------------------------------------")
            print(f"Patient ID : {patient_id}")
            print(f"Patient Name : {appt['name']}")
            print(f"Doctor : {appt['doctor']}")
            print(f"Appointment Time : {appt['time']}")
            print("Status : Appointment Confirmed")

hospital = Hospital()

# Successful appointment booking
try:
    hospital.book_appointment("PT101", "Rahul Sharma", "Dr. Reddy", "11:30 AM")
    hospital.display_appointment("PT101")
except (ValueError, DoctorUnavailableError) as e:
    print(f"Error: {e}")

# Invalid case (doctor not available)
try:
    hospital.book_appointment("PT102", "Anita Verma", "Dr. Mehta", "2:00 PM")
    hospital.display_appointment("PT102")
except (ValueError, DoctorUnavailableError) as e:
    print(f"Error: {e}")

#============================================================================================================

# Q9: Food Delivery System

class FoodUnavailableError(Exception):
    pass

class FoodOrder:
    def __init__(self):
        self.orders = {}

    def place_order(self, cust_name, restaurant, food_item, qty):
        if qty <= 0:
            raise ValueError("Invalid quantity.")
        if food_item not in ["Pizza", "Biryani", "Burger"]:
            raise FoodUnavailableError("Selected food item is unavailable.")
        self.orders[cust_name] = {"restaurant": restaurant, "food": food_item, "qty": qty}

    def display_order(self, cust_name):
        order = self.orders.get(cust_name)
        if order:
            print("-----------------------------------------")
            print("Food Order Details")
            print("-----------------------------------------")
            print(f"Customer Name : {cust_name}")
            print(f"Restaurant : {order['restaurant']}")
            print(f"Food Item : {order['food']}")
            print(f"Quantity : {order['qty']}")
            print("Order Status : Confirmed")

order_system = FoodOrder()

# Successful order
try:
    order_system.place_order("Arjun", "Paradise", "Biryani", 2)
    order_system.display_order("Arjun")
except (ValueError, FoodUnavailableError) as e:
    print(f"Error: {e}")

# Invalid case 
try:
    order_system.place_order("Rahul", "Dominos", "Pasta", 1)
    order_system.display_order("Rahul")
except (ValueError, FoodUnavailableError) as e:
    print(f"Error: {e}")
        
#============================================================================================================

# Q10: Online Examination System

class StudentNotRegisteredError(Exception):
    pass

class OnlineExam:
    def __init__(self, student_id, student_name, exam_name, marks=None):
        self.student_id = student_id
        self.student_name = student_name
        self.exam_name = exam_name
        self.marks = marks

    def submit_exam(self, marks):
        # Validate marks
        if not isinstance(marks, (int, float)):
            raise ValueError("Marks must be a number.")
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100.")
        self.marks = marks

    def calculate_result(self):
        # Pass/Fail logic
        result = "PASS" if self.marks >= 40 else "FAIL"

        # Grade calculation
        if self.marks >= 90:
            grade = "A"
        elif self.marks >= 75:
            grade = "B"
        elif self.marks >= 50:
            grade = "C"
        else:
            grade = "D"

        return result, grade

    def display_result(self):
        try:
            result, grade = self.calculate_result()
            print("-----------------------------------------")
            print("Examination Result")
            print("-----------------------------------------")
            print(f"Student ID : {self.student_id}")
            print(f"Student Name : {self.student_name}")
            print(f"Exam Name : {self.exam_name}")
            print(f"Marks : {self.marks}")
            print(f"Result : {result}")
            print(f"Grade : {grade}")
        except (ValueError, StudentNotRegisteredError) as e:
            print(f"Error: {e}")



try:
    exam1 = OnlineExam("ST105", "Sai Ram", "Python Programming")
    exam1.submit_exam(91)   # Valid marks
    exam1.display_result()

    exam2 = OnlineExam("ST106", "Rahul", "Java Programming")
    exam2.submit_exam(120)  # Invalid marks
    exam2.display_result()

    exam3 = OnlineExam("ST107", "Mehul", "Java Programming")
    exam3.submit_exam(-12)  # Invalid marks
    exam3.display_result()
    
except Exception as e:
    print(f"Error: {e}")
    
    