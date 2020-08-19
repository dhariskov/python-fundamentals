class Vehicle:
    def __init__(self, type, model, price, owner=None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money, owner):
        change = 0
        if money >= self.price and self.owner is None:
            change = money - self.price
            print(f"Successfully bought a {self.type}. Change: {change}")
            self.owner = owner
        else:
            if money < self.price:
                print("Sorry, not enough money")
            if self.owner is not None:
                print("Car already sold")

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            print("Vehicle has no owner")

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
vehicle.buy(20000, "Peter")
vehicle.buy(35000, "George")
print(vehicle)
vehicle.sell()
print(vehicle)


