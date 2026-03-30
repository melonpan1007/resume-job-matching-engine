import re 

def clean_text(text:str) -> str:
    """Basic text cleaning"""

    text = text.lower()
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r' [^a-zA-Z0-9\s]','', text)

    return text.strip()


#normalized text before representation
