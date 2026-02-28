# 🚀 Air India Document Intelligence Chatbot
### Production-Style RAG System Deployed on AWS

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green?style=flat-square)
![Groq](https://img.shields.io/badge/Groq-Llama_3.1-orange?style=flat-square)
![FAISS](https://img.shields.io/badge/FAISS-Vector_Store-purple?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?style=flat-square&logo=streamlit)
![AWS](https://img.shields.io/badge/AWS-EC2-yellow?style=flat-square&logo=amazon-aws)

---

## 🧠 Project Overview

A **Retrieval-Augmented Generation (RAG)** based Document Intelligence System that enables users to ask natural language questions about Air India policy and operational PDFs.

The system processes **120+ pages of documents**, retrieves only the most relevant content, and generates accurate, context-aware responses using a Large Language Model (LLM) — deployed end-to-end on **AWS EC2**.

---

## 🏗️ Architecture

```
PDF Documents (121+ Pages)
         ↓
Document Loader (PyPDF)
         ↓
Recursive Text Chunking
         ↓
Vector Embeddings
         ↓
FAISS Vector Store
         ↓
Top-K Similarity Search
         ↓
Groq Llama 3.1 LLM
         ↓
Streamlit Chat Interface
         ↓
AWS EC2 Deployment
```

---

## 🔥 Key Features

| Feature | Description |
|--------|-------------|
| 📄 **Multi-PDF Ingestion** | Recursive loading of multiple PDF documents |
| 🧩 **Smart Chunking** | Recursive text splitting for token optimization |
| 🧠 **Semantic Embeddings** | Transformer-based vector embeddings |
| 🔎 **FAISS Retrieval** | Fast similarity search over document vectors |
| 🤖 **Groq LLM** | Llama 3.1 (8B Instant) for generation |
| 💬 **Chat UI** | Conversational interface with history |
| ☁️ **Cloud Deployed** | Hosted on AWS EC2 (Ubuntu) |
| 🔐 **Secure Config** | API keys via environment variables |
| ⚡ **Token Efficient** | Optimized RAG pipeline reduces cost & latency |

---

## 💡 Problem It Solves

Large documents **cannot be directly passed to LLMs** due to:
- Token limits
- High latency
- Increased cost
- Reduced answer relevance

### ✅ How This System Solves It

| Step | Action |
|------|--------|
| 1 | Split documents into structured, overlapping chunks |
| 2 | Generate embeddings for semantic understanding |
| 3 | Retrieve only top-k relevant chunks per query |
| 4 | Pass optimized, limited context to the LLM |

**Result:** Faster responses · Lower token usage · Higher accuracy · Scalable design

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **LLM** | Groq (Llama 3.1 8B Instant) |
| **RAG Framework** | LangChain |
| **Vector Store** | FAISS |
| **Embeddings** | Transformer-based embedding model |
| **UI** | Streamlit |
| **Cloud** | AWS EC2 (Ubuntu) |
| **Security** | Environment Variables |
| **Version Control** | Git + GitHub |

---

## ⚙️ Core Components

### 1️⃣ Document Processing
- Loaded PDFs recursively using `DirectoryLoader`
- Extracted text content using `PyPDFLoader`

### 2️⃣ Chunking Strategy
- Used `RecursiveCharacterTextSplitter`
- **Chunk size:** 1000 characters
- **Overlap:** 200 characters
- Ensures semantic continuity across chunk boundaries

### 3️⃣ Retrieval Strategy
- Created embeddings for all document chunks
- Stored embeddings in a FAISS vector store
- Retrieved **Top-3** semantically similar chunks per query

### 4️⃣ LLM Integration
- Powered by **Groq Llama 3.1 (8B Instant)**
- Structured prompt with retrieved context
- Context-aware generation with graceful fallback if answer not found

### 5️⃣ Deployment
- Ubuntu EC2 instance on AWS
- Python virtual environment for isolation
- Streamlit served on port `8501`
- Secure environment variable configuration

---

## 🚀 Getting Started (Local)

### Prerequisites
- Python 3.10+
- A [Groq API Key](https://console.groq.com)

### Installation

```bash
# 1. Clone the repository
git clone <repo_url>
cd Air-India-Chatbot

# 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set your Groq API key
export GROQ_API_KEY="your_api_key_here"

# 5. Run the app
streamlit run app.py
```

App will be available at: **http://localhost:8501**

---

## ☁️ Deployment on AWS EC2

### Step-by-Step

```bash
# 1. Launch an Ubuntu EC2 instance (t2.micro or higher)
# 2. SSH into the instance
ssh -i your-key.pem ubuntu@<your-ec2-public-ip>

# 3. Update and install Python
sudo apt update && sudo apt install python3-pip python3-venv -y

# 4. Clone the repository
git clone <repo_url>
cd Air-India-Chatbot

# 5. Set up virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 6. Install dependencies
pip install -r requirements.txt

# 7. Set environment variable
export GROQ_API_KEY="your_api_key_here"

# 8. Run Streamlit (publicly accessible)
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

> ⚠️ Make sure port `8501` is open in your EC2 **Security Group** inbound rules.

App will be accessible at: **http://\<your-ec2-public-ip\>:8501**

---

## 📁 Project Structure

```
Air-India-Chatbot/
│
├── data/                  # PDF documents folder
│   └── *.pdf
│
├── app.py                 # Main Streamlit application
├── rag_pipeline.py        # RAG logic (chunking, embeddings, retrieval)
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variable template
└── README.md
```

---

## 🔐 Environment Variables

Create a `.env` file or export the following:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> Never commit your `.env` file. Add it to `.gitignore`.

---

## 📌 Future Improvements

- [ ] Add support for more document formats (DOCX, TXT)
- [ ] Implement conversational memory across sessions
- [ ] Add document upload from UI
- [ ] Integrate reranking for improved retrieval accuracy
- [ ] Add authentication layer for production use

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
