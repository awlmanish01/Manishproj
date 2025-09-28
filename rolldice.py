#importing random module
import random
#using function
def roll_dice():
  return random.randint(1,6)
print("welcome to Roll Dice Game")


while True:
 user=input("press enter to roll the dice(q to quit)")
 if user.lower()=="q":
    print("Game over")
    break
 else:
    result=roll_dice()
    print("you rolled:",result)