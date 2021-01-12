import random
import string
import time

class Person:
    def __init__(self, name="", age=None):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age}"

    def __len__(self):
        return len(self.name)


# human = Person("brad", 37)
# alien = Person()

# print(human.name)
# print(alien.name)

# print(human)
# print(alien)

# if len(human) > len(alien):
#     print("Human is better")

# alien.name = "alf"
# alien.age = 400

# print(alien)


class PlayingCard:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"


# suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
# values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

# deck = []
# for suit in suits:
#     for value in values:
#         deck.append(PlayingCard(suit, value))

# for card in deck:
#     print(card)

# print(random.choice(deck))



class Car:
    def __init__(self, make, model, year, drive, seats):
        self.make = make
        self.model = model
        self.year = year
        self.drive = drive
        self.color = random.choice(["red", "white", "gray", "blue", "black", "tan"])
        self.type = random.choice(["truck", "sedan", "coupe", "suv", "hatchback"])
        self.vin = "".join([random.choice(string.ascii_uppercase + string.digits) for x in range(16)])
        self.seats = seats
        self.fuel_level = 100
        self.mpg = 30

    def drive_car(self, distance):
        self.fuel_level -= distance * self.mpg

    def refuel(self):
        self.fuel_level = 100

    def __str__(self):
        return self.make + " " + self.model + " " + str(self.year)

betty = Car("hyundai", "genesis", 2050, "rear", 4)

# while True:
#     time.sleep(1)
#     print(betty.fuel_level)
#     betty.drive_car(2)
#     if betty.fuel_level < 20:
#         print("Getting fuel")
#         betty.refuel()

print(betty)
