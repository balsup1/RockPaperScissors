rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors? \n"))
if choice > 2 or choice < 0:
  print("This is an invalid number")
  

computer_choice = random.randint(0,2)


if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)

if computer_choice == 0:
  print(f"Computer chose: {rock}")
elif computer_choice == 1:
  print(f"Computer chose: {paper}")
elif computer_choice == 2:
  print(f"Computer chose: {scissors}")

if (choice == 0) & (computer_choice == 1):
  print("You lose")
elif (choice == 1) & (computer_choice == 2):
  print("You lose")
elif (choice == 2) & (computer_choice == 0):
  print("You lose")
elif choice == computer_choice:
  print("Its a tie")
else:
  print("You win")
