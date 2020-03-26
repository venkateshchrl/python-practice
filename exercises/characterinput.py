import datetime

name = input("Please enter your name: ")
age = int(input("Age: "))
copies = int(input("Copies: "))
date = datetime.datetime.now()
current_year = date.year

value = (current_year - age) + 100
for i in range(copies):
    print("The year when you turn 100 is " + str(value))
