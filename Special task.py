# Gautam Special Task

# 1. Program to Create a Student Management System

class Students:
        def __init__(self,student_name,roll_number,marks):
            self.student_name = student_name
            self.roll_number = roll_number
            self.marks = marks

        def display(self):
            print("Name : ",self.student_name)
            print("Roll_Number : ",self.roll_number)
            
        
        def grade(self):
            if(self.marks >= 90):
                print("Grade : A")
            elif(self.marks >= 75):
                print("Grade : B")
            elif(self.marks >= 50):
                print("Grade : C")
            else:
                print("Grade : Fail")


s = Students("Gautam",67,93)
s.display()
s.grade()
s = Students("Ravi",56,85)
s.display()
s.grade()
s = Students("Anu",97,48)
s.display()
s.grade()


# 2. Program to Design a Bank Account System

class BankAccount:

    def __init__(self, ac_name, balance):
        self.ac_name = ac_name
        self.balance = balance

    def deposite(self, amount):
        self.balance += amount
        print(f"deposited: {amount}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw : {amount}")
        else:
            print("Your balance is insufficient")

    def display_balance(self):
        print(f"Balance : {self.balance}")

B1 = BankAccount("Diksha", 16000)
B1.withdraw(500)
B1.display_balance()

B2 = BankAccount("Anushree",11000)
B2.withdraw(1500)
B2.display_balance()
        
B3 = BankAccount("Umawati",50000)
B3.deposite(200)
B3.display_balance()


# 3. Program to Build a Product Billing System

class Products:
    
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def calculate_total(self):
        return self.price * self.qty
    
    def display_bill(self):
        total = self.calculate_total()
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.qty}")
        print(f"Total =  {total}")

P1 = Products("Laptop",50000,1)
P1.display_bill()
        
P2 = Products("Mobile",20000,2)
P2.display_bill()

P3 = Products("Pen",10,5)
P3.display_bill()


# 4. Program to Create an Employee Salary System

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def final_sal(self):
        bonus = self.salary * 0.10
        return self.salary + bonus
         
    def display(self):
        final_salary = self.final_sal()
        print(f"Name: {self.name} ")
        print(f"final Salary = {int(final_salary)}")

E1 = Employee("Sairam", 10000)
E1.display()

E2 = Employee("Raghu", 20000)
E2.display()

E3 = Employee("Vinayak", 5000)
E3.display()


# 5. Program to Create a Car Information System

class Car:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def discount_price(self):
        discount = self.price * 0.05
        return self.price - discount
    
    def display(self):
        discounted_price = self.discount_price()
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Original price: {self.price}")
        print(f"Discounted_price = {int(discounted_price)}")

        
C1 = Car("Toyota", "Innova", 2000000)    
C1.display()

C2 = Car("Hyundai", "i20", 800000)    
C2.display()

C3 = Car("Tata", "Nexon", 1000000)    
C3.display()

