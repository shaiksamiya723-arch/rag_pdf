import re
import streamlit as st
from pypdf import PdfReader

st.title("PDF Reader")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type="pdf"
)

def score_chunk(query: str, chunk: str) -> int:
    query_tokens = set(re.findall(r"\w+", query.lower()))
    chunk_tokens = set(re.findall(r"\w+", chunk.lower()))
    return sum(1 for token in query_tokens if token in chunk_tokens)


def get_relevant_chunks(text: str, question: str, max_chunks: int = 3):
    chunks = [chunk.strip() for chunk in re.split(r"\n\s*\n+", text) if chunk.strip()]
    if not chunks:
        chunks = [text.strip()]

    scored = [(score_chunk(question, chunk), chunk) for chunk in chunks]
    scored.sort(key=lambda item: item[0], reverse=True)
    return [chunk for score, chunk in scored if score > 0][:max_chunks] or [scored[0][1]]


if uploaded_file is not None:
    pdf = PdfReader(uploaded_file)

    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    st.subheader("PDF Content")
    st.write(text)

    question = st.text_input("Ask a question about the PDF")
    if question:
        answer_chunks = get_relevant_chunks(text, question)
        st.subheader("Answer from PDF")
        for idx, chunk in enumerate(answer_chunks, start=1):
            st.write(chunk)
            if idx < len(answer_chunks):
                st.write("---")