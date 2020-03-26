num = int(input("Enter a number: "))
check = int(input("Enter a number to divide: "))
if(num % 4 == 0):
    print("The given input is multiple of 4")
elif(num % 2 == 0):
    print("The given input is even number")
else:
    print("The given input is odd number")

if(num % check == 0):
    print(num, " divides evenly by check ", check)
else:
    print(num, " doesn't divide evenly by check ", check)