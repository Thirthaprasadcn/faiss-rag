import streamlit as st
import faiss
import numpy as np
import os
from sentence_transformers import SentenceTransformer

# Page Configuration
st.set_page_config(
    page_title="AI Employee Assistant | RAG Search",
    page_icon="🤖",
    layout="wide"
)

# Custom Premium CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }
    
    .stTextInput > div > div > input {
        background-color: #334155 !important;
        color: white !important;
        border-radius: 12px !important;
        border: 1px solid #475569 !important;
        padding: 15px !important;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #3b82f6 0%, #2563eb 100%) !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 10px 24px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.4) !important;
    }
    
    .result-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(71, 85, 105, 0.3);
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 15px;
        transition: all 0.3s ease;
    }
    
    .result-card:hover {
        border-color: #3b82f6;
        transform: scale(1.01);
    }
    
    .score-badge {
        background: rgba(59, 130, 246, 0.2);
        color: #60a5fa;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 10px;
    }
    
    .header-text {
        background: linear-gradient(90deg, #60a5fa, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 3rem;
        margin-bottom: 0;
    }
    
    .sidebar .sidebar-content {
        background-color: #0f172a;
    }
    
    hr {
        border: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, #475569, transparent);
        margin: 2rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Functions ---

@st.cache_resource
def load_model():
    """Load the sentence transformer model."""
    return SentenceTransformer('all-MiniLM-L6-v2')

def load_documents_from_file(file_content):
    """Process file content into chunks (Q&A pairs)."""
    # Decode bytes to string if necessary
    if isinstance(file_content, bytes):
        text = file_content.decode('utf-8')
    else:
        text = file_content
        
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    # Assuming Q followed by A format (pair every two lines)
    documents = []
    for i in range(0, len(lines) - 1, 2):
        pair = f"**Q:** {lines[i]}\n\n**A:** {lines[i+1]}"
        documents.append(pair)
        
    # If there's a leftover line, add it as is
    if len(lines) % 2 != 0:
        documents.append(lines[-1])
        
    return documents

@st.cache_data
def create_faiss_index(documents):
    """Generate embeddings and create FAISS index."""
    model = load_model()
    embeddings = model.encode(documents)
    
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings).astype('float32'))
    
    return index, documents

def retrieve_context(query, index, documents, top_k=3):
    """Search the index for the query."""
    model = load_model()
    query_embedding = model.encode([query])
    
    D, I = index.search(np.array(query_embedding).astype('float32'), top_k)
    
    results = []
    for idx, i in enumerate(I[0]):
        if i < len(documents):
            results.append({
                "content": documents[i],
                "score": float(D[0][idx])
            })
    return results

# --- App UI ---

def main():
    st.markdown('<p class="header-text">RAG Assistant</p>', unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8; font-size: 1.2rem;'>Intelligent Retrieval for Employee Documents</p>", unsafe_allow_html=True)
    
    with st.sidebar:
        st.title("📁 Setup Knowledge Base")
        uploaded_file = st.file_uploader("Upload employee text file", type="txt")
        
        st.divider()
        st.info("The system uses FAISS for vector search and Sentence-Transformers for embeddings.")
        
        # Option to use the existing Employee.txt if no file uploaded
        use_default = st.checkbox("Use default Employee.txt", value=True if not uploaded_file else False)

    # Initialize state
    if "index" not in st.session_state:
        st.session_state.index = None
        st.session_state.docs = None

    # Processing Logic
    file_to_process = None
    if uploaded_file:
        file_to_process = uploaded_file.getvalue()
    elif use_default:
        if os.path.exists("Employee.txt"):
            with open("Employee.txt", "r", encoding="utf-8") as f:
                file_to_process = f.read()
        else:
            st.error("Employee.txt not found. Please upload a file.")

    if file_to_process:
        with st.spinner("🚀 Building Vector Database..."):
            documents = load_documents_from_file(file_to_process)
            st.session_state.index, st.session_state.docs = create_faiss_index(documents)
            st.success(f"Indexed {len(documents)} document pairs!")

    # Search Section
    st.divider()
    
    query = st.text_input("🔍 Ask a question about company policy:", placeholder="e.g. What is the notice period?")
    
    if query:
        if st.session_state.index is not None:
            results = retrieve_context(query, st.session_state.index, st.session_state.docs)
            
            st.subheader("🎯 Top Relevant Results")
            
            for res in results:
                st.markdown(f"""
                <div class="result-card">
                    <span class="score-badge">Similarity Score: {res['score']:.4f}</span>
                    <div style="color: #e2e8f0; line-height: 1.6;">
                        {res['content']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("Please upload a document first to start searching.")

    # Footer
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; font-size: 0.8rem;'>Built with Streamlit • FAISS • Sentence-Transformers</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
