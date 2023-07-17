from langchain.document_loaders import PyPDFLoader 
from langchain.embeddings import OpenAIEmbeddings 
from langchain.vectorstores import Chroma 
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI


import APIsecret
import os

class addPdf2collecion:
    def __init__(self) -> None:
        self.setOpenAIAPIkey()

    def setOpenAIAPIkey(self):
        os.environ["OPENAI_API_KEY"] = APIsecret.OPEN_API_KEY
    def addFile(self):
        from langchain.document_loaders import PyPDFDirectoryLoader
        self.pdf_folder_path = "C:\\Users\\lawrence\\Desktop\\Job\\meetingOnly\\data\\"
        self.loader = PyPDFDirectoryLoader(self.pdf_folder_path)
        self.docs = self.loader.load()
        embeddings = OpenAIEmbeddings()
        vectordb = Chroma(embedding_function=embeddings,persist_directory=".\db")
        vectordb.persist()
        Chroma.add_documents(self=vectordb,documents = self.docs)
