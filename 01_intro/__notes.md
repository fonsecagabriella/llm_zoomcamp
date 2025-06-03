# Introduction - LLM Zoomcamp

➡️ [LLMs options](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/awesome-llms.md#openai-api-alternatives)

## 1.1 Introduction Concepts

📺 [Link to the video](https://www.youtube.com/watch?v=Q75JgLEXMsM)

- **Framework: Retrieval-Augmented Generation (RAG)**
RAG combines two main components: retrieval, meaning search through a knowledge base (in this case, FAQ documents), and generation, where an LLM generates human-like answers using the retrieved context. Retrieval enriches the LLM’s knowledge by providing relevant context that it can use to generate accurate responses.

- **Large Language Models (LLMs) Overview**
LLMs are advanced language models that predict the next token or word based on prior input, but at a much larger scale than simpler models. These models have billions of parameters, trained on massive datasets. Although technically they operate by predicting the next most probable word, their outputs appear as intelligent, conversational responses similar to human communication. Examples include ChatGPT.

- **How LLMs Work in Practice**
The input to an LLM is typically a text prompt, which can include a question and some contextual information. The output is a generation of text that completes the prompt, ideally answering the question in a meaningful way. In standard usage, the model completes the input with a coherent and relevant answer.

- **Necessity of Retrieval in RAG**
While LLMs can answer general knowledge questions directly (e.g., “How do I cook salmon?”), they struggle with specific contextual queries (e.g., “Is it too late to join the course?”) where up-to-date or domain-specific knowledge is needed. Retrieval provides the LLM with access to current, relevant documents that define the knowledge base for those queries.

- **Retrieval Process in the RAG Framework**
The user’s query is first sent to a knowledge base. This knowledge base contains documents or articles (e.g., FAQ entries). The system retrieves relevant documents based on the query, which are then included as context in the LLM prompt. This augmented prompt enables the LLM to generate precise answers based on retrieved evidence rather than relying solely on its pre-trained knowledge.

- **Modular Architecture and Flexibility**
Both components of the RAG framework — the retrieval system and the LLM — are modular and interchangeable. The course demonstrates this by starting with a simple search engine for retrieval and later upgrading to Elasticsearch and vector search techniques. Similarly, the LLM can be swapped between OpenAI models or open-source alternatives by adjusting the prompt accordingly.


## 1.2 Configuring your environment

📺 [Link to the video](https://www.youtube.com/watch?v=ozCpmkbJNJE)

**Option: setting the environment locally with Anaconda"**

- Create the conda environment
`conda create -n llmenv python=3.10`

- Activate the environment **llmenv**
`conda activate llmenv`

- Install the needed packages - available via conda
`conda install jupyter pandas scikit-learn tqdm openai elasticsearch`

- Install the needed packages - available outside conda, if the above returns an error
`pip install openai elasticsearch`

## 1.3 Retrival & Search

📺 [Link to the video Retrival](https://www.youtube.com/watch?v=olvem333Bqo)
📺 [Link to the video Generating Answers](https://www.youtube.com/watch?v=qz316T3U49Q)
👩🏽‍💻 [Link to workshop - Building your own search engine](https://github.com/alexeygrigorev/build-your-own-search-engine/blob/main/notebook.ipynb)

- Documents containing FAQ data should be parsed in Json for efficiency: [parser script](./parse-faq.ipynb)

## 1.4 Running ElasticSearch

📺 [Link to the video](https://www.youtube.com/watch?v=1lgbR5wMvsI)

👩🏽‍💻 [Working file](./rag-intro.ipynb)

- Running ElasticSearch from Docker:

```bash
docker run -it \
    --rm \
    --name elasticsearch \
    -m 4GB \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    docker.elastic.co/elasticsearch/elasticsearch:8.4.3
```

If the previous command doesn't work (i.e. you see "error pulling image configuration"), try to run ElasticSearch directly from Docker Hub:

```bash
docker run -it \
    --rm \
    --name elasticsearch \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    elasticsearch:8.4.3
```

- Test if works in the terminal `curl https://localhost:9200/`

- Index settings:

```bash
{
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
        "properties": {
            "text": {"type": "text"},
            "section": {"type": "text"},
            "question": {"type": "text"},
            "course": {"type": "keyword"} 
        }
    }
}
```

- Query:

```bash
{
    "size": 5,
    "query": {
        "bool": {
            "must": {
                "multi_match": {
                    "query": query,
                    "fields": ["question^3", "text", "section"],
                    "type": "best_fields"
                }
            },
            "filter": {
                "term": {
                    "course": "data-engineering-zoomcamp"
                }
            }
        }
    }
}

```
