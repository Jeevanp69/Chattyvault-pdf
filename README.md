# 📚 ChattyVault PDF

A Retrieval-Augmented Generation (RAG) application that lets users upload PDF documents, ask questions about their contents, and receive grounded answers with cited source pages.

## 🚀 Features

- Upload PDF documents
- Extract text from PDFs
- Split documents into overlapping chunks
- Generate local semantic embeddings
- Store embeddings in ChromaDB
- Retrieve relevant document chunks using semantic search
- Generate grounded answers with Google Gemini
- Show source pages used for the answer
- Streamlit web interface
- Local-first development workflow

## 🏗️ Architecture

```text
PDF Upload
    │
    ▼
PDF Text Extraction
    │
    ▼
Document Chunking
(chunk size: 1500
 overlap: 200)
    │
    ▼
Sentence Transformer
Embeddings
    │
    ▼
ChromaDB
Vector Store
    │
    ▼
User Question
    │
    ▼
Semantic Retrieval
Top-K Relevant Chunks
    │
    ▼
Google Gemini
    │
    ▼
Grounded Answer
+ Source Pages
🛠️ Tech Stack
Python
Streamlit
LangChain
LangChain Hugging Face
ChromaDB
Sentence Transformers
PyPDF
Google Gemini API
📂 Project Structure
chattyvault-pdf/
│
├── ingest.py
├── query.py
├── streamlit_app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
⚙️ Setup
1. Clone the repository
git clone https://github.com/Jeevanp69/chattyvault-pdf.git
cd chattyvault-pdf
2. Create a virtual environment

Windows:

python -m venv .venv
.venv\Scripts\Activate.ps1
3. Install dependencies
pip install -r requirements.txt
4. Configure the Gemini API

Create a .env file:

GEMINI_API_KEY=your_gemini_api_key_here

Never commit your .env file or expose your API key publicly.

5. Ingest a PDF
python ingest.py path\to\your_document.pdf

This extracts the PDF content, creates document chunks, generates embeddings, and stores them in ChromaDB.

6. Test the RAG pipeline
python query.py "What are the five essential characteristics of cloud computing?"
7. Run the Streamlit application
python -m streamlit run streamlit_app.py

Open:

http://localhost:8501

Upload a PDF and ask questions about its contents.

🧪 Verified Test

The application was tested using a sample PDF covering Fundamentals of Cloud Computing.

Test question:

What are the five essential characteristics of cloud computing?

The application successfully returned:

On-demand self-service
Broad network access
Resource pooling
Rapid elasticity
Measured service

The response also reported the retrieved source pages.

🔍 How RAG Works in This Project

Instead of sending an entire document directly to the language model, the application:

Extracts text from the uploaded PDF.
Splits the text into overlapping chunks.
Converts chunks into vector embeddings using a local Sentence Transformer model.
Stores the vectors in ChromaDB.
Converts the user's question into an embedding.
Retrieves the most relevant document chunks.
Sends only the retrieved context to Gemini.
Generates an answer grounded in that context.
Displays the source pages associated with the retrieved chunks.
💰 Cost

The project is designed for a free-cost development workflow:

PDF processing: local
Embeddings: local Sentence Transformer
Vector database: local ChromaDB
LLM: Google Gemini API

No Anthropic API credits are required.

API availability and free-tier limits depend on the current provider account and model.

🔐 Environment Variables
GEMINI_API_KEY=your_gemini_api_key_here

The real .env file is excluded from Git using .gitignore.

⚠️ Limitations
Retrieval quality depends on document chunking and embedding quality.
Large documents may require additional retrieval optimization.
The current system uses a fixed top-K retrieval strategy.
Gemini API quotas and model availability can vary.
ChromaDB is configured for local development.
🔮 Future Improvements
Hybrid keyword + semantic retrieval
Retrieval re-ranking
Multi-document knowledge bases
Conversation memory
Streaming responses
Improved citation formatting
Retrieval evaluation metrics
Production vector database
Cloud deployment
Document management and deletion
👨‍💻 Author

Jeevan Puppala

GitHub: https://github.com/Jeevanp69
