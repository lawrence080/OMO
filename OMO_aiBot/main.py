from Bot import Bot
from addPdf import addPdf2collecion
from training import training
from addtxt import addtxt2collecion



class AI():

    def __init__(self) -> None:
        self.bot = Bot()
    
    def askQuestion(self):
        while True:
            userInput = input("please enter your question: ")
            if userInput == 'no':
               break
            
            ans = self.bot.bot(quesiton=userInput)
            print(ans)
            aiTraining = training()
            ai_reply = aiTraining.trainBot(ans,1)
    def addPDF(self):
        a = addPdf2collecion()
        a.addFile()
        print("add pdf file \n ")

    def addTxt(self):
        a = addtxt2collecion()
        a.addFile()
        print(" add txt file \n")
    


if __name__ == "__main__":
    a = AI()
    # a.addPDF()
    # bot = Bot()
    while True:
        action = input("please chose on of the three :\n 1: ask question \n 2: add pdf file \n 3: add txt file \n")
        match action:
            case "1":
                a.askQuestion()
            case "2":
                a.addPDF()
            case "3":
                a.addTxt()
            case "4" :
                break
                print("invalid answer")



