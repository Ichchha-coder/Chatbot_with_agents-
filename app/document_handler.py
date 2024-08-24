# app/document_handler.py

import os
from langchain.indexes import VectorIndex
from langchain.embeddings import EmbeddingModel
from langchain.chains import RetrievalQA

class DocumentHandler:
    def __init__(self, llm):
        self.index = VectorIndex(embedding_model=EmbeddingModel())
        self.llm = llm
        self.qa_chain = RetrievalQA(llm=self.llm, retriever=self.index.as_retriever())
        self._load_documents()

    def _load_documents(self):
        documents_folder = os.path.join(os.getcwd(), 'documents')
        for filename in os.listdir(documents_folder):
            with open(os.path.join(documents_folder, filename), 'r') as file:
                document = file.read()
                self.index.add_document(document)

    def handle_query(self, query):
        return self.qa_chain.run(query)
