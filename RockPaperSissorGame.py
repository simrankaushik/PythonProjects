# rock, paper, scissors GAME

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
import random
print("WELCOME")
user_choice = input("what u wanna have ? type 0 for rock, 1 for paper and 2 for scissors:\n ")

choice_int = int(user_choice)
if choice_int == 0:
    print("your choose rock " + rock)
if choice_int == 1:
    print("your choose paper " + paper)
if choice_int == 2:
    print("your choose scissors " + scissors)

computer_choice=random.randint(0,2)

if choice_int >= 3 or choice_int < 0:
    print("You typed an invalid number, you lose!")
else:
    print([choice_int ])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print([computer_choice])


    if choice_int == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and choice_int == 2:
        print("You lose")
    elif computer_choice > choice_int :
        print("You lose")
    elif choice_int  > computer_choice:
        print("You win!")
    elif computer_choice == choice_int:
        print("It's a draw")






