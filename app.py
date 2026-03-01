import os
os.environ["STREAMLIT_SERVER_FILE_WATCHER_TYPE"] = "none"
import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="AirIndia RAG Chatbot",
    page_icon="📄",
    layout="wide"
)

# -------------------- ENV VARIABLE CHECK --------------------

try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except KeyError:
    st.error("GROQ_API_KEY not set in Streamlit secrets.")
    st.stop()

PDF_FOLDER = "pdfs"
GLOB_PATTERN = "**/*.pdf"

# -------------------- BUILD VECTOR STORE --------------------
@st.cache_resource(show_spinner="🔄 Processing PDFs and building vector index...")
def build_vectorstore():

    loader = DirectoryLoader(
        path=PDF_FOLDER,
        glob=GLOB_PATTERN,
        loader_cls=PyPDFLoader
    )

    documents = loader.load()

    if not documents:
        return None

    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    split_docs = text_splitter.split_documents(documents)

    # Embeddings
    embeddings = FastEmbedEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(split_docs, embeddings)

    return vectorstore


# -------------------- LLM --------------------
@st.cache_resource
def get_llm():
    return ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.2
    )


# -------------------- MAIN APP --------------------
def main():

    st.title("📄 AirIndia RAG Chatbot")
    st.caption("Ask questions about Air India documents")

    # Sidebar
    st.sidebar.header("About")
    st.sidebar.info(
        """
        🔎 Retrieval-Augmented Generation (RAG)
        📚 FAISS Vector Store
        🤖 Groq Llama 3.1 Model
        ☁️ Deployable on AWS EC2
        """
    )

    if st.sidebar.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

    vectorstore = build_vectorstore()

    if not vectorstore:
        st.warning("No PDFs found inside the 'pdfs' folder.")
        st.stop()

    llm = get_llm()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display Chat History
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User Input
    if question := st.chat_input("Ask a question about the documents..."):

        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.markdown(question)

        # 🔥 Retrieve Top 3 Relevant Chunks
        retrieved_docs = vectorstore.similarity_search(question, k=3)

        context = "\n\n".join(doc.page_content for doc in retrieved_docs)

        prompt = f"""
You are a helpful assistant answering ONLY from the provided context.
If the answer is not found in the context, respond with:
"I don't have enough information in the documents."

Context:
{context}

Question:
{question}

Answer clearly and concisely:
"""

        with st.chat_message("assistant"):
            try:
                response = llm.invoke(prompt)
                answer = response.content
                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as e:
                st.error(f"Error during generation: {str(e)}")


if __name__ == "__main__":

    main()




