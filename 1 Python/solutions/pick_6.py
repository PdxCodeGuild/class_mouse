import random

# Generate a list of 6 random numbers representing the winning tickets
def num_matches(winning, current):
    matches = 0
    for i in range(len(winning)):
        if winning[i] == current[i]:
            matches += 1
    return matches

def generate_ticket():
    ticket = []
    for i in range(6):
        num = random.randint(1,99)
        while num in ticket:
            num = random.randint(1,99)
        ticket.append(num)

    return ticket

    # return [random.randint(1,99) for i in range(6)]

winning_ticket = generate_ticket()
power_ball = random.randint(0,99)
# Start your balance at 0
balance = 0
expenses = 0
earnings = 0
occurrences = {} 

# Loop 100,000 times, for each loop:
for x in range(100000):
# Generate a list of 6 random numbers representing the ticket
    current_ticket = generate_ticket()
    current_power_ball = random.randint(0,99)

# Subtract 2 from your balance (you bought a ticket)
    balance -= 2
    expenses += 2

# Find how many numbers match
    matches = num_matches(winning_ticket, current_ticket)

    if matches not in occurrences:
        occurrences[matches] = 1
    else:
        occurrences[matches] += 1


# Add to your balance the winnings from your matches
    winnings = {
        0: 0,
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: 1000000,
        6: 25000000
    }

    if current_power_ball == power_ball:
        balance += winnings[matches] * 2
        earnings += winnings[matches] * 2
    else:
        balance += winnings[matches]
        earnings += winnings[matches]



# After the loop, print the final balance
for t in occurrences:
    print(f"{t} matched {occurrences[t]} times.")

print(f"${balance}")
print(f"ROI: {((earnings - expenses)/expenses)*100}%")