# 🩺 Medical RAG Chatbot

A Retrieval-Augmented Generation (RAG) based medical chatbot that provides context-aware medical information using WHO medical publications.

The system combines semantic document retrieval with a locally running Large Language Model (LLM) using Ollama to generate answers based on relevant medical information retrieved from the knowledge base.

---

## 🚀 Features

- Retrieval-Augmented Generation (RAG)
- WHO medical publications as the knowledge source
- PDF document processing
- Text extraction and chunking
- Hugging Face embeddings
- Semantic similarity search
- ChromaDB vector database
- Local LLM inference using Ollama
- FastAPI backend
- Interactive web interface
- Source attribution
- Medical safety guardrails
- Reduced LLM hallucination through context-based generation

---

## 🏗️ System Architecture

```text
                    User
                     │
                     ▼
              Web Interface
                     │
                     ▼
                FastAPI
                     │
                     ▼
              RAG Pipeline
                     │
              ┌──────┴──────┐
              ▼             ▼
          Embeddings     ChromaDB
                            │
                            ▼
                    Relevant Documents
                            │
                            ▼
                         Ollama
                            │
                            ▼
                     Generated Answer
                            │
                    ┌───────┴───────┐
                    ▼               ▼
                 Answer          Sources
```
## 📚 Medical Knowledge Sources

The chatbot uses the following World Health Organization (WHO) publications
as its primary medical knowledge sources:

### 1. Diabetes

**Title:** Guidance on global monitoring for diabetes prevention and control – 2024  
**Publisher:** World Health Organization  
**ISBN:** 9240102248

### 2. Hypertension

**Title:** Guideline for the pharmacological treatment of hypertension in adults  
**Publisher:** World Health Organization  
**Publication Year:** 2021  
**ISBN:** 978-92-4-003398-6

### 3. Asthma

**Title:** Tobacco and asthma: WHO tobacco knowledge summaries  
**Publisher:** World Health Organization  
**Publication Year:** 2024  
**ISBN:** 978-92-4-009753-7

> **Note:** The original PDF files are not included in this repository.

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn

### RAG / AI
- LangChain
- Ollama
- Hugging Face Embeddings
- Retrieval-Augmented Generation (RAG)

### Vector Database
- ChromaDB

### Frontend
- HTML
- CSS
- JavaScript

### Development Tools
- Git
- GitHub
- Visual Studio Code

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/medical-rag-chatbot.git
cd medical-rag-chatbot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows PowerShell

```powershell
venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
venv\Scripts\activate
```

### 4. Install Required Packages

```bash
pip install -r requirements.txt
```

### 5. Install and Setup Ollama

Install Ollama and download the LLM model used by the project:

```bash
ollama pull llama3.2
```

Verify that the model is installed:

```bash
ollama list
```

Make sure Ollama is running before starting the application.

### 6. Add WHO Medical Documents

Place the required WHO PDF documents inside the `data/` directory:

```text
data/
├── Diabetes WHO.pdf
├── Hypertension WHO.pdf
└── Asthma WHO.pdf
```

The PDF files are excluded from the Git repository using `.gitignore`.

### 7. Build the Vector Database

Run the document loader to process the PDFs and create the ChromaDB vector database:

```bash
python app/loader.py
```

### 8. Start the FastAPI Server

```bash
uvicorn app.main:app --reload
```

The application will run at:

```text
http://127.0.0.1:8000
```

### 9. Open FastAPI API Documentation

Open the following URL in your browser:

```text
http://127.0.0.1:8000/docs
```
