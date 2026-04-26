# End-to-End Project Documentation: RAG with FAISS

This document outlines the step-by-step implementation of the Retrieval-Augmented Generation (RAG) system built using FAISS and Sentence-Transformers.

## 1. Project Overview
The goal of this project was to create a semantic search engine capable of retrieving precise information from a company policy document (`Employee.txt`). Unlike traditional keyword search, this system understands the *meaning* of the user's query.

## 2. Technical Stack
- **Frontend**: Streamlit (Modern dark-themed UI)
- **Embeddings**: `all-MiniLM-L6-v2` (Sentence-Transformers)
- **Vector Database**: FAISS (Facebook AI Similarity Search)
- **Language**: Python 3.10+

## 3. Implementation Workflow

### Step 1: Data Preparation
- **Input**: A text file (`Employee.txt`) containing Question and Answer pairs on consecutive lines.
- **Preprocessing**: The code reads the file and groups every two lines into a single "Document" (Q&A pair). This ensures that when a match is found, the user gets both the question and its corresponding answer as context.

### Step 2: Embedding Generation
- Each document (Q&A pair) is passed through the `SentenceTransformer` model.
- The model converts text into a **384-dimensional dense vector** (embedding) that represents its semantic meaning.

### Step 3: FAISS Indexing
- A FAISS index (`IndexFlatL2`) is initialized.
- The generated embeddings are added to this index. FAISS organizes these vectors in a way that allows for extremely fast similarity calculations using Euclidean distance (L2).

### Step 4: Retrieval (Search)
- When a user enters a query:
  1. The query is converted into a vector using the same embedding model.
  2. FAISS compares the query vector against all document vectors in the index.
  3. The top $k$ (default 3) most similar documents are returned based on the lowest distance scores.

### Step 5: User Interface
- A premium Streamlit dashboard displays the results in aesthetic "cards," showing the similarity score and the retrieved content.

## 4. How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Launch the application:
   ```bash
   streamlit run app.py
   ```
3. Upload your `.txt` file or use the pre-loaded `Employee.txt`.
4. Start searching!

---
*Created by AI Assistant - April 2026*
