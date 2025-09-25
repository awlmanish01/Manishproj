import random
print("Rock Paper Scissors Game!!")
choose=int(input("Enter your choice(1,2,or3) \n1.rock\n2.paper \n3.scissors\n"))
print("User_choice:",choose)
random_num=random.randint(1,4)
print("Computer_choice:",random_num)
if choose < 1 and choose > 3:
 print("Invalid choice(Choose 1,2 or 3)")
elif choose==random_num:
 print("its a tie")
elif (choose==1 and random_num==3) or (choose==2 and random_num==1) or (choose==3 and random_num==2):
 print("User wins!")
else:
 print("Computer wins")