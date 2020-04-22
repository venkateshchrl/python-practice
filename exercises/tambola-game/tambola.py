import os
from tambolasheetgenerator import SheetGenerator

class Tambola:
    def __init__(self):
        self.no_of_sheets = int(input("No. of Sheets to be generated: "))
        self.sheet_generator = SheetGenerator()
        self.sheets = []
    
    def generateSheets(self):
        for i in range(0, self.no_of_sheets):
            sheet = "="*44 + "\n"
            sheet += "-"*18 + "SHEET -"+str((i+1))+"-"*18 +"\n"
            sheet += "="*44 + "\n"
            sheet += self.sheet_generator.generateSheet()
            sheet += " "*44 + "\n"
            self.sheets.append(sheet)
    
    def storeSheetToFile(self, sheetNumber, sheetContent):
        if os.path.exists('sheets/Tambola-Sheet-'+str(sheetNumber+1)+'.txt') == False:
            self.fileObject = open('sheets/Tambola-Sheet-'+str(sheetNumber+1)+'.txt', "w+")
        else:
            self.fileObject = open('sheets/Tambola-Sheet-'+str(sheetNumber+1)+'.txt', "w+")
        self.fileObject.write(sheetContent)
    
    def validateSheets(self):
        validate_counter = 0
        for i in range(len(self.sheets))[:len(self.sheets)-1]:
            for j in range(len(self.sheets))[i+1:]:
                if(self.sheets[i] == self.sheets[j]):
                    validate_counter += 1
            if(validate_counter == 0):
                self.storeSheetToFile(i, self.sheets[i])
            
        if validate_counter > 0:
            print("Duplicate Sheets Present")
        else:
            print("All sheets are unique")

tambola = Tambola()
tambola.generateSheets()
tambola.validateSheets()