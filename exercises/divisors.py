number = int(input("Enter a number: "))
index = 1
divisorList = []
while(index < number):
    if(number % index == 0):
        divisorList.append(index)
    index += 1
print(number, " is divisble by ", index)