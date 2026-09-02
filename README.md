 🩺 Medical RAG Chatbot

A Retrieval-Augmented Generation (RAG) based medical chatbot that provides context-aware medical information using WHO medical publications.

The system combines semantic document retrieval with a locally running Large Language Model (LLM) using Ollama to generate answers based on relevant medical information retrieved from the knowledge base.



 🚀 Features

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



 🏗️ System Architecture


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
