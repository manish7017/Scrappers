import PyPDF2

# Define the path to the PDF file
pdf_path = "Manish's Resume.pdf"

# List of words to check for
target_words = ["C++", "Python", "javascript", "linux"]

# Open the PDF file
with open(pdf_path, "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    target_words_found = False

    for page_num in range(len(pdf_reader.pages)):
        page_text = pdf_reader.pages[page_num].extract_text()

        for word in target_words:
            if word.lower() in page_text.lower():
                print(f'Page {page_num + 1}: Found "{word}"')
                target_words_found = True

    if not target_words_found:
        print("No target words found in the PDF.")
