# Day 1 - Project Setup

**Date:** 24 August 2026

## Completed

- Created the EvidenceAI project structure
- Created and activated a Python 3.10 virtual environment
- Installed the initial dependencies
- Verified all core library imports
- Created a reproducible requirements file
- Initialized Git and connected the GitHub repository
- Downloaded a 10-paper corpus covering transformers, retrieval and RAG

## What I learned

- A virtual environment isolates project dependencies from global Python packages.
- 'requirements.txt' records the package versions needed to reproduce the environment. 
- Git does not track empty directories, so placeholder files preserve the structure.
- '.gitignore' prevents environments, secrets, generated data and local PDFs from entering the repository.

## Issue encountered

GitHub rejected an outdated or invalid stored credential. Re-authenticating through Git Credential Manager resolved the problem.

## Next Step

Build the PDF-ingestion pipeline and extract page-level text while preserving document names and page numbers.