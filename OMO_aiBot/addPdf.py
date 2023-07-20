from langchain.document_loaders import PyPDFLoader 
from langchain.embeddings import OpenAIEmbeddings 
from langchain.vectorstores import Chroma 
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.document_loaders import PyPDFDirectoryLoader

import APIsecret
from addFile import addFile
import os

class addPdf2collecion(addFile):
    def __init__(self) -> None:
        self.setOpenAIAPIkey()

    def setOpenAIAPIkey(self):
        os.environ["OPENAI_API_KEY"] = APIsecret.OPEN_API_KEY
    def addFile(self):
        self.pdf_folder_path = "OMO_aiBot\\pdftrainData"
        self.loader = PyPDFDirectoryLoader(self.pdf_folder_path)
        self.docs = self.loader.load()
        embeddings = OpenAIEmbeddings()
        vectordb = Chroma(embedding_function=embeddings,persist_directory="db")
        vectordb.persist()
        Chroma.add_documents(self=vectordb,documents = self.docs)
