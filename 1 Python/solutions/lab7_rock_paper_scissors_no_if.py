### Modules ###
import random

### Variables ###
choices = ['rock', 'paper', 'scissors']
# dictionary to assign inputs to values
choice_dict = {
  'rock': 0,
  'paper': 1,
  'scissors': 2
}
# Calculate result message using a list of lists. -1 is lose, 0 is tie, 1 is win, 2 is invalid input
results = [
  #rock paper scissors  
  [0,   -1,     1], # rock
  [1,    0,    -1], # paper
  [-1,   1,     0], # scissors
  [2,    2,     2]  # invalid
]
# dictionary to assign message to result
result_messages = {
  -1 : "Sorry you lose",
  0 : "It is a tie",
  1 : "Congrats, you win!",
  2 : "Invalid input"
}
# dictionary to keep with the theme of "no if" statements
play_again = {
  "yes": True,
  "no": False
}

### Logic ###
# Welcome message
print('Welcome to Rock, Paper, Scissors!')

# Loop for replayability
running = play_again["yes"]
while running:
  # Get the users choice and convert to value for result
  player_choice = choice_dict.get(input(f'Please select one: \n{choices}: '), 3)
  # Get the computers choice
  computer_choice = random.choice(choices)
  # Output computers choice to the screen
  print(f'Computer chose {computer_choice.capitalize()}')
  # Overwrite computer_choice with the value needed to determine winner
  computer_choice = choice_dict.get(computer_choice)
  # Get the result message and print to screen
  print(result_messages[results[player_choice][computer_choice]])
  # Ifless conditional to keep with "no if" theme
  running = play_again.get(input('Would you like to play again?'), False)