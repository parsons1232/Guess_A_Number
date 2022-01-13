#!/usr/bin/env python3

import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
  if guess < answer:
    print("Too low.")
    return turns -1
  elif guess > answer:
    print("Too high.") 
    return turns -1 
  else:
    print(f"That's correct! {answer} is the correct number! You Win!")


def difficulty():
  level = (input("Choose a difficulty: Type 'easy' or 'hard': "))
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS
  
def game():
  print("Welcome to the Guessing Game!")
  print("I am thinking of a number between 1 and 100...")
  answer = random.randint(1,100)
  #print(f"psssttt.... the correct answer is {answer}")

  turns = difficulty()
  print(f"You have {turns} guesses left.")
  
  guess = 0

  while guess != answer:
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    print(f"You have {turns} guesses left.")
    if turns == 0:
      print(f"You have run out of turns. The number was {answer}. You lose.")
      return
game()
