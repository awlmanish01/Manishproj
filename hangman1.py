import random
print("Welcome to hangman Game")
list=['love','peace','hate','care','late','hope']
rand=random.choice(list)
len(rand)
space=len(rand)*['_']
print(space)
attempt=0
max_attempt=5
guessed_word=[]
while attempt<max_attempt and '_' in space:
 user=input("Guess the letters:")
 if not user.isalpha() or len(user)!=1:
  print("Enter a valid single letter")
  continue
 if user in guessed_word:
  print("You have already guessed the letter .Try different one")
 else:
  guessed_word.append(user)
  

 if user in rand:
  for i in range(len(rand)):
   if rand[i]==user:
    space[i]=user
    print("Correct guess",''.join(space))
 else:
  attempt+=1
  print("Wrong guess!Try again ")
  print(f"You have {max_attempt-attempt}try remaining")

 print("Guessed letters:", " ".join(guessed_word))
 print()
 
if '_' not in space:
  print("You have sucessfully cracked the word")
  print(f"You have done it in {attempt} wrong guesses!")
else:
  print("Game over!")



