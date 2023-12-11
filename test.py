import pdfplumber 
from hfcb_lang import HuggingChat as HCA
import os

llm = HCA(email=os.getenv("EMAIL"), psw=os.getenv("PASSWORD"), cookie_path="./cookies_snapshot")

def extract_text_from_pdf(pdf_path, start_page=0, end_page=None):
    content = ""
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            if i >= start_page:
                if end_page is not None and i < end_page:
                    content += page.extract_text()
                elif end_page is None:
                    content += page.extract_text()

    return content

def get_response(content):
    query = "Summarize the chapter for me: " + content
    response = llm(query)
    return response

def interactive_chat():
    pdf_path = "test_ncert.pdf"
    content = extract_text_from_pdf(pdf_path, start_page=5, end_page=10)

    while True:
        query = input("Enter query: ")
        prompt = "The content is: " + content + "\n\n" + "The query is: " + query
        response = llm(prompt)
        print("AI response: ", response)

        conti = input("Continue? (y/n): ")
        if conti == "n":
            break

if __name__ == "__main__":
    interactive_chat()
        