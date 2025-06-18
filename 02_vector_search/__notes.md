# Vector Search - LLM Zoomcamp | Week 02



## 2.1 Introduction to Vector Search & qdrant

📺 [Link to video](https://www.youtube.com/watch?v=cX2vO1q2BGE)
📕 [Notebook](./sematic_search.ipynb)

- **Traditional vs. Vector Search Example**
    - Keyword search: Searching “bats” returns docs containing the word “bat” (e.g., “bat in a cave”).
    - Vector search: Searching “bat” can return images visually resembling bats, bat sounds, or semantically related text like “flying mouse.”

**Vectorization Process**

- Text, images, audio, and video are converted into numeric vectors that encode semantic information.
- Similarity is measured numerically, often with cosine similarity or other vector distance metrics.

**Quadrant’s Technical Characteristics**

- Written in Rust for performance efficiency.
- Open source and freely available.
- Supports scalable search over very large datasets.
- Supports advanced vector search capabilities beyond semantic similarity (referenced in external documentation).

**Deployment Using Docker 🐳**

- Install qdrant and fastembed:
`pip install -q "qdrant-client[fastembed]>=1.14.2"`

- Run in Docker:
```bash
docker pull qdrant/qdrant

docker run -p 6333:6333 -p 6334:6334 \
   -v "$(pwd)/qdrant_storage:/qdrant/storage:z" \
   qdrant/qdrant
```

## 2.2 Studying the dataset & choosing an embeding model
📺 [Link to video](https://www.youtube.com/watch?v=4lX6sbdrs84)

**🧠 What is an Embedding Model?**
An embedding model is a machine learning model that transforms input data (like text, images, or audio) into vectors — basically, lists of numbers. These vectors capture the semantic meaning of the input in a form that can be compared using math.

In simple terms:
- Input: "I love cats"
- Output: [0.12, -0.03, 0.87, ...] ← a vector (aka "embedding")

The model is trained so that similar inputs produce similar vectors.

**🧭 Why Are Embedding Models Needed?**
Qdrant (and other vector databases) do not understand raw text. Instead, they store and search among vectors.

To make this work:

- You choose an embedding model (like FastEmbed) that suits your task.
- It turns your documents/questions into vectors.
- Qdrant stores these vectors and performs fast similarity search (e.g. cosine similarity or dot product).

When you search, your query is embedded too — then compared to the stored ones to find the most similar.

*Why you can't skip this:*
Without embeddings, Qdrant has no way to measure "semantic closeness" — e.g., knowing that "cat" is more similar to "kitten" than to "car".

**⚡ What is FastEmbed?**
FastEmbed is an open-source Python library that makes it easy to use pretrained embedding models, optimized for performance. It supports fast, local embedding generation using models like all-MiniLM-L6-v2 or bge-small-en, often powered by ONNX.

Benefits:

- No API calls or rate limits (runs locally)
- Works out of the box with Qdrant
- Free and fast


**What is Cosine Search?**
Cosine search (or cosine similarity search) is a method to measure how similar two vectors are, based on the angle between them — not their length.

In vector search (like with Qdrant), you're usually trying to find which documents are most similar to your query. Cosine similarity gives you a score between:

- +1 = perfectly similar (same direction)
- 0 = not similar (90° angle)
- –1 = opposite meaning (exactly opposite direction — rare in embeddings)

## 2.3 Indexing data to Qdrant

📺 [Link to video](https://www.youtube.com/watch?v=TM5WxZ9EqoQ)


- Point: it's a data point, a question in our case

## 2.4 Buiding hybrid search in Qdrant
📺 [Link to video](https://www.youtube.com/watch?v=ZdbIk8AltDU)
📕 [Notebook](./sematic_search.ipynb)

- Hybrid search combines multiple retrieval methods, typically dense embeddings and sparse (keyword-based) vectors, to build a more robust and reliable information retrieval system. It is considered more advanced than using a single search technique.

- Sparse vectors, often used in keyword-based search like BM25, mostly consist of zero values and focus on exact word or phrase matches. Dense vectors, used in semantic search, represent the meaning of texts in a continuous vector space. Sparse vectors have a flexible dictionary able to support new words without retraining, unlike dense models bound to their training data.

- **BM25 is the industry-standard lexical search method** leveraging term frequency (TF) and inverse document frequency (IDF) to rank documents based on exact term matches, rewarding appearances of important terms and penalizing repeated occurrences of the same term.

- **Scores produced by sparse vector models like BM25 are unbounded**, unlike cosine similarity scores used in dense embedding search, which range between -1 and 1. **This difference complicates direct score comparison or combinations**, influencing hybrid search design.

- A typical hybrid approach uses a fast retriever (e.g., a smaller dense model) to fetch candidate documents, then reranks them with a more expensive or precise model (e.g., BM25 sparse model).

- Fusion combines rankings from multiple search methods into a unified ranked list using techniques like Reciprocal Rank Fusion (RRF), which relies on ranking positions rather than raw scores.

- Reranking is a broader term referring to refining initial search results either by heavy models, cross encoders, or business logic rules to improve result quality.

- Reciprocal Rank Fusion Algorithm (RRF) merges ranked outputs from different search methods by assigning intermediate scores based on document positions, not their similarity scores. This approach prefers documents consistently ranked highly across multiple methods.

- **Use Cases for Hybrid Search**: Hybrid search caters to diverse query types: keyword-heavy queries benefit from lexical (sparse) methods, while natural language questions benefit from semantic (dense) methods. This ensures better results for all users, from shopping site searches to chatbot QA systems.