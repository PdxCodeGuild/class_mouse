cards = {
    'A': 1,
    "J": 10,
    "Q": 10,
    "K": 10
}

users_cards = input("Enter 3 cards separated by commas: ").upper()
users_cards = users_cards.replace(" ", "")
users_cards = users_cards.split(",")

total = 0
# aces = 0
for card in users_cards:
    # if card == "A":
    #     aces += 1
    value = cards.get(card, card)
    value = int(value)
    total += value

if "A" in users_cards:
    if total + 10 <= 21:
        total += 10

# for x in range(aces):
#     if total + 10 <= 21:
#         total += 10

print(total)
if total < 17:
    print("You should hit")
elif total < 21:
    print("You should stay")
elif total == 21:
    print("Blackjack!!!")
else:
    print("Busted :(")