from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

# Rename variable to avoid conflict with any previous loader imports
pdf_loader = PyPDFLoader(r"data\Full-Moon.pdf")
docs = pdf_loader.load()

# Split documents into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)
chunks = splitter.split_documents(docs)

# Create embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# Create vector store
db = FAISS.from_documents(chunks, embeddings)
db.save_local("vector_db/full_moon")

print("✅ Ingestion complete")
