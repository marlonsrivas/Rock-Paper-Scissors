
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

player = int(input("What do you choose? Type 0 for Rock, 1 For Paper or 2 for Scissors.\n"))

if (player) == 0:
    print(f"rock \n {rock}")
elif player == 1:
    print(f"paper \n {paper}")
elif player == 2:
    print(f"scissors\n {scissors}")




choicesString = rock,paper,scissors

if(player > 2 or player < 0):
    print("Number is invalid, You lose")
else:
    print("Computer chose")
    select = random.randint(0, 2)
    print(select)
    print(choicesString[select])

    if(int(player) == int(select)):
        print("Its a tie")
    elif(player == 0 and select != 1):
        print("Player Wins")
    elif(player == 1 and select != 2):
        print("Player Wins")
    elif(player == 2 and select != 0):
        print("Player Wins")
    elif(select == 0 and player != 1):
        print("You Lose")
    elif(select == 1 and player != 2):
        print("You Lose")
    elif(select == 2 and player != 0):
        print("You Lose")

