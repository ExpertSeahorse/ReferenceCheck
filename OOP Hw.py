class Line:
    def __init__(self, coor1, coor2):
        self.cord1 = coor1
        self.cord2 = coor2

        self.x1, self.y1 = self.cord1
        self.x2, self.y2 = self.cord2

    def distance(self):
        return ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**.5

    def slope(self):
        return ((self.y2 - self.y1) / (self.x2 - self.x1))


a = (3, 11)
b = (-9, 100)
ab = Line(a, b)

print(ab.distance())
print(ab.slope())

print()
print()
print()
print()


########################################################################################################################
class Cylinder:
    def __init__(self, radius =1, height = 1):
        self.height = height
        self.radius = radius

    def volume(self):
        return 3.14 * self.radius**2 * self.height

    def surface_area(self):
        return 2 * (3.14 * self.radius * self.height) + 2 * 3.14 * self.radius**2


c= Cylinder(2, 3)
print(c.volume())
print(c.surface_area())

print()
print()
print()
print()


########################################################################################################################
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"{self.owner} has {self.balance} in this account"

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Funds")


acct1 = Account("Joey", 10000)
print(acct1)
acct1.deposit(4000)
print(acct1)
acct1.withdraw(3465)
print(acct1)
acct1.withdraw(10000000000)
print(acct1)
