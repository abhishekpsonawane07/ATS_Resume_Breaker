
# ATS Resume Breaker 💼💬

**ATS Resume Breaker** is an AI-powered tool designed to improve the hiring process by allowing recruiters to extract insights from resumes in PDF format and ask questions about the content. It leverages OpenAI's powerful language models and cutting-edge technologies like vector databases to enable smarter and more efficient recruitment decisions.

---

## 🌟 Features

- 📄 **PDF Resume Upload**: Upload PDF resumes for processing.
- ❓ **Ask Questions**: Query specific details from the resume (e.g., "What skills does the candidate have?").
- 🤖 **AI-Powered Insights**: Get relevant answers from the resume using OpenAI's language model.
- ⚡ **Fast Processing**: Uses vector embeddings and a vector database (FAISS) for quick searches.
- 🧠 **Answer Suggestions**: Receive automated answer suggestions for enhanced insights.

---

## 💻 Tech Stack

- **Python**: Main programming language.
- **Streamlit**: For building the web-based UI.
- **PyPDF2**: Extract text from PDF resumes.
- **LangChain**: Manage text processing, chunking, and embedding generation.
- **OpenAI API**: Generate embeddings and answer user queries via GPT-3.5.
- **FAISS**: Efficient vector database for fast similarity searches.
- **Pickle**: Save and load vector embeddings to avoid recomputing.

---

## 🛠 Installation

To run this project locally, follow these steps:

1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/ATS-Resume-Breaker.git
   ```

2. **Navigate to the project folder**:
   ```bash
   cd ATS-Resume-Breaker
   ```

3. **Create and activate a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set your OpenAI API key**:
   - You need an OpenAI API key. You can get it from [here](https://platform.openai.com/account/api-keys).
   - Once you have your key, set it in your environment variables:
     ```bash
     export OPENAI_API_KEY="your-api-key"
     ```

6. **Run the app**:
   ```bash
   streamlit run app.py
   ```

7. Open your browser and go to `http://localhost:8501` to start using the ATS Resume Breaker!

---

## 🚀 Usage

1. **Upload a Resume**: Click the "Upload Resume" button to upload a PDF resume.
2. **Ask Questions**: Type your questions about the resume (e.g., "What is the candidate's skillset?").
3. **View Answers**: After submitting the question, the tool will display AI-generated answers based on the resume content.

---

## ⚙️ How It Works

1. **Resume Upload**: The user uploads a PDF resume.
2. **Text Extraction**: The tool uses `PyPDF2` to extract text from the PDF.
3. **Text Chunking**: The extracted text is split into chunks using `RecursiveCharacterTextSplitter` for efficient processing.
4. **Embedding Generation**: The text chunks are converted into vector embeddings using OpenAI API.
5. **Vector Store**: The embeddings are stored using **FAISS** to enable fast similarity searches.
6. **Question Processing**: When the user asks a question, the system searches the vector database and uses the OpenAI model to generate answers.
7. **Answer Suggestion**: The system also generates automated answer suggestions using GPT-2.

---

## 🧩 Challenges & Solutions

- **PDF Parsing**: Extracting clean and usable text from PDF resumes with different formats.  
   ✅ **Solution**: Used `PyPDF2` to read and extract text from the PDF, ensuring robust parsing.
  
- **Handling Large Texts**: Managing long resumes and ensuring the text is divided into manageable chunks without losing context.  
   ✅ **Solution**: Used `RecursiveCharacterTextSplitter` to split text into coherent chunks.

- **Vector Embeddings**: Converting large text chunks into embeddings for fast retrieval.  
   ✅ **Solution**: Implemented **FAISS** for fast vector similarity searches.

- **Query Accuracy**: Ensuring the AI model provides accurate answers based on the resume content.  
   ✅ **Solution**: Leveraged OpenAI's GPT-3.5 for precise question-answering.

---

## 📈 Future Improvements

- **Enhanced PDF Parsing**: Improve parsing capabilities to handle more complex resume layouts and formats.
- **Multi-language Support**: Add support for resumes in different languages.
- **Personalized Insights**: Allow users to store resumes and preferences for faster insights.
- **More Advanced Queries**: Enhance the query system with more sophisticated NLP models and capabilities.

---

## 🎯 Contributing

We welcome contributions! If you have suggestions or improvements for this project, feel free to fork the repository, make your changes, and submit a pull request.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---



#  OUTPUT

![output main](https://github.com/abhishekpsonawane07/ATS_Resume_Breaker/assets/120458850/4027a46b-5c3f-4d0d-b1d3-46913386ca2a)



![output 2](https://github.com/abhishekpsonawane07/ATS_Resume_Breaker/assets/120458850/47526a7c-d234-44a8-9db0-b726e430c94f)



