from pathlib import Path
from pypdf import PdfReader

def extract_pdf_pages(pdf_path):
    pdf_path = Path(pdf_path)

    reader = PdfReader(pdf_path)

    pages = []

    for page_number, page in enumerate(reader.pages,start=1):
        text = page.extract_text() or ""

        pages.append(
            {
                "document": pdf_path.name,
                "page": page_number,
                "text": text,
            }
        )


    return pages


