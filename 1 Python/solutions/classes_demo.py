import random

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


suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

deck = []
for suit in suits:
    for value in values:
        deck.append(PlayingCard(suit, value))

# for card in deck:
#     print(card)

print(random.choice(deck))