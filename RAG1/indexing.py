from dotenv import load_dotenv
from file_reader import extract_paragraphs
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embedding = OpenAIEmbeddings(
    model="bge-m3:latest",
    base_url="http://localhost:11434/v1",
    api_key="ollama",
    check_embedding_ctx_length=False
)

vectore_store = InMemoryVectorStore(embedding)

chunks = extract_paragraphs("pdfs/Penguins_ACL.pdf")
vectore_store.add_texts(texts=chunks)
print(f"indexed {len(chunks)} chunks")