# 🤖 AI Employee Assistant | RAG Search

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-000000?style=for-the-badge&logo=meta&logoColor=white)

A premium, end-to-end **Retrieval-Augmented Generation (RAG)** semantic search engine built with Streamlit, FAISS, and `sentence-transformers`. 

This application acts as an intelligent assistant capable of understanding natural language queries and retrieving the most relevant answers from company policy documents, using state-of-the-art dense vector embeddings.

---

## ✨ Features

- **🧠 Semantic Search**: Uses `all-MiniLM-L6-v2` embeddings to understand the *meaning* of your query, not just exact keyword matches.
- **⚡ Lightning-Fast Retrieval**: Utilizes Facebook's FAISS (Facebook AI Similarity Search) for high-speed, scalable vector similarity search.
- **🎨 Premium User Interface**: A modern, dark-themed responsive UI built with Streamlit and custom CSS, featuring interactive result cards.
- **📄 Local Document Processing**: Easily upload text files (e.g., `Employee.txt`) or use the default knowledge base to instantly build a searchable vector index.

## 🛠️ Technology Stack

- **Frontend**: Streamlit (with Custom CSS)
- **Embeddings Model**: `SentenceTransformer` (`all-MiniLM-L6-v2`)
- **Vector Database**: FAISS
- **Core Processing**: Python & NumPy

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.10+ installed on your machine.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Thirthaprasadcn/faiss-rag.git
   cd faiss-rag
   ```

2. **Create a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the Streamlit server:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to `http://localhost:8501`.
3. You can either upload your own `.txt` document (formatted with alternating Question and Answer lines) or use the pre-loaded `Employee.txt` file.
4. Type your query in the search bar and discover relevant insights!

## 📂 Project Structure

- `app.py`: The main Streamlit application containing the UI and search logic.
- `requirements.txt`: Python package dependencies.
- `Employee.txt`: Sample knowledge base containing Q&A pairs about company policies.
- `EndToEnd_Info.md`: Detailed technical documentation explaining the RAG pipeline.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! 
Feel free to check out the [issues page](https://github.com/Thirthaprasadcn/faiss-rag/issues).

## 📝 License

This project is free and open-source.
