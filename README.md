PDF Reader App

A simple and interactive PDF Reader application built using Streamlit and PyPDF.
This app allows users to upload a PDF file, extract its text content, and ask questions related to the uploaded document.

Features
Upload PDF files easily
Extract text from PDF pages
Display complete PDF content
Ask questions based on PDF text
Retrieve relevant text chunks matching the question
Simple and beginner-friendly interface
Technologies Used
Python
Streamlit
PyPDF
Regular Expressions (re module)
Project Structure
project-folder/
│
├── app.py
├── requirements.txt
└── README.md
Installation
1. Clone the Repository
git clone <your-repository-url>
cd <repository-folder>
2. Create Virtual Environment (Optional)
Windows
python -m venv venv
venv\Scripts\activate
Linux / Mac
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install streamlit pypdf

Or using requirements.txt:

pip install -r requirements.txt
Running the Application

Run the following command in terminal or PowerShell:

streamlit run app.py

The application will open automatically in your browser.

How It Works
User uploads a PDF file.
The app extracts text from all PDF pages.
Extracted text is displayed on the screen.
User asks a question related to the PDF.
The app:
Splits text into chunks
Scores chunks based on matching keywords
Displays the most relevant chunks as answers
Functions Explained
score_chunk(query, chunk)

This function compares the user's question with a text chunk and calculates a relevance score based on matching words.

def score_chunk(query: str, chunk: str) -> int:
get_relevant_chunks(text, question, max_chunks=3)

This function:

Splits PDF text into chunks
Scores each chunk
Returns the most relevant chunks
def get_relevant_chunks(text: str, question: str, max_chunks: int = 3):
Example Usage
Upload PDF

Upload any PDF document using the file uploader.

Ask Questions

Example questions:

What is machine learning?
Explain the introduction section.
What are the advantages mentioned?
Requirements

Create a requirements.txt file with:

streamlit
pypdf
Future Improvements
Add AI-based question answering
Highlight matched text
Support multiple PDF uploads
Add summarization feature
Improve chunk ranking algorithm
Author

Nagarari Harshini
B.Tech – Artificial Intelligence & Data Science

License

This project is open-source and free to use for learning purposes.