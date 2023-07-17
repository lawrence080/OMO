from Bot import Bot
from addPdf import addPdf2collecion
from training import training



if __name__ == "__main__":
    bot = Bot()
    userInput = input("please enter your question")
    ans = bot.bot(userInput)
    print(ans)
    aiTraining = training()
    a = aiTraining.trainBot(ans,1)
    print(a)


