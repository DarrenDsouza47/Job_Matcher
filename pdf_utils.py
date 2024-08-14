import pypdf
from io import BytesIO

def extract_text_pdf(pdf_file):
    text=""
    if pdf_file is not None:
        with BytesIO(pdf_file.read()) as pdf_buffer:
            pdf_reader=pypdf.PdfReader(pdf_buffer)
            for page in pdf_reader.pages:
                text+=page.extract_text()
    return text