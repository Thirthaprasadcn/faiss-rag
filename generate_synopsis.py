from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Project Synopsis: RAG with FAISS', 0, 1, 'C')
        self.ln(5)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 8, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 7, body)
        self.ln()

def create_synopsis():
    pdf = PDF()
    pdf.add_page()
    
    pdf.chapter_title('1. Project Title')
    pdf.chapter_body('AI-Powered Employee Assistant: Retrieval-Augmented Generation (RAG) using FAISS and Sentence-Transformers.')

    pdf.chapter_title('2. Abstract')
    pdf.chapter_body('This project implements a Retrieval-Augmented Generation (RAG) system designed to provide semantic search capabilities over internal company documents. By utilizing vector embeddings and the FAISS library, the system can understand user queries contextually and retrieve the most relevant information from an unstructured text database, significantly improving the efficiency of information retrieval compared to traditional keyword-based searches.')

    pdf.chapter_title('3. Objectives')
    pdf.chapter_body('- To develop a mini-search engine for local text documents.\n- To implement semantic search using dense vector embeddings.\n- To utilize FAISS for high-speed similarity search.\n- To provide a user-friendly web interface for document interaction.')

    pdf.chapter_title('4. Methodology')
    pdf.chapter_body('The system follows a standard RAG pipeline:\n1. Data Ingestion: Loading text files and splitting them into context-aware chunks.\n2. Vectorization: Converting text chunks into 384-dimensional vectors using the all-MiniLM-L6-v2 transformer model.\n3. Indexing: Storing vectors in a FAISS index for optimized retrieval.\n4. Querying: Converting user queries to vectors and performing a similarity search in the vector space.')

    pdf.chapter_title('5. Key Features')
    pdf.chapter_body('- Semantic Understanding: Finds answers even if the exact keywords do not match.\n- High Performance: FAISS allows searching through thousands of records in milliseconds.\n- Modern UI: Responsive and aesthetic dashboard built with Streamlit.\n- Document Flexibility: Supports dynamic file uploads and real-time indexing.')

    pdf.chapter_title('6. Future Scope')
    pdf.chapter_body('- Integration with Large Language Models (LLMs) like GPT-4 or Llama-3 for generating conversational answers based on retrieved context.\n- Support for multi-document indexing (PDFs, Docx, etc.).\n- Deployment as a microservice with a REST API.')

    pdf.output('Project_Synopsis.pdf')
    print("PDF generated successfully: Project_Synopsis.pdf")

if __name__ == '__main__':
    create_synopsis()
