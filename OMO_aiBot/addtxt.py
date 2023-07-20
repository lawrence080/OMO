import APIsecret
import os
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

class addtxt2collecion:
    def __init__(self) -> None:
        self.setOpenAIAPIkey()

    def setOpenAIAPIkey(self):
        os.environ["OPENAI_API_KEY"] = APIsecret.OPEN_API_KEY
    def addFile(self):
        self.text_folder_path = "OMO_aiBot\\trainedData"
        loaders = DirectoryLoader(self.text_folder_path,glob='**/*.txt')
        docs = loaders.load()
        Text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        doc_text = Text_splitter.split_documents(documents=docs)
        # self.loader = PyPDFDirectoryLoader(self.pdf_folder_path)
        # self.docs = self.loader.load()
        embeddings = OpenAIEmbeddings()
        vectordb = Chroma(embedding_function=embeddings,persist_directory="db")
        vectordb.persist()
        Chroma.add_documents(self=vectordb,documents = doc_text)