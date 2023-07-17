
from langchain.document_loaders import PyPDFLoader 
from langchain.embeddings import OpenAIEmbeddings 
from langchain.vectorstores import Chroma 
from langchain.chains import ConversationalRetrievalChain, LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import StringPromptTemplate


import APIsecret
import os

from Bot import Bot
from langchain import ConversationChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    # AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
    
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)


class training(Bot):
    humanTemplate:str = "human:answer:{question}"
    systemTemplate:str = "system: assume you are an Open AI answer judge. the judgmental standers are honesty, clarity and easy to read. please rate the answer from 1 to 3. 1 means the content is unclear, worng and hard to understand, 2 means the content is unclear but correct, and 3 means the content is easy to understand, clear, and correct, provid explaination"

    def __init__(self) -> None:
        super().__init__()

    def setinitialPrompt(self,priviousAIAnswer:str):
        # aiTemplate = "please rate the answer from 1 to 10, base on {category}"
        # ai_message_prompt_template = AIMessagePromptTemplate().from_template(template=aiTemplate)

        
        human_message_prompt_template = HumanMessagePromptTemplate.from_template(template=self.humanTemplate)
        
        system_message_prompt_template = SystemMessagePromptTemplate.from_template(template=self.systemTemplate)

        chatPrompt = ChatPromptTemplate.from_messages([system_message_prompt_template, human_message_prompt_template])
        return chatPrompt
        
    def trainBot(self, userInput, value):
        chat = ChatOpenAI(temperature=0)
        message = [
            SystemMessage(content=self.systemTemplate)
        ]

        ui = self.humanTemplate.format(question=userInput)
        message.append(HumanMessage(content=ui))
        ai_response = chat(messages=message).content
        message.append(AIMessage(content=("ai: "+ai_response)))
        file = open("trainedData\\trainBotdocument{0}.txt".format(value),"a+")
        with file as txt_file:
            for line in message:
                temp = line.content
                txt_file.write(" "+temp+ "\n")
        return ai_response

        
    # def trainAI(self,priviousAIAnswer:str):

    #     # bot = Bot()
    #     # pdf_qa = bot.bot()

    #     chatPrompt = self.setinitialPrompt()
        
        
    #     embeddings = OpenAIEmbeddings()
    #     vectordb = Chroma(embedding_function=embeddings,persist_directory=".\db")
    #     vectordb.persist()
    #     memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    #     pdf_qa = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0.8) , vectordb.as_retriever(), memory=memory, condense_question_prompt=chatPrompt)
        
    #     Userinput = priviousAIAnswer
    #     humanTemplate:str = f"please rate the answer:{Userinput},from 1 to 10"
    #     result =pdf_qa({"question":humanTemplate})
        

    #     return result



