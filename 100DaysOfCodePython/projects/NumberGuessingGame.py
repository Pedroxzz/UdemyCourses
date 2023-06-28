import random
logo = """
 _   _                 _                 _____                     _               _____                      
| \ | |               | |               |  __ \                   (_)             |  __ \                     
|  \| |_   _ _ __ ___ | |__   ___ _ __  | |  \/_   _  ___  ___ ___ _ _ __   __ _  | |  \/ __ _ _ __ ___   ___ 
| . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | __| | | |/ _ \/ __/ __| | '_ \ / _` | | | __ / _` | '_ ` _ \ / _ \ 
| |\  | |_| | | | | | | |_) |  __/ |    | |_\ \ |_| |  __/\__ \__ \ | | | | (_| | | |_\ \ (_| | | | | | |  __/
\_| \_/\__,_|_| |_| |_|_.__/ \___|_|     \____/\__,_|\___||___/___/_|_| |_|\__, |  \____/\__,_|_| |_| |_|\___|
                                                                            __/ |                             
                                                                           |___/                              
"""
EASY_MODE = 10
HARD_MODE = 5

def set_difficulty():
  choice = input('Choose a difficulty. Type "easy" or "hard": ')
  if choice.lower == 'easy':
    return EASY_MODE
  else  :
    return HARD_MODE
  
def check_answer(guess, answer, turn):
  if guess > answer:
    print('Your guess is too high')
    return turn- 1
  elif guess < answer:
    print("Your guess is too low.")
    return turn - 1
  else:
    print(f"You got it! The answer was {answer}.")
  
def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = random.randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turn = set_difficulty()

  guess = 0
  while guess != answer:
    print(f"You have {turn} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turn)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")
      
game()

