import random
item_list=['Rock','Paper','Scissor']
user_choice=input("Enter Your Move (Rock,Paper,Scissor) ? : ")
computer_move=random.choice(item_list)
print(f"User Choice : {user_choice}, Computer_Choice : {computer_move}")

if user_choice==computer_move:
    print("Both Chooses Same : Match Tie")
elif user_choice == 'Rock':
    if computer_move == 'Paper':
        print("Paper Covers Rock : Computer Wins")
    else:
        print("Rock Smashes Scissor : You Wins")
elif user_choice == 'Paper':
    if computer_move == 'Rock':
        print("Paper Covers Rock : You Wins")
    else:
        print("Scissor cuts  paper : Computer Wins")
elif user_choice == 'Scissor':
    if computer_move == 'Paper':
        print("Scissors cuts paper : You Wins")
    else:
        print("Rock Smashes Scissor : Computer Wins")

else:
    print("Invalid Move")