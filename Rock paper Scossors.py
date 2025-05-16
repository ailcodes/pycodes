# Rock, Paper, Scissoor Game
msg=print("Welcome to Rock, Paper, Scissoor Game. \nPlease enter Player 1 and Player 2 name to continue")
Player1=input("Enter your name as Player 1 :  ")
Player2=input("Enter your name as Player 2 :  ")
print(f"Player 1 is : {Player1} \nand \nPlayer 2 is : {Player2}")
print("Let's start")
game=["Rock", "Paper", "Scissor"]
print(f"Hey {Player1}, make your choice from the following.")
print("1. Rock \n2.Paper \n3.Scissors")
num1=int(input("Just input the number : "))

if num1==1:
    choice1=game[0]
elif num1==2:
    choice1==game[1]
elif num1==3:
    choice1==game[2]


print(f"Hey {Player1}, make your choice from the following.")
print("1. Rock \n2.Paper \n3.Scissors")
num2=int(input("Just input the number : "))

if num2==1:
    choice2=game[0]
elif num2==2:
    choice2=game[1]
elif num2==3:
    choice2=game[2]


if choice1==choice2:
    print("It's a Draw!")
elif choice1==game[0] and choice2==game[1]:
    print(f"{Player2} wins the game")
elif choice1==game[0] and choice2==game[2]:
    print(f"{Player1} wins the game")
elif choice1==game[1] and choice2==game[0]:
    print(f"{Player1} wins the game")
elif choice1==game[1] and choice2==game[2]:
    print(f"{Player2} wins the game")
elif choice1==game[2] and choice2==game[0]:
    print(f"{Player2} wins the game")
elif choice1==game[2] and choice2==game[1]:
    print(f"{Player1} wins the game")
