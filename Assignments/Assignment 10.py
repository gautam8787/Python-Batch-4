#Gautam Assignment 10

# -----------------------------------------------------------------

# 1. password checker 

def password_checker(password):
    is_upper = 0
    is_lower = 0
    is_digit = 0
    is_special = 0

    special_chars = "@#$%!&*"

    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."

    for char in password:
        if char.isupper():
            is_upper += 1
        elif char.islower():
            is_lower  += 1
        elif char.isdigit():
            is_digit  += 1
        elif char in special_chars:
            is_special  += 1

    if all([is_upper, is_lower, is_digit, is_special]):
        return "Strong Password"
    else:
        return "Weak Password"


# Example
print(password_checker("Test@123"))

# -------------------------------------------------------

#2. Log file analyzer

logs = [
    "INFO: User logged in",
    "ERROR: Database connection failed",
    "WARNING: Disk space low",
    "INFO: File uploaded",
    "ERROR: Timeout occurred"
]

log_counts = {}
unique_levels = set()

for log in logs:
    level = log.split(":")[0]
    unique_levels.add(level)
    log_counts[level] = log_counts.get(level, 0) + 1

print("Log Counts:", log_counts)
print("Unique Levels:", unique_levels)

# -------------------------------------------------------

#3. simple payment system

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid using Credit Card.")

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI.")

# Demonstration
payment1 = CreditCardPayment()
payment2 = UPIPayment()

payment1.pay(500)
payment2.pay(300)

# -------------------------------------------------------

#4. database connection class 

class DatabaseConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        print(f"Connecting to database at {host}:{port}")

class MySQLDatabase(DatabaseConnection):
    def __init__(self, host, port, username, password):
        super().__init__(host, port)
        self.username = username
        self.password = password
        print(f"MySQL connection established with user {username}")

# Example
db = MySQLDatabase("localhost", 3306, "root", "admin123")

# -------------------------------------------------------

#5. using *args and *kwargs for API request builder

def apirequestbuilder( *args, **kwargs):
    print("Positional Parameters:", args)
    print("Query Parameters:", kwargs)

# Example
apirequestbuilder( "param1", "param2", id=101, name="Gautam")

# -------------------------------------------------------

#6. product price calculator 

def calculate_price(price, tax=10, discount=0):
    final_price = (price - discount) + (price * tax / 100)
    return final_price

# Example
print("Final Price:", calculate_price(1000, discount=100))
print("Final Price:", calculate_price(500, tax=5))

# -------------------------------------------------------

#7. logging frameworks 

class FileLogger:
    def log(self, message):
        print(f"Logging to file: {message}")

class ConsoleLogger:
    def log(self, message):
        print(f"Logging to console: {message}")

def log_message(logger, message):
    logger.log(message)  # Duck typing

# Example
file_logger = FileLogger()
console_logger = ConsoleLogger()

log_message(file_logger, "File log entry")
log_message(console_logger, "Console log entry")


