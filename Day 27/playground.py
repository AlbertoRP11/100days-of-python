# Default values for arguments
# def add(a=1, b=2, c=3):
#     print(a + b + c)

# Unlimited Arguments
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     print(sum)
# add(7, 8, 9)

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

# calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")


my_car = Car(make="Nissan", model="GTR")
print(my_car.make)
