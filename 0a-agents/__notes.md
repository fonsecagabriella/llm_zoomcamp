# Introduction to Agents and Retrieval-Augmented Generation (RAG)

📺 [Link to video](https://www.youtube.com/watch?v=GH3lrOsU3AU)
📚 [Link to Jupyter Notebook of the instructions](./workshop.ipynb)

The classical RAG pipeline consists of three steps:
1. **SEARCH**: performing a search on a knowledge base
2. **PROMPT**: building a prompt with retrieved context, and
3. **LLM**:    generating an answer using an LLM.

A simple implementation is:

```py
def rag(query):
    search_results = search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(prompt)
    return answer
```



## Classical RAG Implementation

- Different types of searches can be used: in-memory keyword search, ElasticSearch text search, vector search, and hybrid search.
- The search step retrieves relevant documents; then, a prompt is constructed that includes the context and user question.
- The LLM is queried with this prompt to generate a context-aware answer.
- A simple in-memory search engine (minarch) and FAQ documents were used as the knowledge base in [examples](./../02_vector_search/).
- Limitations: classical RAG only answers questions present in the knowledge base and cannot answer off-topic or unseen queries effectively.

## Agentic RAG: Adding Decision-Making to RAG

- Agentic RAG enhances classical RAG by enabling the system (agent) to decide if it can answer directly using its knowledge or if it needs to search the knowledge base. This decision-making makes the assistant more flexible, handling both knowledge base queries and generic questions.
- The agent observes the dialogue environment and decides between two actions: answer immediately or perform a search.
- Implementation involves modifying the prompt to instruct the LLM to choose which action to take based on the presence or absence of context.

## Agentic Search: Multi-Step Iterative Retrieval

- Agentic search extends agentic RAG by allowing multiple iterations of querying the knowledge base.
- The agent can reformulate or refine search queries based on previous search results and previous queries, enabling deeper exploration.
- Maintaining a history of past queries, search results, and actions is crucial for this iterative approach to avoid repeats and improve search quality.
- To prevent infinite loops, the system limits the maximum number of iterations.
- This approach better handles broad or ambiguous questions that require multiple facets of information.-

## Key Insights

⭐️ **Instead of manually parsing and handling JSON outputs from prompts, function calling allows developers to define tools (e.g., search and add-entry functions) that the LM can invoke autonomously.**

🤔 **Agentic RAG enables intelligent decision-making between direct LM answers and knowledge base queries:** By allowing the LM to decide whether to answer immediately or perform a search, the system becomes more flexible, balancing knowledge limitations with retrieval accuracy. This step moves beyond static RAG towards more autonomous AI assistants that can handle a broader range of queries effectively.

🔄 **Iterative multi-step search improves answer quality through query reformulation and context accumulation:** Agentic search leverages multiple rounds of querying with memory of past searches and results, allowing the LM to refine its search strategy dynamically. This mimics human research behavior and significantly boosts the quality of responses on complex or ambiguous questions.

🛠️ **Function calling abstracts tool invocation and simplifies complex agent workflows:** Instead of manually parsing prompt outputs and coding conditional logic for each possible action, function calling lets developers define available functions/tools declaratively. The LM autonomously chooses which functions to call, streamlining development and improving maintainability, especially as the number of tools grows.

💬 **Maintaining conversation history and state is crucial for creating interactive, context-aware chatbots:** The instructor demonstrates how to preserve action history, search queries, and dialogue context across multiple user interactions and function calls. This memory enables follow-up questions and contextual answers, essential for natural and engaging user experiences.

🔧 **Extensibility through modular tool addition enhances the agent’s capabilities over time:** By designing the system to support adding new functions (e.g., adding FAQs), the agent can evolve and improve continuously without major rewrites. This modularity supports real-world applications requiring ongoing updates and customizations.

⚠️ **Prompt engineering remains an art and science, especially when designing agentic behaviors and multi-turn interactions:** The complexity of prompts increases with agent sophistication, requiring careful crafting and iterative testing. While function calling reduces some complexity, understanding prompt design principles remains vital for tuning agent performance.

💡 **Practical considerations such as persistence, input validation, and provider compatibility impact deployment:** The demo uses an in-memory index without persistence, which is suitable for demos but not real-world usage. Input validation guardrails are necessary to prevent unwanted behaviors. Additionally, function calling currently depends on provider support (e.g., OpenAI), so fallback strategies may be required for other LLMs.