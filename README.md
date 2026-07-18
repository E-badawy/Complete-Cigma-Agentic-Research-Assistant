# Cigma Agentic Research Assistant

> **Accelerating Scientific Discovery with Agentic AI**

Cigma Agentic Research Assistant is an enterprise-grade AI research platform designed to automate scientific literature review, evidence synthesis, and research report generation. The system combines Retrieval-Augmented Generation (RAG), semantic search, local knowledge bases, and live scientific literature retrieval to produce comprehensive, evidence-based research reports within minutes.

Unlike traditional chatbots, Cigma is built as an **agentic research workflow**, capable of retrieving information from multiple sources, ranking evidence, generating structured reports, managing research libraries, and citing scientific publications.

---

## Overview

Researchers spend significant time searching databases, reading publications, extracting findings, and writing literature reviews. Cigma streamlines this workflow by integrating modern Large Language Models with semantic retrieval and scholarly search engines.

The platform enables researchers to:

* Build and manage private research libraries.
* Upload scientific papers and institutional documents.
* Search local documents using semantic retrieval.
* Retrieve the latest publications from scientific databases.
* Generate structured research reports.
* Produce properly formatted references.
* Export reports in multiple formats.

---

## Key Features

### Agentic Research Workflow

* Intelligent query understanding
* Context-aware retrieval
* Semantic document ranking
* Multi-source evidence synthesis
* Structured report generation

---

### Retrieval-Augmented Generation (RAG)

* Local document indexing
* Dense vector embeddings
* FAISS similarity search
* Chunk-based retrieval
* Context injection into LLM prompts

---

### Research Library Management

* Create multiple libraries
* Upload PDF documents
* Automatic document indexing
* Metadata generation
* Library statistics

---

### Scientific Literature Search

Supports live retrieval from scholarly sources including:

* OpenAlex
* PubMed
* Online scientific repositories

Results include:

* Title
* Authors
* Abstract
* DOI
* Publication year
* Citation count
* Journal information

---

### AI Report Generation

Generated reports include:

* Executive Summary
* Detailed Analysis
* Key Findings
* Critical Discussion
* Limitations
* Future Research Directions
* References

---

### Export Options

Reports can be exported as:

* PDF
* Microsoft Word (.docx)
* Markdown
* Clipboard copy

---

### Modern User Experience

* Responsive React interface
* Animated research workflow
* Markdown rendering
* Source tracking
* Professional typography
* Dark-inspired scientific theme

---

# System Architecture

```
React + Vite
      │
      ▼
FastAPI REST API
      │
      ▼
Agent Orchestrator
      │
      ├─────────────► Local Knowledge Base
      │                    │
      │                    ▼
      │             FAISS Vector Store
      │
      ├─────────────► OpenAlex API
      │
      ├─────────────► PubMed
      │
      └─────────────► Groq LLM
                           │
                           ▼
                 Structured Research Report
```

---

# Technology Stack

## Frontend

* React
* Vite
* Tailwind CSS
* Framer Motion
* Axios
* React Markdown
* React Icons

---

## Backend

* FastAPI
* Pydantic
* LangChain
* LangGraph
* FAISS
* Sentence Transformers
* Groq API

---

## Machine Learning

* BAAI BGE Embeddings
* Semantic Search
* Dense Vector Retrieval
* Retrieval-Augmented Generation

---

## Scientific Integrations

* OpenAlex
* PubMed
* Local Research Libraries

---

## Document Processing

* PyMuPDF
* PyPDF
* python-docx
* ReportLab

---

## Installation

### Clone the repository

```bash
git clone https://github.com/E-badawy/Complete-Cigma-Agentic-Research-Assistant.git

cd Complete-Cigma-Agentic-Research-Assistant
```

---

## Backend Setup

```bash
cd backend

pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
```

Run the API:

```bash
uvicorn main:app --reload
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

# Project Structure

```
backend/
│
├── app/
│   ├── agents/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── routers/
│   ├── services/
│   └── utils/
│
├── data/
│
├── requirements.txt
└── main.py

frontend/
│
├── src/
│   ├── components/
│   ├── context/
│   ├── hooks/
│   ├── layouts/
│   ├── pages/
│   ├── services/
│   └── api/
│
├── package.json
└── vite.config.js
```

---

# API Overview

## Research

```
POST /agent
```

Generates an AI-powered research report.

---

## Libraries

```
GET /libraries
```

Returns all research libraries.

```
POST /libraries
```

Creates a new library.

```
POST /libraries/upload
```

Uploads and indexes research documents.

```
DELETE /libraries/{library}
```

Deletes a research library.

---

# Current Capabilities

* Semantic document retrieval
* Multi-library support
* AI-powered report generation
* Scientific paper discovery
* Reference generation
* Local document indexing
* Export functionality
* Responsive web interface

---

# Planned Enhancements

* Real-time streaming responses
* Conversational research memory
* Citation style selection (APA, MLA, IEEE, Vancouver)
* Multi-agent orchestration
* Research project management
* Audio report narration
* Knowledge graph visualization
* Multi-language support
* User authentication
* Cloud vector databases
* Collaborative workspaces

---

# Contributing

Contributions are welcome through issues, feature requests, and pull requests. Please ensure that changes follow the project's coding standards and include appropriate documentation where necessary.

---

# Author

**Badawi Aminu Muhammed**

AI/ML Engineer • Data Scientist • Research Analyst

**Portfolio**

https://e-badawy.github.io

**GitHub**

https://github.com/E-badawy

**LinkedIn**

https://www.linkedin.com/in/elameenbadawy

---

> *Cigma Agentic Research Assistant demonstrates how autonomous AI agents, semantic retrieval, and scientific knowledge systems can be integrated to reduce the time from research question to evidence-based insight, enabling researchers to focus more on discovery and less on information retrieval.*
