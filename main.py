import fitz  # PyMuPDF
import os

# Hardcoded path to the PDF file
pdf_path = "./.pdf_files/YV1XZEHR3R2326083.pdf"

def extract_text_from_pdf(pdf_path):
    # Check if the file exists
    if not os.path.isfile(pdf_path):
        print(f"Error: The file '{pdf_path}' does not exist.")
        return
    
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Initialize an empty string to hold the text
    pdf_text = ""
    
    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pdf_text += page.get_text()
    
    return pdf_text

def save_text_to_file(text, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    text = extract_text_from_pdf(pdf_path)
    if text:
        output_file = pdf_path = "./.output/extracted_text.txt"
        save_text_to_file(text, output_file)
        print(f"Extracted text saved to '{output_file}'.")
