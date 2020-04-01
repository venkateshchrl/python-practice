class WordReverse:
    def __init__(self, inputStr):
        self.inputStr = inputStr

    def wordReverse(self):
        return " ".join(self.inputStr.split(" ")[::-1])

    def wordReverseWithLogic(self):
        strList = self.inputStr.split(" ")
        strListReversed = []
        for i in range(len(strList)):
            strListReversed.append(strList[len(strList)-1-i])
        return " ".join([str for str in strListReversed])
    
reversed = WordReverse(input("Enter a Sentence: "))
print(reversed.wordReverse())
print(reversed.wordReverseWithLogic())