import random #Gemerating random number by importing random module

print("Welcome to mastermind Game")
num=random.randrange(1000,10000)#generating random number forom range 1000 to 10000

user=int(input("Enter 4 digit number:"))#Taking input from user

if user==num: #CHECKS FIRST guess is correct. 
  print("you have guessed the number in 1st try.You have been the mastermind")
else:
  ctr=1 #it counts the no. of attempts user attempted.
while user!=num:#runs loop until the user inputs  correct number.
   num_str=str(num)#converting the number into string
   user_str=str(user)
   correct=['X']*4
   count=0
   for i in range(4):  #it runs loop from 0 to 3
     if user_str[i]==num_str[i]:
      count+=1
      correct[i]=user_str[i] #it stores the correctly placed users input in right index

   if count>0:
    print(f"Not the all  numbers were correctly placed . But you did get {count} digit right")
    print("Correct positions so far: ", " ".join(correct))
   else:
    print("Wrong guess!. None numbers correctly placed")

   print()
   user=int(input("Enter your choices"))
   ctr+=1
#When loop exits 
print("You have become the mastermind")
print(f"You have done it in {ctr} attempt")
