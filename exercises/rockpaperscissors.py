input1 = input("Enter Player 1 Choice: ")
input2 = input("Enter Player 2 Choice: ")

def compare(input1, input2):
    if input1 == input2:
        return("It is a tie!")
    elif input1 == "Rock":
        if input2 == "Scissors":
            return ("Player 1 Wins")
        else:
            return ("Player 2 Wins")
    elif input1 == "Scissors":
        if input2 == "Paper":
            return ("Player 1 Wins")
        else:
            return ("Player 2 Wins")
    elif input1 == "Paper":
        if input2 == "Rock":
            return ("Player 1 Wins")
        else:
            return ("Player 2 Wins")
    else:
        return ("Invalid input!")

print(compare(input1, input2))