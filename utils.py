import fitz  # PyMuPDF

def extract_pdf_comments(pdf_path):
    """Extract all comments and their associated text from a PDF file."""
    comments = []
    doc = fitz.open(pdf_path)
    for page_num, page in enumerate(doc, 1):
        for annot in page.annots():
            content = annot.info.get("content", "")
            rect = annot.rect
            text = page.get_text("text", clip=rect)
            if len(content) == 0 or len(text.strip()) == 0:
                continue
            if content.lower().strip() == "ok" or content.lower().strip() == "oh":
                comment_text = f"Highlighted text on page {page_num}: {text.strip()}"
            else:
                comment_text = f"Comment on page {page_num}: {content}\nAssociated text: {text.strip()}"
            comments.append(comment_text)
    
    doc.close()
    return comments
