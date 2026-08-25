# Day 2 - PDF Ingestion

## Goal

Build the first stage of the EvidenceAI document pipeline by extracting page-level text from PDF research papers while preserving source metadata.

## What I built

Created `src/ingestion/pdf_loader.py` with an `extract_pdf_pages()` function using `pypdf`.

Each extracted page is represented as:

{
    "document": "filename.pdf",
    "page": page_number,
    "text": "extracted_text"
}

The loader was tested across all 10 PDFs in the initial EvidenceAI corpus.

### Results

- 10 PDFs processed successfully
- 146 pages extracted
- 0 empty pages detected

## What I learned

- How `PDFReader` from `pypdf` opens and reads PDFs.
- How to extract text page by page using `page.extract_text()`
- Why document names and page numners must be preserved for future citations.
- Why PDF text extraction may not perfectly perserve equations, subscripts, superscripts, and layout.
- How `page.extract_text() or ""` prevents missing text from becoming `None`.
- How `.strip()` can be used to detect pages containing only whitespace.
- How `Path.glob("*.pdf")` can find all PDF files inside a directory.
- How Python list indexing relates to PDF page records, e.g. `pages[0]` represents the first extracted page.

## Problems/ Observations

- I initially ran the Python file without saving it, so the new test code did not execute.
- Printing the entire page dictionary produced a very large and messy terminal output.
- Mathematical notation on page 5 of *Attention Is All You Need* was not recontructed perfectly by `pypdf`.

This showed that PDF extraction is not always identical to the visual representation of a PDF.

## Why This Matters for EvidenceAI

EvidenceAI needs to know not only what text it retrieves, but where that text came from.

Preserving:

- document name
- page number
- extracted text

will later allow retrieved evidence to be traced back to its original source and cited in generated answers.

## Next

Day 3: Chunking

Convert extracted page text into smaller searchable chunks while preserving metadata such as :

- chunk ID
- document
- page
- text

Then manually inspect chunk quality before moving on to embeddings.