"""
ingest.py — Step 1 of the RAG pipeline.

Takes a PDF, splits it into overlapping text chunks, embeds each chunk
with a free local embedding model, and stores the vectors in a
persistent Chroma database on disk.

Run this by itself first and confirm it prints a chunk count > 0
before touching query.py or the UI. This is the "does ingestion work"
checkpoint.

Usage:
    python ingest.py path/to/your/file.pdf
"""

import sys
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

PERSIST_DIR = "chroma_db"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"  # small, free, runs locally — no API key needed


def ingest_pdf(pdf_path: str) -> int:
    """Load a PDF, chunk it, embed it, and persist it to Chroma.

    Returns the number of chunks stored, so callers (including the
    Streamlit UI) can confirm ingestion actually happened.
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"No file found at {pdf_path}")

    # 1. Load the PDF — this keeps page numbers attached to each chunk,
    #    which is what lets us cite sources later in query.py.
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    # 2. Split into overlapping chunks. Overlap prevents a sentence
    #    that spans a chunk boundary from losing context.
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=200,
    )
    chunks = splitter.split_documents(pages)

    # 3. Embed + store. HuggingFaceEmbeddings downloads the model once
    #    (needs internet the first time) and then runs locally for free.
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=PERSIST_DIR,
    )

    return len(chunks)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ingest.py path/to/file.pdf")
        sys.exit(1)

    count = ingest_pdf(sys.argv[1])
    print(f"Ingested and stored {count} chunks into '{PERSIST_DIR}/'.")
    print("Checkpoint: if this number looks reasonable for your document, ingestion works.")
