# RAG & LM Evaluation - LLM Zoomcamp | Week 03

## 3.1 Evaluation Metrics for Retrieval
📺 [Link to video](https://www.youtube.com/watch?v=APMrUnC_dy0)

- The choice of the best retrieval method highly depends on the dataset characteristics and the specific use case requirements.

- **Ground truth data is crucial for meaningful evaluation**

    - Having a trustworthy gold standard dataset is the backbone of evaluation.
    - Such datasets allow for benchmarking different retrieval techniques fairly and objectively.

## 3.2 Evaluation Metrics
1. **Precision at k (P@k)**:
   - Measures the number of relevant documents in the top k results.
   - Formula: `P@k = (Number of relevant documents in top k results) / k`

2. **Recall**:
   - Measures the number of relevant documents retrieved out of the total number of relevant documents available.
   - Formula: `Recall = (Number of relevant documents retrieved) / (Total number of relevant documents)`

3. **Mean Average Precision (MAP)**:
   - Computes the average precision for each query and then averages these values over all queries.
   - Formula: `MAP = (1 / |Q|) * Σ (Average Precision(q))` for q in Q

4. **Normalized Discounted Cumulative Gain (NDCG)**:
   - Measures the usefulness, or gain, of a document based on its position in the result list.
   - Formula: `NDCG = DCG / IDCG`
     - `DCG = Σ ((2^rel_i - 1) / log2(i + 1))` for i = 1 to p
     - `IDCG` is the ideal DCG, where documents are perfectly ranked by relevance.

5. **Mean Reciprocal Rank (MRR)**:
   - Evaluates the rank position of the first relevant document.
   - Formula: `MRR = (1 / |Q|) * Σ (1 / rank_i)` for i = 1 to |Q|

6. **F1 Score**:
   - Harmonic mean of precision and recall.
   - Formula: `F1 = 2 * (Precision * Recall) / (Precision + Recall)`

7. **Area Under the ROC Curve (AUC-ROC)**:
   - Measures the ability of the model to distinguish between relevant and non-relevant documents.
   - AUC is the area under the Receiver Operating Characteristic (ROC) curve, which plots true positive rate (TPR) against false positive rate (FPR).

8. **Mean Rank (MR)**:
   - The average rank of the first relevant document across all queries.
   - Lower values indicate better performance.

9. **Hit Rate (HR) or Recall at k**:
   - Measures the proportion of queries for which at least one relevant document is retrieved in the top k results.
   - Formula: `HR@k = (Number of queries with at least one relevant document in top k) / |Q|`

10. **Expected Reciprocal Rank (ERR)**:
    - Measures the probability that a user finds a relevant document at each position in the ranked list, assuming a cascading model of user behavior.
    - Formula: `ERR = Σ (1 / i) * Π (1 - r_j) * r_i` for j = 1 to i-1
      - Where `r_i` is the relevance probability of the document at position i.

## 3.3 Ground Truth Dataset Generation

📺 [Link to video](https://www.youtube.com/watch?v=bpxi6fKcyLw)
📕 [Link to notebook](./eval/ground-truth-data.ipynb)

Here we will use a LLM to generate questions for each register we have in the document. This is going to be the "golden results" for our tests.
When we run the questions, they should return exactly the document that was used to generate that question. This is a simple way to generate the **ground truth dataset**, but not necessarily the best.


## 3.4 Evaluation of Text Retrieval Techniques

📺 [Link to video](https://www.youtube.com/watch?v=fdIV4xCsp0c)
📕 [Link to notebook](./eval/evaluate-text.ipynb)

For each query we have in the dataset, we will execute the query and check if the document is actually returned in the results.

We will use the following metrics:
- Hit Rate - We want the relevant documents to be returned
- Mean Reciprocal Rank (MRR) - we want relevant documents to have a high rank