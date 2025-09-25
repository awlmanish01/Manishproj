import random
print("Welcome to Number Guessing Game")
rand_number=random.randint(1,100)
attempt=0
max_attempt=6

while attempt < max_attempt :
  remaining=max_attempt-(attempt+1)

  guess=int(input(" Guess a number from 1-100\n"))

  if guess < 1 and guess > 100:
     print("Enter number between 1-100")
  elif guess == rand_number:
     print(f"The number is {guess}.You guessed in {attempt+1}  attempt")
  elif guess < rand_number:
     print("your guess is too low. TRY HIGH")
     print(f"You have {remaining} try left")
  else :
     print("your guess is too high. TRY LOW")
     print(f"You have {remaining} try left")
  attempt+= 1

  if attempt == max_attempt and guess != rand_number:
   print("Game over!!")
