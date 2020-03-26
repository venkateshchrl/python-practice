list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
inputFromUser = int(input("Enter a number: "))
newList = []
for i in list:
    if(i < inputFromUser):
        newList.append(i)
print(newList)