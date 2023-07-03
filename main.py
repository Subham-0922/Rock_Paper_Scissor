import random

Choice = ["Rock", "Paper", "Scissors"]

while True:
    print("Rock, Paper, Scissors Game:")
    youwin, computerwin=0,0
    for i in range(1,6):
        print("Round ",i," Start:")
        print("Please select any option")
        print("1.Rock", "2.Paper", "3.Scissors",sep="\n")
        ch=int(input())
        if ch==1:
            print("You select Rock")
            ch = "Rock"
        elif ch==2:
            print("You select Paper")
            ch = "Paper"
        elif ch==3:
            print("You select Scissors")
            ch = "Scissors"
        else : 
            print("Invalid Choice")
            break
        
        cc = random.choice(Choice)
        print("Computer selected ",cc)

        if ch == cc:
            print("This round is Draw",sep="\n")
        elif (ch=="Paper" and cc=="Rock") or (ch=="Rock" and cc=="Scissors") or (ch=="Scissors" and cc=="Paper"):
            youwin+=1
            print("You Win this round",sep="\n")
        else : 
            computerwin+=1
            print("Computer Win this round",sep="\n")

    if youwin>computerwin:
        print("You are Winner of the Game")
        print("Your Score is :",youwin," Computer Score is :",computerwin,sep=" ")
    elif youwin<computerwin:
        print("You Lost Game")
        print("Your Score is :",youwin," Computer Score is :",computerwin,sep=" ")
    else:
        print("Game Draw")
        print("Your Score is :",youwin," Computer Score is :",computerwin,sep=" ")

    uc = input("You want to play again (y/n)")
    if uc=="y":
        continue
    else:
        break

