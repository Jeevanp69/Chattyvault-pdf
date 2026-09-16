"""
streamlit_app.py — Step 3: the UI, built last on top of the two
pipelines that already work on their own.

Run with: streamlit run streamlit_app.py
"""

import os
import tempfile
import streamlit as st
from ingest import ingest_pdf
from query import answer_question

st.set_page_config(page_title="Chat With Your Documents", page_icon="📄")
st.title("📄 Chat With Your Documents")
st.caption("Upload a PDF, then ask questions about it. Answers cite the page they came from.")

if "ingested" not in st.session_state:
    st.session_state.ingested = False
if "history" not in st.session_state:
    st.session_state.history = []

# --- Upload + ingest ---
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file is not None and not st.session_state.ingested:
    with st.spinner("Reading and indexing your document..."):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        chunk_count = ingest_pdf(tmp_path)
        os.unlink(tmp_path)
        st.session_state.ingested = True

    st.success(f"Indexed {chunk_count} chunks. Ask away below.")

# --- Chat ---
if st.session_state.ingested:
    question = st.chat_input("Ask a question about your document")

    if question:
        with st.spinner("Thinking..."):
            result = answer_question(question)
        st.session_state.history.append((question, result["answer"], result["sources"]))

    for q, a, sources in reversed(st.session_state.history):
        with st.chat_message("user"):
            st.write(q)
        with st.chat_message("assistant"):
            st.write(a)
            if sources:
                st.caption(f"Source page(s): {', '.join(str(s) for s in sources)}")
else:
    st.info("Upload a PDF above to get started.")
