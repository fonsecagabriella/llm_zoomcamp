# Best practices - LLM Zoomcamp | Week 05

## 01. Techniques to improve RAG pipeline

- **Stage 01: Indexing stage**
    - 1. Parse initial documents (FAQ)
    - 2. Split texts into chunks or paragraphs (question block)
    - 3. Embed each chuck into a vector
    - 4. Store those vectors in a database

- **Stage 02: Answering stage**
    - 1. Turn user question into a vector form
    - 2. Extract top k documents from the database
    - 3. Show our question and the most relevant documents to LLM
    - 4. LLM returns the answer

### **Tips to improve retrieval**

- **Small-to-big chunk retrieval**
    - Problem of choosing the right embedding size of chuncks
    - Use small chunks on indexing stage and large chunks on answering stage

- **Leveraging document metadata**
    - Adding metadata can be useful (simple document name, data and path)
    - Ask LLM to produce metadata

- **Hybrid search**
    - Combine 2 methods: vector-based search and keyword-based search in a pipeline
    - Vector search is looking for the closest chunks in the embedding space (semantic search)
    - Keyword search is looking for the matches of the separate words (lexical search)

- **User query rewriting:** Users are not always good in formulating their questions, so you can use LLM to reformulate questions in a better-structred way

- **Document reranking**
    - Documents with the highest embedding similarity may not be the most relevant
    - Rerank the retrieved document chunks (ie. using LLM)