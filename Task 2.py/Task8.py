# Gautam Task 8

# -------------------------------------------------------

# Q 1: Online Payment System (Method Overriding)

class Payment:
    def make_payment(self, amount):
        print("Generic Payment Process")


class CreditCardPayment(Payment):
    def make_payment(self, amount):
        print("-----------------------------------------")
        print("Payment Details")
        print("-----------------------------------------")
        print("Payment Method : Credit Card")
        print(f"Amount         : ₹{amount}")
        print("Status         : Payment Successful\n")


class DebitCardPayment(Payment):
    def make_payment(self, amount):
        print("-----------------------------------------")
        print("Payment Details")
        print("-----------------------------------------")
        print("Payment Method : Debit Card")
        print(f"Amount         : ₹{amount}")
        print("Status         : Payment Successful\n")


class UpiPayment(Payment):
    def make_payment(self, amount):
        print("-----------------------------------------")
        print("Payment Details")
        print("-----------------------------------------")
        print("Payment Method : UPI")
        print(f"Amount         : ₹{amount}")
        print("Status         : Payment Successful\n")


# Examples
c = CreditCardPayment()
c.make_payment(2500)

u = UpiPayment()
u.make_payment(850)

# -------------------------------------------------------

# Q 2: Employee Salary Management (Method Overriding)

class Employee:
    def calculate_salary(self):
        print("Generic Salary Calculation")


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("-----------------------------------------")
        print("Employee Salary Details")
        print("-----------------------------------------")
        print("Employee Type      : Full Time")
        print("Salary             : ₹60,000\n")


class PartTimeEmployee(Employee):
    def calculate_salary(self):
        print("-----------------------------------------")
        print("Employee Salary Details")
        print("-----------------------------------------")
        print("Employee Type      : Part Time")
        print("Salary             : ₹25,000\n")


class ContractEmployee(Employee):
    def calculate_salary(self):
        print("-----------------------------------------")
        print("Employee Salary Details")
        print("-----------------------------------------")
        print("Employee Type      : Contract")
        print("Salary             : ₹40,000\n")


# Examples
f = FullTimeEmployee()
f.calculate_salary()

p = PartTimeEmployee()
p.calculate_salary()

c = ContractEmployee()
c.calculate_salary()

# -------------------------------------------------------

# Q 3: Vehicle Information System (Duck Typing)

class Car:
    def vehicle_info(self):
        print("-----------------------------------------")
        print("Vehicle Information")
        print("-----------------------------------------")
        print("Vehicle Type   : Car")
        print("Brand          : Hyundai")
        print("Fuel           : Petrol\n")


class Bike:
    def vehicle_info(self):
        print("-----------------------------------------")
        print("Vehicle Information")
        print("-----------------------------------------")
        print("Vehicle Type   : Bike")
        print("Brand          : Honda")
        print("Fuel           : Petrol\n")


class Bus:
    def vehicle_info(self):
        print("-----------------------------------------")
        print("Vehicle Information")
        print("-----------------------------------------")
        print("Vehicle Type   : Bus")
        print("Brand          : Volvo")
        print("Fuel           : Diesel\n")


# Duck Typing Function
def display_vehicle(vehicle):
    vehicle.vehicle_info()


# Examples
display_vehicle(Car())
display_vehicle(Bike())
display_vehicle(Bus())

# -------------------------------------------------------

# Q 4: Notification System (Method Overriding)

class Notification:
    def send_notification(self):
        print("Generic Notification")


class EmailNotification(Notification):
    def send_notification(self):
        print("-----------------------------------------")
        print("Notification Details")
        print("-----------------------------------------")
        print("Notification Type : Email")
        print("Status            : Sent Successfully\n")


class SMSNotification(Notification):
    def send_notification(self):
        print("-----------------------------------------")
        print("Notification Details")
        print("-----------------------------------------")
        print("Notification Type : SMS")
        print("Status            : Sent Successfully\n")


class WhatsAppNotification(Notification):
    def send_notification(self):
        print("-----------------------------------------")
        print("Notification Details")
        print("-----------------------------------------")
        print("Notification Type : WhatsApp")
        print("Status            : Sent Successfully\n")


# Examples
EmailNotification().send_notification()
SMSNotification().send_notification()
WhatsAppNotification().send_notification()

# -------------------------------------------------------

# Q 5: Food Delivery System (Method Overriding + Duck Typing)

class Dominos:
    def order_food(self):
        print("-----------------------------------------")
        print("Food Order Details")
        print("-----------------------------------------")
        print("Restaurant      : Dominos")
        print("Food Ordered    : Veg Pizza")
        print("Status          : Order Confirmed\n")


class KFC:
    def order_food(self):
        print("-----------------------------------------")
        print("Food Order Details")
        print("-----------------------------------------")
        print("Restaurant      : KFC")
        print("Food Ordered    : Chicken Bucket")
        print("Status          : Order Confirmed\n")


class Paradise:
    def order_food(self):
        print("-----------------------------------------")
        print("Food Order Details")
        print("-----------------------------------------")
        print("Restaurant      : Paradise")
        print("Food Ordered    : Chicken Biryani")
        print("Status          : Order Confirmed\n")


# Duck Typing Function
def place_order(restaurant):
    restaurant.order_food()


# Examples
place_order(Dominos())
place_order(KFC())
place_order(Paradise())
