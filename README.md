# EvidenceAI
 EvidenceAI is a citation-first Retrieval-Augmented Generation (RAG) system that answers questions using evidence retrieved from a private collection of documents.

 ## Project Goal

 Build an end-to-end RAG application featuring:

 - PDF ingestion with page-level metadata
 - Configurable document chunking
 - Semantic and lexical retrieval
 - Hybrid search and reranking
 - Grounded LLM-generated answers
 - Source citations and insufficient-evidence handling
 - Retrieval and generation evaluation
 - FastAPI backend and Streamlit interface

 ## Current status

 Day 2 complete - PDF ingestion and page-level text extraction.

## Implemented So Far

- Project environment and repository structure
- Initial AI/ML research paper corpus
- PDF ingestion using PyPDF
- Page-level text extraction
- Document name and page-number metadata preservation
- Empty-page handling

The current corpus contains 10 PDFs. The ingestion pipeline successfully extracted 146 pages with 0 empty pages detected.

## Initial Technology Stack

- Python 3.10
- Sentence Transformers
- Qdrant
- PyPDF
- NumPy
- pandas

## Next Step

Day 3 - implement document chunking while preserving source metadata.