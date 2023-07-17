from Bot import Bot
from addPdf import addPdf2collecion
from training import training
from addtxt import addtxt2collecion

def askQuestion():
    while True:
        userInput = input("please enter your question: ")
        if userInput == 'no':
            break
        ans = bot.bot(userInput)
        print(ans)
        aiTraining = training()
        a = aiTraining.trainBot(ans,1)
        print(a)
def addPDF():
    a = addPdf2collecion()
    a.addFile()
    print("add pdf file \n ")

def addTxt():
    a = addtxt2collecion()
    a.addFile()
    print(" add txt file \n")
    


if __name__ == "__main__":
    bot = Bot()
    while True:
        action = input("please chose on of the three :\n 1: ask question \n 2: add pdf file \n 3: add txt file \n")
        match action:
            case "1":
                askQuestion()
            case "2":
                addPDF()
            case "3":
                addTxt()
            case _ :
                print("invalid answer")



