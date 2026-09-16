import sys
import os

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from google import genai

load_dotenv()

PERSIST_DIR = "chroma_db"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
TOP_K = 4

# Gemini client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


def retrieve(question, k=TOP_K):
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    vectordb = Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=embeddings
    )

    return vectordb.similarity_search(question, k=k)


def answer_question(question):
    docs = retrieve(question)

    if not docs:
        return {
            "answer": "No documents found. Run ingest.py first.",
            "sources": []
        }

    context = "\n\n---\n\n".join(
        f"[Page {d.metadata.get('page', '?')}]\n{d.page_content}"
        for d in docs
    )

    prompt = f"""Answer the question using ONLY the context below.

If the answer isn't in the context, say you don't know.
Do not guess or use outside knowledge.

Context:
{context}

Question:
{question}

Answer:"""

    interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt
    )

    answer_text = interaction.output_text

    sources = sorted(
        {d.metadata.get("page", "?") for d in docs}
    )

    return {
        "answer": answer_text,
        "sources": sources
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python query.py "your question here"')
        sys.exit(1)

    question = " ".join(sys.argv[1:])
    result = answer_question(question)

    print("\nAnswer:")
    print(result["answer"])

    print("\nSource pages:")
    print(", ".join(map(str, result["sources"])))