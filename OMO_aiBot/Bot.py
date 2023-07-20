from langchain.document_loaders import PyPDFLoader 
from langchain.embeddings import OpenAIEmbeddings 
from langchain.vectorstores import Chroma 
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI


import APIsecret
import os
from addPdf import addPdf2collecion


# from langchain.document_loaders import PyPDFDirectoryLoader
# pdf_folder_path = "C:\\Users\\lawrence\\Desktop\\Job\\meetingOnly\\data\\"
# loader = PyPDFDirectoryLoader(pdf_folder_path)
# docs = loader.load()

class Bot(addPdf2collecion):
    def __init__(self) -> None:
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        super().setOpenAIAPIkey()
    def bot(self,quesiton)->str:
        embeddings = OpenAIEmbeddings()
        # vectordb = Chroma.from_documents(docs, embedding=embeddings, 
        #                                  persist_directory=".\db")
        vectordb = Chroma(embedding_function=embeddings,persist_directory="db")
        vectordb.persist()
        pdf_qa = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0.8 ) , vectordb.as_retriever(), memory = self.memory, chain_type="map_reduce")
        query = quesiton
        print(self.memory)
        result = pdf_qa({"question": query})
        print(result)
        # print(result["answer"])
        result["answer"]
        return result["answer"]



# if __name__ == "__main__":
#     while(True):
#         q = input(' please enter your question: ')
#         if q == 'n':
#             break
#         bot(q)
    