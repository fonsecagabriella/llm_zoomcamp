# dlt + Cognee + Kuzu

With [the flow of this notebook](./cognee_taxi_dataset_demo.ipynb) in mind you can treat **dlt** as the conveyor belt**, **Cognee as the brain** that learns and reasons over the data, and **Kuzu as the ultra-fast filing cabinet** that stores the brain’s structured memory.

## dlt – Data-Load Tool (ELT in pure Python)
**What it is: a lightweight, open-source ELT framework.** 
You write normal Python functions to fetch data (“resources”) and dlt takes care of pagination, schema inference, incremental loading and writing to dozens of destinations 

- Why it’s in the notebook: to fetch a live REST dataset without building a one-off scraper, and to hand you a clean dataframe you can feed straight into Cognee.

## Cognee – AI Memory / Knowledge-Graph layer
**What it is: an open-source “memory engine” that turns arbitrary text, tables, media, or conversation logs into a hybrid knowledge-graph + vector store** in just a few lines. 
It replaces ad-hoc RAG glue with a declarative E-C-L (Extract → Cognify → Load) pipeline and already speaks to 30 + data sources 


Key concepts you’ll meet in the notebook:
- `add()` – ingest raw objects (text or DataFrame rows).
- `cognify()` – run the LLM/NER pass that extracts entities & relations.
- `search()` – ask questions; pick a SearchType for keyword, semantic-vector or KG traversal.
- `visualize_graph()` – pop an interactive graph to see what was learned.

## Kuzu – Embedded, high-performance graph database
**What it is: think “DuckDB for graphs”.** 
Kuzu is an in-process, columnar, Cypher-speaking property-graph engine with built-in full-text and vector indices. No separate server, just pip install kuzu and you’re off 

- Why Cognee chooses it by default: it’s fast for analytical traversals, persists to a single file, and its API is a thin Python wrapper—perfect for notebooks and agent memory.

## Structure of the notebook
| Stage                 | Library call(s)                                                  | What happens                                                                                                                                                |
| --------------------- | ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ingest**            | `dlt.resource` → `pipeline.run()`                                | dlt pulls paginated yellow-taxi trips from the Zoomcamp demo API, infers a schema, normalises the JSON and lands it in a tabular form.                      |
| **Persist**           | dlt’s pipeline destination (by default DuckDB in the same Colab) | The raw→modelled data now lives in a local analytical store you can query with SQL or export as a `pandas` DataFrame.                                       |
| **Cognify**           | `await cognee.add(df)` → `await cognee.cognify()`                | Cognee reads the dataframe, converts entities & relations into a **knowledge-graph** plus embeddings, and stores everything in the graph DB you configured. |
| **Store**             | env `GRAPH_DATABASE_PROVIDER="kuzu"`                             | Cognee opens an **embedded Kuzu** database; nothing to install or start separately, the graph sits in the same Python process.                              |
| **Query / Visualise** | `await cognee.search(...)`, `visualize_graph(...)`               | You can ask natural-language or Cypher-like questions. Cognee translates them, Kuzu executes them, and the notebook renders sub-graphs or answer snippets.  |

