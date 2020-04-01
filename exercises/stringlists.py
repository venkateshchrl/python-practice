def reverse(word):
    revStr = ''
    for ch in range(len(word)):
        revStr += word[len(word)-1-ch]
    return revStr

str = input("Enter a word: ")
revStr = str[::-1]
if revStr == str:
    print("This is a Palindrome")
else:
    print("This is NOT a Palindrome")