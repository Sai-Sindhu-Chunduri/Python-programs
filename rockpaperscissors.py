'''u1=int(input("Enter user1 choice: "))
u2=int(input("Enter user2 choice: "))
if u1>3 or u2>3:
    print("Enter valid choice")
else:
    if u1==u2:
        print("Tie game")
    if ((u1==1 and u2==2) or (u1==2 and u2==3) or (u1==3 and u2==1)):
        print("User2 wins")
    if ((u1==1 and u2==3) or (u1==2 and u2==1) or (u1==3 and u2==2)):
        print("User1 wins")'''
   

'''import random
user_choice=int(input("Enter user choice: "))
computer_choice=random.randint(1,3)
print("computer_choice:",computer_choice)
if user_choice>3:
    print("Enter valid choice")
else:
    if user_choice==computer_choice:
        print("Tie game")
    if ((user_choice==1 and computer_choice==2) or (user_choice==2 and computer_choice==3) or (user_choice==3 and computer_choice==1)):
        print("Computer wins")
    if ((user_choice==1 and computer_choice==3) or (user_choice==2 and computer_choice==1) or (user_choice==3 and computer_choice==2)):
        print("User wins")'''

import random
user_choice=int(input("Enter user choice: "))
computer_choice=random.randint(0,2)
print("computer_choice:",computer_choice)
A=[[0,2,1],[1,0,2],[2,1,0]]
result_matrix=A[user_choice][computer_choice]
winner=['Tie','Win','Lose']
result=winner[result_matrix]
print(result)

#0-->rock       and tie
#1-->paper      and win
#2-->scissors   and loose

   

