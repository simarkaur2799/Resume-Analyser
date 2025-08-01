import fitz  # PyMuPDF
import docx
import tempfile

def extract_text_from_pdf(file_bytes):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(file_bytes)
        tmp.flush()
        doc = fitz.open(tmp.name)
        return " ".join(page.get_text() for page in doc)

def extract_text_from_docx(file_bytes):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp.write(file_bytes)
        tmp.flush()
        doc = docx.Document(tmp.name)
        return "\n".join([p.text for p in doc.paragraphs])

def extract_text(file: bytes, filename: str) -> str:
    if filename.endswith(".pdf"):
        return extract_text_from_pdf(file)
    elif filename.endswith(".docx"):
        return extract_text_from_docx(file)
    elif filename.endswith(".txt"):
        return file.decode("utf-8")
    else:
        raise ValueError("Unsupported file type.")
