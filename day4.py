# Day #4 Challenge
# Author: Naren
# Date: 2022.9.15

import random

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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissor]

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
me = int(input())
print(game_images[me])
computer = random.randint(0, 2)
#randomモジュールの関数randint(a, b)はa <= n <= bのランダムな整数intを返す。randrange(a, b + 1)と等価。bの値も範囲に含むので注意。
print("Computer choose:{}\n{}".format(computer, game_images[computer]))

if me > computer:
    if me == 2 and computer == 0:
        print("You lose")
    else:
         print("You win")    
elif me < computer:
    if me == 0 and computer == 2:
        print("You win")    
    else:
        print("You lose")
else:
    print("Equal, do this again")

print()