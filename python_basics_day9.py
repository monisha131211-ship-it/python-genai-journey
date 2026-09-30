# Example 2: Abstraction with multiple child classes
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

CreditCard().pay(500)
UPI().pay(200)

# Example 3: Abstraction hiding internal details
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connected to MySQL Database")

db = MySQLDatabase()
db.connect()
