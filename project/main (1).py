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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

game = [rock, paper, scissors]


if player >= 3 or player < 0: 
  print("You typed an invalid number, you lose!")
else:
  print(game[player])


  
  computer = random.randint(0,2)
  print("Computer chose:")
  print(game[computer])

  
  if player == 0 and computer == 2:
    print("You Win!")
  elif computer == 0 and player == 2:
    print("Computer wins!")
  elif computer > player:
    print("Computer wins!")
  elif player > computer:
    print("You Win!")
  elif player == computer:
    print("The game is draw")




# Putting the whole condition in one big IF allows the program to debugg if the player chooses number > 3 or < 0




