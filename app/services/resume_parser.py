import io
import docx2txt
import fitz  # PyMuPDF

def extract_text_from_file(filename: str, file_stream: io.BytesIO) -> str:
    if filename.endswith(".pdf"):
        text = ""
        with fitz.open(stream=file_stream.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
        return text
    elif filename.endswith(".docx"):
        return docx2txt.process(file_stream)
    else:
        raise ValueError("Unsupported file format")
