import random

outcomes = {
    "rockvspaper": "computer",
    "rockvsscissors": "player",
    "papervsscissors": "computer",
    "papervsrock": "player",
    "scissorsvsrock": "computer",
    "scissorsvspaper": "player"
}


valid_choices = ['rock', 'paper', 'scissors']

user_choice = ""
while user_choice not in valid_choices:
    user_choice = input(f"Choose one: {', '.join(valid_choices)}: ")

computer_choice = random.choice(valid_choices)

if user_choice == computer_choice:
    print("It was a tie")
else:
    key = user_choice + "vs" + computer_choice
    print(f"{outcomes[key]} wins!")
    
