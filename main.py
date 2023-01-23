from art import logo, vs
from game_data import data
import random
from replit import clear

def format_data(account):
  """Format account data into printable format"""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess,a_followers,b_followers):
  """"Use if statement to check if user is correct."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
  
# Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)


while game_should_continue:
  # generate random acount from the game data.
  # Making account at position B become the next account at position A.

  account_a = account_b
  account_b = random.choice(data)
  
  while account_a == account_b:
    account_b = random.choice(data)
  
  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Against B: {format_data(account_b)}.")
  
  #Ask user for a guess
  guess = input("Who has more followers? Type 'A' or 'B'").lower()
  
  # Check if user is correct
  # Get follower count of each account
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  
  is_correct = check_answer(guess,a_follower_count,b_follower_count)

  clear()
  print(logo)
  
  # Give user feedback on their guess.
  # Score keeping
  if is_correct:
    print("You'r right!")
    score += 1
  else:
    game_should_continue = False
    print("Sorry,that's wrong. Final score: {score}.")
  

# Clear the screen between rounds