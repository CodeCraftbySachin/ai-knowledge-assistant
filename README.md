# AI Knowledge Assistant (RAG-based Chatbot)

A modular **Retrieval-Augmented Generation (RAG)** chatbot built using LangChain, FAISS, and Hugging Face embeddings.

This system answers questions based on custom documents while maintaining conversation memory and role-based responses.

---

## 🧠 Features

- 🔍 Semantic Search using FAISS
- 📄 Document-based Question Answering (RAG)
- 🧠 Conversation Memory (context-aware responses)
- 🎭 Role-based Chat (teacher, storyteller, interviewer)
- 🧱 Modular Architecture (clean and scalable)

---

## 🏗️ Project Structure

```
ai-knowledge-assistant/
│
├── app.py
│
├── config/
│   └── settings.py
│
├── llm/
│   └── model.py
│
├── prompts/
│   └── prompt.py
│
├── memory/
│   └── memory.py
│
├── retriever/
│   ├── loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   └── vectorstore.py
│
├── chains/
│   └── chatbot_chain.py
│
├── data/
│   └── sample.txt
│
└── requirements.txt
```

---

## 🔁 How It Works

1. User enters a query  
2. System retrieves relevant chunks from documents (FAISS)  
3. Context is injected into the prompt  
4. LLM generates a grounded response  
5. Memory maintains conversation history  

---

## ⚙️ Tech Stack

- LangChain
- Groq (LLM)
- Hugging Face (sentence-transformers)
- FAISS (vector database)
- Python

---

## 🚀 Setup Instructions

### 1. Clone the repository
```
git clone <your-repo-url>
cd ai-knowledge-assistant
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Set environment variable
```
Windows:
setx GROQ_API_KEY "your_api_key"
Mac/Linux:
export GROQ_API_KEY="your_api_key"
```
### 4. Run the project

You can run the project in two ways:

#### Option A: Streamlit Web UI (Recommended)
```
streamlit run streamlit_app.py
```

#### Option B: CLI Version
```
python app.py
```

- Example Usage
- Select Role: teacher
- You: What is Python?
- AI: Python is a high-level programming language...


### 6. Future Improvements

- Support for PDF documents
- Web-based UI (React + FastAPI)
- Multi-document ingestion
- Source citation display
