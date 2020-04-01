import random
userInputStr = ""
count = 0

def matchUserGuess(randomNumber, userInput):
    global count
    diff = userInput - randomNumber
    if diff == 0:
        print("User guessed the exact number after ", count, " tries")
        return ("You guessed the exact number")
    elif diff > 0:
        count += 1
        return ("You guess is too high to the exact number")
    elif diff < 0:
        count += 1
        return ("You guess is too low to the exact number")

while(userInputStr != "exit"):
    randomNumber = random.randint(0, 10)
    userInputStr = input("Guess the number: ")
    if(userInputStr != "exit"):
        print("Random Number: ", randomNumber)
        print("Count ", count)
        print(matchUserGuess(randomNumber, int(userInputStr)))

        
