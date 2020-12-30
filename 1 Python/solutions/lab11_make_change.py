coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]

# coins = {
#     "half-dollar": 50,
# }


num_coins = []

pennies = input("Enter dollar amount $")
pennies = float(pennies)

pennies *= 100

pennies = int(pennies)

for coin in coins:
    name = coin[0]
    value = coin[1]
    quantity = (name, pennies // value)
    pennies -= value * quantity[1]
    num_coins.append(quantity)


for coin in num_coins:
    print(f"{coin[0]}: {coin[1]}")