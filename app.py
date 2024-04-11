import streamlit as st
from dotenv import load_dotenv
import pickle
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
import os

os.environ['OPENAI_API_KEY'] = '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'

# Set page layout
st.set_page_config(
    page_title="ATS Resume Breaker",
    page_icon="💼",
    layout="wide"
)

# Sidebar contents
with st.sidebar:
    st.title('ATS Resume Breaker 💬')
    st.markdown('''
    ## About
    This app is an ATS Resume Breaker powered by LangChain and OpenAI.
    - Extracts insights from resumes in PDF format.
    - Uses OpenAI's language model for question-answering.
    - Enhance your hiring process with AI!
    ''')
    st.write("")  # Adds a line break
    st.write('Made by Team 8 AI&DS')

# Main content
def main():
    st.header("Welcome to ATS Resume Breaker 💼💬")
    st.subheader("Upload your PDF resume and ask questions!")

    openai_api_key = os.getenv('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')
    load_dotenv()

    # Upload a PDF file
    pdf = st.file_uploader("Choose a PDF file", type='pdf')

    if pdf is not None:
        pdf_reader = PdfReader(pdf)

        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text=text)

        # Embeddings
        store_name = pdf.name[:-4]

        if os.path.exists(f"{store_name}.pkl"):
            with open(f"{store_name}.pkl", "rb") as f:
                VectorStore = pickle.load(f)
        else:
            embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
            VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
            with open(f"{store_name}.pkl", "wb") as f:
                pickle.dump(VectorStore, f)

        # Accept user questions/query
        query = st.text_input("Ask questions about your resume:")
        st.write("")  # Adds a line break

        if st.button("Get Insights"):
            if query:
                docs = VectorStore.similarity_search(query=query, k=3)

                llm = OpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)
                chain = load_qa_chain(llm=llm, chain_type="stuff")
                with get_openai_callback() as cb:
                    response = chain.run(input_documents=docs, question=query)

                # Display response
                st.subheader("Response:")
                st.write(response)

if __name__ == '__main__':
    main()
