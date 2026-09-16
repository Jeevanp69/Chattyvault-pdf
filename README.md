# 📄 RAG Document Q&A

A Retrieval-Augmented Generation (RAG) application that lets users upload PDF documents and ask questions about their contents.

The application retrieves relevant document chunks and uses Google Gemini to generate grounded answers with source-page references.

## 🚀 Features

- Upload PDF documents
- Automatic PDF text extraction
- Intelligent document chunking
- Local semantic embeddings using Sentence Transformers
- ChromaDB vector storage
- Semantic similarity retrieval
- Gemini-powered question answering
- Answers grounded only in retrieved document context
- Source-page references
- Streamlit web interface
- Free-cost development setup using local embeddings and Gemini API access

## 🏗️ Architecture

```text
                ┌─────────────────┐
                │    PDF Upload   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │  PDF Extraction │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Chunking        │
                │ 1500 / 200      │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Sentence       │
                │ Transformer    │
                │ Embeddings     │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │    ChromaDB     │
                └────────┬────────┘
                         │
                User Question
                         │
                         ▼
                ┌─────────────────┐
                │ Semantic Search │
                │   Top-K Chunks  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Google Gemini   │
                │  Answer Model   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Answer + Source │
                │     Pages       │
                └─────────────────┘
🛠️ Tech Stack
Python
Streamlit
LangChain
ChromaDB
Sentence Transformers
PyPDF
Google Gemini API
📂 Project Structure
rag-app/
│
├── data/
│   └── cloud_computing_basics.pdf
│
├── chroma_db/
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
git clone <your-repository-url>
cd rag-app
2. Create a virtual environment

Windows:

python -m venv .venv
.venv\Scripts\Activate.ps1
3. Install dependencies
pip install -r requirements.txt
4. Configure Gemini API

Create a .env file:

GEMINI_API_KEY=your_gemini_api_key_here

Never commit .env or your API key to GitHub.

5. Ingest a PDF
python ingest.py data\cloud_computing_basics.pdf

The application splits the PDF into overlapping chunks and stores their embeddings in ChromaDB.

6. Test from the command line
python query.py "What are the five essential characteristics of cloud computing?"
7. Run the Streamlit application
python -m streamlit run streamlit_app.py

Open:

http://localhost:8501

Upload a PDF and ask questions about its contents.

🧪 Verified Test

The project was tested using a sample PDF titled Fundamentals of Cloud Computing.

Test question:

What are the five essential characteristics of cloud computing?

The system successfully returned:

On-demand self-service
Broad network access
Resource pooling
Rapid elasticity
Measured service

and reported the retrieved source pages.

🔐 Environment Variables
GEMINI_API_KEY=your_gemini_api_key_here
💰 Cost

The application uses:

Local Sentence Transformer embeddings
Local ChromaDB storage
Gemini API for answer generation

No Anthropic API credits are required.

Actual API availability and free-tier limits depend on the provider's current account and model availability.

⚠️ Limitations
Answers depend on the quality of retrieved document chunks.
Very large documents may require additional chunking and retrieval optimization.
The application currently uses a fixed top-K retrieval strategy.
Gemini API availability and quotas can vary by account.
ChromaDB is stored locally during development.
🔮 Future Improvements
Hybrid keyword + semantic retrieval
Re-ranking retrieved chunks
Multi-document search
Conversation memory
Streaming responses
Better citation formatting
Evaluation dataset and retrieval metrics
Production vector database
Cloud deployment
👨‍💻 Author

Jeevan Puppala