class ListDuplicates:
    def __init__(self, inputList):
        self.inputList = inputList
    
    def removeDuplicates(self):
        output = []
        for i in self.inputList:
            if i not in output:
                output.append(i)
        return output

    def removeDuplicatesUsingSet(self):
        return list(set(self.inputList))

listDuplicates = ListDuplicates([1, 2, 3, 4, 5, 6, 7, 8, 1, 3, 5, 7])
print(listDuplicates.removeDuplicates())
print(listDuplicates.removeDuplicatesUsingSet())