def checkIfNumberIsPrime(number):
    count = 0
    for i in range(1, number):
        if number % i == 0:
            count += 1
    if count == 1:
        print("Chosen number is Prime")
    else:
        print("Chosen number is NOT Prime")

checkIfNumberIsPrime(int(input("Enter a number: ")))