class Main:
    userWord = None
    forbiddenLetters = None
    words = None
    mapUpper = None
    scanner = None

    def __init__(self):
        self.userWord = ""
        self.forbiddenLetters = ""
        self.words = []
        self.mapUpper = {}
        self.scanner = "Python-inputs"
      
        print("[Welcome to Wordle Cheater]\n\n[Input capital letters if in correct position]\n[Input lower case letters if in word but wrong position]\n[Input ? if unsure of letter in word]\n")

        self.readFile()
    
        while(len(self.userWord) != 5):
            print("[Input must be 5 characters]")
            self.userWord = self.getWord()

        self.eliminateForbiddenWords(self.getForbiddenLetters())
    
    def readFile(self):
        with open('wordbank.txt') as file:
            self.words = [line.rstrip('\n') for line in file]
    
    def getWord(self):
        print("Enter word: ", end = "")
        return input()
        
    def getForbiddenLetters(self):
        print("Enter letters not in the word (- for none): ", end = "")
        self.forbiddenLetters = input()
        return self.forbiddenLetters
        
    def eliminateForbiddenWords(self, forbidden):
        i = 0
        while (i < len(self.words)) :
            j = 0
            while (j < len(forbidden)) :
                if (str(forbidden[j]) in self.words[i]):
                    self.words.pop(i)
                    i -= 1
                    break
                j += 1
            i += 1

        self.filter()
        
    def filter(self):
        lowerOnly = ""
        i = 0
        while (i < len(self.userWord)):
            if (self.userWord[i].islower()):
                lowerOnly += self.userWord[i]
            elif(self.userWord[i].isupper()):
                self.mapUpper[str(self.userWord[i])] = i
            i += 1
        
        self.lowerCheck(lowerOnly)
        self.upperCheck()
        
        print("\nPotential Guesses: ")
        self.printWords()
        
        if(len(self.words) > 1):
            extraLetters = ""
            print("Add additional letters not in word (- for none): ", end = "")
            extraLetters = input()
            if (not extraLetters == "-"):
                self.forbiddenLetters += extraLetters
                self.eliminateForbiddenWords(self.forbiddenLetters)
                
    def lowerCheck(self, lower):
        i = 0
        while(i < len(lower)) :
            letter = str(lower[i])
            j = 0
            while (j < len(self.words)):
                if (not letter in self.words[j]):
                    self.words.pop(j)
                    j -= 1
                j += 1
            i += 1
            
    def upperCheck(self):
        for k in self.mapUpper:
            letter = k.lower()
            pos = self.mapUpper[k]

            j = 0
            while(j < len(self.words)):
                if(not str(self.words[j])[pos] == letter):
                    self.words.pop(j)
                    j -= 1
                j += 1

    def printWords(self):
        for word in self.words:
            print(word)
        print()  
            
    @staticmethod
    def main(args):
        Main()
        
if __name__ == "__main__":
    Main.main([])