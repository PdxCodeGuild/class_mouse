coins = {
    "half-dollar": 50,
    "quaters": 25,
    "dimes": 10,
    "nickels": 5,
    "pennies": 1
}


num_coins = {}

pennies = input("Enter dollar amount $")
pennies = float(pennies)

pennies *= 100

pennies = int(pennies)

for name in coins:
    value = coins[name]
    quantity = pennies // value
    num_coins[name] = quantity
    pennies -= quantity * value

for name in num_coins:
    print(f"{name}: {num_coins[name]}")