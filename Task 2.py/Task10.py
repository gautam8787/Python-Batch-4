# Gautam Task 10

# -------------------------------------------------------

# Q 1: Student Record Management System

import os

class StudentRecord:
    FILE = "students.txt"

    def add_student(self, sid, name, course, marks):
        try:
            if marks < 0 or marks > 100:
                raise ValueError("Invalid marks.")
            with open(self.FILE, "a") as f:
                f.write(f"{sid},{name},{course},{marks}\n")
            print("Record Saved Successfully.")
        except Exception as e:
            print("Error:", e)

    def view_students(self):
        try:
            if not os.path.exists(self.FILE):
                raise FileNotFoundError("File not found.")
            with open(self.FILE, "r") as f:
                data = f.readlines()
            if not data:
                raise Exception("Empty file.")
            for line in data:
                sid, name, course, marks = line.strip().split(",")
                print(f"Student ID: {sid}, Name: {name}, Course: {course}, Marks: {marks}")
        except Exception as e:
            print("Error:", e)

    def search_student(self, sid):
        try:
            with open(self.FILE, "r") as f:
                for line in f:
                    s, n, c, m = line.strip().split(",")
                    if s == sid:
                        print("Student Found Successfully.")
                        print(f"Student ID: {s}, Name: {n}, Course: {c}, Marks: {m}")
                        return
            raise Exception("Student record not found.")
        except Exception as e:
            print("Error:", e)

sr = StudentRecord()      # Example
sr.add_student("ST101", "Sai Ram", "Python Full Stack", 95)
sr.view_students()
sr.search_student("ST101")

# -------------------------------------------------------

# Q 2: Employee Payroll Management System

import os

class EmployeePayroll:
    FILE = "employees.txt"

    def add_employee(self, eid, name, dept, designation, salary):
        try:
            if salary <= 0:
                raise ValueError("Invalid salary.")
            with open(self.FILE, "a") as f:
                f.write(f"{eid},{name},{dept},{designation},{salary}\n")
            print("Employee Added Successfully.")
        except Exception as e:
            print("Error:", e)

    def search_employee(self, eid):
        try:
            with open(self.FILE, "r") as f:
                for line in f:
                    e, n, d, des, s = line.strip().split(",")
                    if e == eid:
                        print("Employee Found Successfully.")
                        print(f"Employee ID: {e}, Name: {n}, Dept: {d}, Designation: {des}, Salary: ₹{s}")
                        return
            raise Exception("Employee record not found.")
        except Exception as e:
            print("Error:", e)

ep = EmployeePayroll()     # Example
ep.add_employee("EMP101", "Rahul Sharma", "IT", "Python Developer", 60000)
ep.search_employee("EMP101")

# -------------------------------------------------------

# Q 3: Library Management System

import os

class Library:
    FILE = "books.txt"

    def add_book(self, bid, name, author, publisher, copies):
        try:
            if copies < 0:
                raise ValueError("Invalid copies.")
            with open(self.FILE, "a") as f:
                f.write(f"{bid},{name},{author},{publisher},{copies}\n")
            print("Book Added Successfully.")
        except Exception as e:
            print("Error:", e)

    def issue_book(self, bid):
        try:
            lines = []
            found = False
            with open(self.FILE, "r") as f:
                lines = f.readlines()
            with open(self.FILE, "w") as f:
                for line in lines:
                    b, n, a, p, c = line.strip().split(",")
                    if b == bid:
                        if int(c) <= 0:
                            raise Exception("Requested book is currently unavailable.")
                        c = str(int(c) - 1)
                        found = True
                        print("Book Issued Successfully.")
                        print(f"Remaining Copies: {c}")
                    f.write(f"{b},{n},{a},{p},{c}\n")
            if not found:
                raise Exception("Book not found.")
        except Exception as e:
            print("Error:", e)

lib = Library()       # Example
lib.add_book("BK101", "Python Programming", "Guido Rossum", "O'Reilly", 8)
lib.issue_book("BK101")

# -------------------------------------------------------

# Q 4: Banking Transaction Management System

import os

class BankAccount:
    FILE = "accounts.txt"
    TRANS_FILE = "transactions.txt"

    def create_account(self, acc_no, holder, acc_type, balance):
        with open(self.FILE, "a") as f:
            f.write(f"{acc_no},{holder},{acc_type},{balance}\n")
        print("Account Created Successfully.")

    def deposit(self, acc_no, amount):
        try:
            if amount <= 0:
                raise ValueError("Invalid deposit amount.")
            lines = []
            with open(self.FILE, "r") as f:
                lines = f.readlines()
            with open(self.FILE, "w") as f:
                for line in lines:
                    a, h, t, b = line.strip().split(",")
                    if a == acc_no:
                        b = str(int(b) + amount)
                        print(f"Deposit Amount: ₹{amount}, Current Balance: ₹{b}")
                        with open(self.TRANS_FILE, "a") as tf:
                            tf.write(f"{acc_no},Deposit,{amount},{b}\n")
                    f.write(f"{a},{h},{t},{b}\n")
        except Exception as e:
            print("Error:", e)

ba = BankAccount()    # Example
ba.create_account("123456789", "Sai Ram", "Savings", 75000)
ba.deposit("123456789", 10000)

# -------------------------------------------------------

# Q 5: Inventory Management System

import os

class Inventory:
    FILE = "inventory.txt"

    def add_product(self, pid, name, category, price, qty):
        try:
            if qty < 0:
                raise ValueError("Invalid quantity.")
            with open(self.FILE, "a") as f:
                f.write(f"{pid},{name},{category},{price},{qty}\n")
            print("Product Added Successfully.")
        except Exception as e:
            print("Error:", e)

    def update_stock(self, pid, qty):
        try:
            lines = []
            with open(self.FILE, "r") as f:
                lines = f.readlines()
            with open(self.FILE, "w") as f:
                found = False
                for line in lines:
                    p, n, c, pr, q = line.strip().split(",")
                    if p == pid:
                        q = str(int(q) + qty)
                        found = True
                        print("Inventory Updated Successfully.")
                        print(f"New Quantity: {q}")
                    f.write(f"{p},{n},{c},{pr},{q}\n")
                if not found:
                    raise Exception("Product not found.")
        except Exception as e:
            print("Error:", e)

inv = Inventory()    # Example
inv.add_product("P101", "Mechanical Keyboard", "Electronics", 2500, 25)
inv.update_stock("P101", -5)

# -------------------------------------------------------

# Q 6: Hospital Management System

import os

class HospitalManagement:
    FILE = "patients.txt"

    def add_patient(self, pid, name, age, gender, disease, doctor, date):
        try:
            if age <= 0:
                raise ValueError("Invalid age.")
            with open(self.FILE, "a") as f:
                f.write(f"{pid},{name},{age},{gender},{disease},{doctor},{date}\n")
            print("Record Saved Successfully.")
        except Exception as e:
            print("Error:", e)

    def display_patients(self):
        try:
            if not os.path.exists(self.FILE):
                raise FileNotFoundError("File not found.")
            with open(self.FILE, "r") as f:
                data = f.readlines()
            if not data:
                raise Exception("Empty file.")
            for line in data:
                pid, name, age, gender, disease, doctor, date = line.strip().split(",")
                print(f"Patient ID: {pid}, Name: {name}, Age: {age}, Disease: {disease}, Doctor: {doctor}, Date: {date}")
        except Exception as e:
            print("Error:", e)

    def search_patient(self, pid):
        try:
            with open(self.FILE, "r") as f:
                for line in f:
                    p, n, a, g, d, doc, dt = line.strip().split(",")
                    if p == pid:
                        print("Patient Found Successfully.")
                        print(f"Patient ID: {p}, Name: {n}, Age: {a}, Disease: {d}, Doctor: {doc}, Date: {dt}")
                        return
            raise Exception("Patient record not found.")
        except Exception as e:
            print("Error:", e)

    def update_patient(self, pid, disease):
        try:
            lines = []
            with open(self.FILE, "r") as f:
                lines = f.readlines()
            found = False
            with open(self.FILE, "w") as f:
                for line in lines:
                    p, n, a, g, d, doc, dt = line.strip().split(",")
                    if p == pid:
                        d = disease
                        found = True
                        print("Patient Record Updated Successfully.")
                    f.write(f"{p},{n},{a},{g},{d},{doc},{dt}\n")
            if not found:
                raise Exception("Patient not found.")
        except Exception as e:
            print("Error:", e)

    def discharge_patient(self, pid):
        try:
            lines = []
            with open(self.FILE, "r") as f:
                lines = f.readlines()
            found = False
            with open(self.FILE, "w") as f:
                for line in lines:
                    p, *_ = line.strip().split(",")
                    if p == pid:
                        found = True
                        continue
                    f.write(line)
            if found:
                print("Patient Discharged Successfully.")
            else:
                raise Exception("Patient not found.")
        except Exception as e:
            print("Error:", e)

hm = HospitalManagement()   # Example
hm.add_patient("PT101", "Rahul Sharma", 35, "Male", "Dengue", "Dr. Reddy", "15-07-2026")
hm.display_patients()
hm.search_patient("PT101")
hm.update_patient("PT101", "Recovered")
hm.discharge_patient("PT101")

# -------------------------------------------------------

# Q 7: Hotel Reservation Management System

import os

class HotelReservation:
    FILE = "bookings.txt"

    def book_room(self, bid, name, room_no, room_type, checkin, checkout):
        try:
            with open(self.FILE, "r") as f:
                for line in f:
                    b, n, r, rt, ci, co = line.strip().split(",")
                    if r == room_no:
                        raise Exception("Room is already booked.")
            with open(self.FILE, "a") as f:
                f.write(f"{bid},{name},{room_no},{room_type},{checkin},{checkout}\n")
            print("Booking Confirmed Successfully.")
        except FileNotFoundError:
            with open(self.FILE, "w") as f:
                f.write(f"{bid},{name},{room_no},{room_type},{checkin},{checkout}\n")
            print("Booking Confirmed Successfully.")
        except Exception as e:
            print("Error:", e)

    def display_bookings(self):
        try:
            with open(self.FILE, "r") as f:
                for line in f:
                    b, n, r, rt, ci, co = line.strip().split(",")
                    print(f"Booking ID: {b}, Name: {n}, Room: {r}, Type: {rt}, Check-In: {ci}, Check-Out: {co}")
        except Exception as e:
            print("Error:", e)



hr = HotelReservation()    # Example
hr.book_room("BK101", "Sai Ram", "305", "Deluxe", "20-07-2026", "23-07-2026")
hr.display_bookings()

# -------------------------------------------------------

# Q 8: Online Shopping Management System

import os

class OnlineShopping:
    FILE = "orders.txt"

    def place_order(self, oid, name, product, qty, price, status):
        try:
            if qty <= 0:
                raise ValueError("Invalid quantity.")
            if price <= 0:
                raise ValueError("Invalid price.")
            with open(self.FILE, "a") as f:
                f.write(f"{oid},{name},{product},{qty},{price},{status}\n")
            print("Order Placed Successfully.\n")
        except Exception as e:
            print("Error:", e)

    def display_orders(self):
        try:
            if not os.path.exists(self.FILE):
                raise FileNotFoundError("File not found.")
            with open(self.FILE, "r") as f:
                data = f.readlines()
            if not data:
                raise Exception("No orders found.")
            for line in data:
                oid, name, product, qty, price, status = line.strip().split(",")
                print("-----------------------------------------")
                print("Online Shopping System")
                print("-----------------------------------------")
                print(f"Order ID          : {oid}")
                print(f"Customer Name     : {name}")
                print(f"Product           : {product}")
                print(f"Quantity          : {qty}")
                print(f"Price             : ₹{price}")
                print(f"Order Status      : {status}\n")
        except Exception as e:
            print("Error:", e)

    def search_order(self, oid):
        try:
            with open(self.FILE, "r") as f:
                for line in f:
                    o, n, p, q, pr, s = line.strip().split(",")
                    if o == oid:
                        print("Order Found Successfully.\n")
                        print("-----------------------------------------")
                        print("Online Shopping System")
                        print("-----------------------------------------")
                        print(f"Order ID          : {o}")
                        print(f"Customer Name     : {n}")
                        print(f"Product           : {p}")
                        print(f"Quantity          : {q}")
                        print(f"Price             : ₹{pr}")
                        print(f"Order Status      : {s}\n")
                        return
            raise Exception("Order not found.")
        except Exception as e:
            print("Error:", e)

    def update_order_status(self, oid, new_status):
        try:
            lines = []
            with open(self.FILE, "r") as f:
                lines = f.readlines()
            found = False
            with open(self.FILE, "w") as f:
                for line in lines:
                    o, n, p, q, pr, s = line.strip().split(",")
                    if o == oid:
                        s = new_status
                        found = True
                        print("Order Status Updated Successfully.\n")
                    f.write(f"{o},{n},{p},{q},{pr},{s}\n")
            if not found:
                raise Exception("Order not found.")
        except Exception as e:
            print("Error:", e)

    def cancel_order(self, oid):
        try:
            lines = []
            with open(self.FILE, "r") as f:
                lines = f.readlines()
            found = False
            with open(self.FILE, "w") as f:
                for line in lines:
                    o, *_ = line.strip().split(",")
                    if o == oid:
                        found = True
                        continue
                    f.write(line)
            if found:
                print("Order Cancelled Successfully.\n")
            else:
                raise Exception("Order not found.")
        except Exception as e:
            print("Error:", e)


shop = OnlineShopping()    # Example Usage

shop.place_order("ORD101", "Arjun", "Laptop", 1, 75000, "Confirmed")  # Place an order

shop.display_orders()   # Display all orders

shop.search_order("ORD101")    # Search for an order

shop.update_order_status("ORD101", "Shipped")  # Update order status

shop.cancel_order("ORD101")    # Cancel an order

# -------------------------------------------------------

# Q 9: Food Delivery Management System

import os

class FoodDelivery:
    FILE = "food_orders.txt"

    def place_order(self, oid, name, restaurant, food, qty, status):
        try:
            if qty <= 0:
                raise ValueError("Invalid quantity.")
            if restaurant not in ["Paradise", "Dominos", "KFC"]:
                raise Exception("Selected restaurant is unavailable.")
            with open(self.FILE, "a") as f:
                f.write(f"{oid},{name},{restaurant},{food},{qty},{status}\n")
            print("Order Placed Successfully.")
        except Exception as e:
            print("Error:", e)

    def display_orders(self):
        try:
            if not os.path.exists(self.FILE):
                raise FileNotFoundError("File not found.")
            with open(self.FILE, "r") as f:
                data = f.readlines()
            if not data:
                raise Exception("No orders found.")
            for line in data:
                oid, name, rest, food, qty, status = line.strip().split(",")
                print(f"Order ID: {oid}, Customer: {name}, Restaurant: {rest}, Food: {food}, Qty: {qty}, Status: {status}")
        except Exception as e:
            print("Error:", e)

    def search_order(self, oid):
        try:
            with open(self.FILE, "r") as f:
                for line in f:
                    o, n, r, fitem, q, s = line.strip().split(",")
                    if o == oid:
                        print("Order Found Successfully.")
                        print(f"Order ID: {o}, Customer: {n}, Restaurant: {r}, Food: {fitem}, Qty: {q}, Status: {s}")
                        return
            raise Exception("Order not found.")
        except Exception as e:
            print("Error:", e)

    def update_delivery_status(self, oid, new_status):
        try:
            lines = []
            with open(self.FILE, "r") as f:
                lines = f.readlines()
            found = False
            with open(self.FILE, "w") as f:
                for line in lines:
                    o, n, r, fitem, q, s = line.strip().split(",")
                    if o == oid:
                        s = new_status
                        found = True
                        print("Delivery Status Updated Successfully.")
                    f.write(f"{o},{n},{r},{fitem},{q},{s}\n")
            if not found:
                raise Exception("Order not found.")
        except Exception as e:
            print("Error:", e)

    def cancel_order(self, oid):
        try:
            lines = []
            with open(self.FILE, "r") as f:
                lines = f.readlines()
            found = False
            with open(self.FILE, "w") as f:
                for line in lines:
                    o, *_ = line.strip().split(",")
                    if o == oid:
                        found = True
                        continue
                    f.write(line)
            if found:
                print("Order Cancelled Successfully.")
            else:
                raise Exception("Order not found.")
        except Exception as e:
            print("Error:", e)

fd = FoodDelivery()   # Example
fd.place_order("FD101", "Sai Ram", "Paradise", "Chicken Biryani", 2, "Out for Delivery")
fd.display_orders()
fd.search_order("FD101")
fd.update_delivery_status("FD101", "Delivered")
fd.cancel_order("FD101")

# -------------------------------------------------------

# Q 10: Course Registration Management System

import os

class CourseRegistration:
    FILE = "registrations.txt"

    def register_student(self, regid, sid, name, course, trainer, date):
        try:
            if not sid.startswith("ST"):
                raise ValueError("Invalid Student ID.")
            with open(self.FILE, "a") as f:
                f.write(f"{regid},{sid},{name},{course},{trainer},{date}\n")
            print("Registration Successful.")
        except Exception as e:
            print("Error:", e)

    def display_registrations(self):
        try:
            if not os.path.exists(self.FILE):
                raise FileNotFoundError("File not found.")
            with open(self.FILE, "r") as f:
                data = f.readlines()
            if not data:
                raise Exception("Empty registration file.")
            for line in data:
                regid, sid, name, course, trainer, date = line.strip().split(",")
                print(f"RegID: {regid}, StudentID: {sid}, Name: {name}, Course: {course}, Trainer: {trainer}, Date: {date}")
        except Exception as e:
            print("Error:", e)

    def search_registration(self, regid):
        try:
            with open(self.FILE, "r") as f:
                for line in f:
                    r, sid, n, c, t, d = line.strip().split(",")
                    if r == regid:
                        print("Registration Found Successfully.")
                        print(f"RegID: {r}, StudentID: {sid}, Name: {n}, Course: {c}, Trainer: {t}, Date: {d}")
                        return
            raise Exception("Registration record not found.")
        except Exception as e:
            print("Error:", e)

    def update_registration(self, regid, new_course):
        try:
            lines = []
            with open(self.FILE, "r") as f:
                lines = f.readlines()
            found = False
            with open(self.FILE, "w") as f:
                for line in lines:
                    r, sid, n, c, t, d = line.strip().split(",")
                    if r == regid:
                        c = new_course
                        found = True
                        print("Registration Updated Successfully.")
                    f.write(f"{r},{sid},{n},{c},{t},{d}\n")
            if not found:
                raise Exception("Registration not found.")
        except Exception as e:
            print("Error:", e)

    def delete_registration(self, regid):
        try:
            lines = []
            with open(self.FILE, "r") as f:
                lines = f.readlines()
            found = False
            with open(self.FILE, "w") as f:
                for line in lines:
                    r, *_ = line.strip().split(",")
                    if r == regid:
                        found = True
                        continue
                    f.write(line)
            if found:
                print("Registration Deleted Successfully.")
            else:
                raise Exception("Registration not found.")
        except Exception as e:
            print("Error:", e)

cr = CourseRegistration()   # Example
cr.register_student("REG101", "ST101", "Sai Ram", "Python Full Stack", "Rocky Ram", "18-07-2026")  
cr.display_registrations()
cr.search_registration("REG101")
cr.update_registration("REG101", "Data Science")
cr.delete_registration("REG101")

