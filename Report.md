1. Problem Statement and Motivation

Current Status: Partially completed

Problem Being Addressed

* Build a document-based assistant that allows users to upload a PDF and interact with its contents.
* The goal is to reduce the time required to manually read long documents.

Why It Matters

* Students, researchers, and professionals often work with lengthy PDFs.
* Finding specific information manually is time-consuming.

Why RAG Was Chosen

* A normal language model may not know the contents of a user-uploaded document.
* Retrieval allows responses to be grounded in the uploaded PDF.
* This improves factual accuracy and reduces hallucinations.

⸻

2. Knowledge Base Design and Description

Current Status: Basic implementation completed

Knowledge Source

* PDF documents uploaded by users.

What We Implemented

* PDF upload functionality using Streamlit.
* PDF text extraction using pypdf.

User PDF
↓
Text Extraction
↓
Display on Screen

Not yet implemented:

* Vector database
* Embeddings
* Persistent knowledge storage

⸻

3. Retrieval Strategy and Methodology

Current Status: Not implemented yet

A true retrieval pipeline requires:

PDF
↓
Chunking
↓
Embeddings
↓
FAISS
↓
Similarity Search

❌ No chunking

❌ No embeddings

❌ No FAISS

❌ No retrieval

The application currently displays extracted text only.

⸻

4. Data Augmentation and Context Enhancement

Current Status: Not implemented

Not yet added:

* Query expansion
* Metadata enrichment
* Summarization
* Context compression
* Language normalization

Current system performs direct text extraction only.

⸻

5. Generation Model Selection and Reasoning

Current Status: Not implemented

No LLM has been connected yet.

Not yet selected:

* OpenAI models
* Anthropic models
* Google Gemma
* Mistral AI Mistral

6. System Prompt Design and Transparency

Current Status: Not implemented

No system prompt exists yet because no LLM has been integrated.

Streamlit UI
     ↓
Upload PDF
     ↓
pypdf Reader
     ↓
Extract Text
     ↓
Display Text
     ↓
Question Box
     ↓
Repeat User Question

Overall Progress

Approximately 20–25% complete toward a full RAG system