# Gautam Task 6

# -------------------------------------------------------

# Q 1: Online Payment Gateway System (Basic)

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

    @abstractmethod
    def payment_status(self):
        pass


class CreditCardPayment(Payment):
    def make_payment(self, amount):
        self.amount = amount
        print("Payment Method : Credit Card")
        print(f"Amount Paid    : ₹{self.amount}")

    def payment_status(self):
        print("Status         : Payment Successful\n")


class DebitCardPayment(Payment):
    def make_payment(self, amount):
        self.amount = amount
        print("Payment Method : Debit Card")
        print(f"Amount Paid    : ₹{self.amount}")

    def payment_status(self):
        print("Status         : Payment Successful\n")


class UpiPayment(Payment):
    def make_payment(self, amount):
        self.amount = amount
        print("Payment Method : UPI")
        print(f"Amount Paid    : ₹{self.amount}")

    def payment_status(self):
        print("Status         : Payment Successful\n")

print("-----------------------------------------")  # Examples
print("Payment Details")
print("-----------------------------------------\n")

c = CreditCardPayment()
c.make_payment(2500)
c.payment_status()

u = UpiPayment()
u.make_payment(1200)
u.payment_status()

# -------------------------------------------------------

# Q 2: Employee Attendance System (Beginner)

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def working_hours(self):
        pass


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 55000

    def working_hours(self):
        return "8 Hours"


class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return 22000

    def working_hours(self):
        return "4 Hours"


class ContractEmployee(Employee):
    def calculate_salary(self):
        return 30000

    def working_hours(self):
        return "6 Hours"

print("-----------------------------------------")   # Examples
print("Employee Details")
print("-----------------------------------------\n")

f = FullTimeEmployee()
print("Employee Type      : Full Time")
print(f"Working Hours      : {f.working_hours()}")
print(f"Monthly Salary     : ₹{f.calculate_salary():,}\n")

p = PartTimeEmployee()
print("Employee Type      : Part Time")
print(f"Working Hours      : {p.working_hours()}")
print(f"Monthly Salary     : ₹{p.calculate_salary():,}\n")

# -------------------------------------------------------

# Q 3: Food Delivery Application (Intermediate)

from abc import ABC, abstractmethod

class Restaurant(ABC):
    @abstractmethod
    def prepare_food(self):
        pass

    @abstractmethod
    def delivery_time(self):
        pass

    @abstractmethod
    def restaurant_details(self):
        pass


class Dominos(Restaurant):
    def prepare_food(self):
        return "Pizza"

    def delivery_time(self):
        return "30 Minutes"

    def restaurant_details(self):
        return "Dominos"


class KFC(Restaurant):
    def prepare_food(self):
        return "Fried Chicken"

    def delivery_time(self):
        return "25 Minutes"

    def restaurant_details(self):
        return "KFC"


class Paradise(Restaurant):
    def prepare_food(self):
        return "Chicken Biryani"

    def delivery_time(self):
        return "35 Minutes"

    def restaurant_details(self):
        return "Paradise"

print("-----------------------------------------")    # Examples
print("Restaurant Details")
print("-----------------------------------------\n")

p = Paradise()
print(f"Restaurant Name     : {p.restaurant_details()}")
print(f"Food                : {p.prepare_food()}")
print("Preparation Time    : 20 Minutes")
print(f"Delivery Time       : {p.delivery_time()}\n")

# -------------------------------------------------------

# Q 4: Vehicle Rental System (Intermediate)

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def rental_price(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

    @abstractmethod
    def vehicle_details(self):
        pass


class Bike(Vehicle):
    def rental_price(self):
        return "₹500 / Day"

    def fuel_type(self):
        return "Petrol"

    def vehicle_details(self):
        return "Bike"


class Car(Vehicle):
    def rental_price(self):
        return "₹2,500 / Day"

    def fuel_type(self):
        return "Petrol"

    def vehicle_details(self):
        return "Car"


class Bus(Vehicle):
    def rental_price(self):
        return "₹5,000 / Day"

    def fuel_type(self):
        return "Diesel"

    def vehicle_details(self):
        return "Bus"

print("-----------------------------------------")   # Examples
print("Vehicle Details")
print("-----------------------------------------\n")

c = Car()
print(f"Vehicle Type      : {c.vehicle_details()}")
print(f"Fuel Type         : {c.fuel_type()}")
print(f"Rental Price      : {c.rental_price()}\n")

# -------------------------------------------------------

# Q 5: Hospital Management System (Advanced)

from abc import ABC, abstractmethod

class Doctor(ABC):
    @abstractmethod
    def doctor_details(self):
        pass

    @abstractmethod
    def consultation_fee(self):
        pass

    @abstractmethod
    def available_timings(self):
        pass

    @abstractmethod
    def treatment(self):
        pass


class Cardiologist(Doctor):
    def doctor_details(self):
        return "Dr. Sharma"

    def consultation_fee(self):
        return 1500

    def available_timings(self):
        return "10:00 AM - 2:00 PM"

    def treatment(self):
        return "Heart Diseases"


class Neurologist(Doctor):
    def doctor_details(self):
        return "Dr. Rao"

    def consultation_fee(self):
        return 1800

    def available_timings(self):
        return "2:00 PM - 6:00 PM"

    def treatment(self):
        return "Brain & Nervous System Disorders"


class Orthopedic(Doctor):
    def doctor_details(self):
        return "Dr. Mehta"

    def consultation_fee(self):
        return 1200

    def available_timings(self):
        return "11:00 AM - 3:00 PM"

    def treatment(self):
        return "Bone & Joint Problems"

print("-----------------------------------------")      # Examples
print("Doctor Details")
print("-----------------------------------------\n")

c = Cardiologist()
print("Department          : Cardiology")
print(f"Doctor Name         : {c.doctor_details()}")
print(f"Consultation Fee    : ₹{c.consultation_fee():,}")
print(f"Available Time      : {c.available_timings()}")
print(f"Treatment           : {c.treatment()}\n")

n = Neurologist()
print("Department          : Neurology")
print(f"Doctor Name         : {n.doctor_details()}")
print(f"Consultation Fee    : ₹{n.consultation_fee():,}")
print(f"Available Time      : {n.available_timings()}")
print(f"Treatment           : {n.treatment()}\n")

