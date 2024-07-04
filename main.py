from art import logo, vs
from game_data import data
import random

# Function to clear the console screen
def clear_screen():
  """
  Clear the console screen using ANSI escape codes.
  This works on Unix-based systems and Windows 10+.
  """
  print("\033[H\033[J", end="")

# Set to keep track of selected data indices
selected_indices = set()

# Function to select unique data index
def select_unique_data_index():
  if len(selected_indices) == len(data):
    raise ValueError("All possible data have already been selected.")
  while True:
    new_index = random.randint(0, len(data) - 1)
    if new_index not in selected_indices:
      selected_indices.add(new_index)
      return new_index

# Function to get user input and check the answer
def get_user_choice(contestant_a, contestant_b):
  while True:
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_choice in ['a', 'b']:
      return user_choice == 'a'

# Function to display the current match
def display_match(contestant_a, contestant_b):
  print(f"Compare A: {contestant_a['name']}, {contestant_a['description']}, from {contestant_a['country']}.")
  print(vs)
  print(f"Against B: {contestant_b['name']}, {contestant_b['description']}, from {contestant_b['country']}.")

# Main game loop
def main():
  print(logo)
  score = 0
  current_pair = [select_unique_data_index(), select_unique_data_index()]

  while True:
    clear_screen()
    print(logo)
    
    contestant_a = data[current_pair[0]]
    contestant_b = data[current_pair[1]]
    
    display_match(contestant_a, contestant_b)
    
    user_choice_is_a = get_user_choice(contestant_a, contestant_b)
    correct_answer_is_a = contestant_a['follower_count'] > contestant_b['follower_count']
    
    if user_choice_is_a == correct_answer_is_a:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      print(f"Sorry, that's wrong. Final score: {score}.")
      break
    
    # Prepare next match
    current_pair[0] = current_pair[1]
    current_pair[1] = select_unique_data_index()

# Run the game
main()
