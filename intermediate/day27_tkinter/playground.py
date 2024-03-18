# Unlimited positional arguments: *args
# Puts all of the arguments into a tuple to be used within the function
def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(1, 2, 3, 4, 5))


# Unlimited keyword arguments: **kwargs
def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(calculate(2, add=3, multiply=5))


# Use in a class
class Car:
    def __init__(self, seats=4, **kw):
        # .get will either return the value or nothing, but doesn't error out.
        self.seats = seats
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(seats=10, make="Thingy", model="GT-R")
print(my_car.model)
print(my_car.seats)
