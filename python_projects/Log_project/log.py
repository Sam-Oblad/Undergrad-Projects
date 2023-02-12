#log.py
import os
from random import choice
from time import sleep
import math
numbers = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
letters = [None, "K", "M", "G", "T"]

def clear(): 
    os.system("clear")

def main_menu(count, correct):
    if correct >= 8:
        clear()
        print("\nYou've answered 8 in a row correctly! \nQuitting program . . .")
        quit()
    display_problem(count, correct)

def display_problem(count, correct):
    print(f"\nQuestion {count}\n")
    answer = create_problem()
    user_input = int(input("\nYour Answer: "))
    if user_input == answer:
        count += 1
        correct += 1
        print(f"Correct! You have answered {correct} correctly")
        sleep(3.2)
        main_menu(count, correct)
    else:
        count += 1
        correct = 0
        print(
        f"""Incorrect. 
The correct answer was {answer}
Correct answer streak back to 0""")
        sleep(4)
        clear()
        main_menu(count, correct)

def create_problem():
    number = choice(numbers)
    letter = choice(letters)
    if letter == None:
        problem = f"Log {number}"
    else:
        problem = f"Log {number}{letter}"
    answer = create_answer(number, letter)
    print(problem)
    return answer

def create_answer(n, l):
  if l == None:
    answer = round(math.log(n, 2))
    return answer
  elif l == "K":
    answer = round(math.log(n * 1_000, 2))
    return answer
  elif l == "M":
    answer = round(math.log(n * 1_000_000, 2))
    return answer
  elif l == "G":
    answer = round(math.log(n * 1_000_000_000, 2))
    return answer
  elif l == "T":
    answer = round(math.log(n * 1_000_000_000_000, 2))
    return answer

def main():
    main_menu(count = 1, correct = 0)
if __name__ == "__main__":
  main()