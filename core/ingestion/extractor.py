from backend.file_handler import extract_text_from_pdf

def extract_text(file):
    """Wrapper for document ingestion"""
    return extract_text_from_pdf(file)