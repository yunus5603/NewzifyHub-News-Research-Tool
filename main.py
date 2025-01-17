import os
import streamlit as st
import pickle
import time
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from warnings import filterwarnings
filterwarnings("ignore")

from dotenv import load_dotenv
load_dotenv()  # Load the environment variables

st.title("NewzifyHub: News Search Tool📈")
st.sidebar.title("News Article URLs")

# Constants
MAX_URLS = 3
CHUNK_SIZE = 500
MODEL_NAME = "all-MiniLM-L6-v2"
VECTOR_INDEX_PATH = "notebooks/vector_index.pkl"
LLM_MODEL = "Llama3-8b-8192"

# Collect URLs from sidebar
urls = []
for i in range(MAX_URLS):
    url = st.sidebar.text_input(
        label=f"URL {i+1}",
        key=f"url_input_{i}"
    )
    if url:
        urls.append(url)

# Process button and setup
process_url_clicked = st.sidebar.button("Process URLs")
main_placeholder = st.empty()

# Initialize LLM
try:
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("GROQ API key not found in environment variables")
    
    llm = ChatGroq(
        groq_api_key=groq_api_key, 
        model=LLM_MODEL
    )

    if process_url_clicked and urls:
        # Load and process URLs
        loader = UnstructuredURLLoader(urls=urls)
        main_placeholder.text("Data Loading...Started...✅")
        data = loader.load()

        # Split text into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            separators=['\n\n', '\n', '.', ','],
            chunk_size=CHUNK_SIZE
        )
        main_placeholder.text("Text Splitter...Started...✅")
        docs = text_splitter.split_documents(data)

        # Create embeddings
        embeddings = HuggingFaceEmbeddings(model_name=MODEL_NAME)
        vectorstore_openai = FAISS.from_documents(docs, embeddings)
        main_placeholder.text("Embedding Vector Started Building...✅✅✅")
        time.sleep(2)

        # Save the FAISS index to a pickle file
        with open(VECTOR_INDEX_PATH, "wb") as f:
            pickle.dump(vectorstore_openai, f)

except Exception as e:
    st.error(f"An error occurred: {str(e)}")

query = main_placeholder.text_input("Question: ")
if query:
    if os.path.exists(VECTOR_INDEX_PATH):
        with open(VECTOR_INDEX_PATH, "rb") as f:
            vectorstore = pickle.load(f)
            chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
            result = chain({"question": query}, return_only_outputs=True)
            # result will be a dictionary of this format --> {"answer": "", "sources": [] }
            st.header("Answer")
            st.write(result["answer"])

            # Display sources, if available
            sources = result.get("sources", "")
            if sources:
                st.subheader("Sources:")
                sources_list = sources.split("\n")  # Split the sources by newline
                for source in sources_list:
                    st.write(source)