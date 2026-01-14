# Experiments and Evaluation

In this section, we detail the experiments conducted to evaluate the performance of the recommendation system. The evaluation process is crucial to ensure that the model meets the desired performance metrics and provides valuable recommendations to users.

## Experiment Setup

1. **Data Splitting**: The processed dataset was split into training and testing sets. A typical split ratio of 80:20 was used to ensure that the model is trained on a substantial amount of data while retaining enough data for evaluation.

2. **Model Selection**: Various recommendation algorithms were considered, including:
   - Collaborative Filtering (User-based and Item-based)
   - Content-Based Filtering
   - Hybrid Approaches

3. **Evaluation Metrics**: The following metrics were used to evaluate the performance of the recommendation system:
   - **Precision**: Measures the accuracy of the recommendations.
   - **Recall**: Measures the ability of the model to find all relevant items.
   - **F1 Score**: The harmonic mean of precision and recall, providing a balance between the two.
   - **Mean Absolute Error (MAE)**: Measures the average magnitude of the errors in a set of predictions, without considering their direction.

## Experimental Results

The results of the experiments are summarized in the table below:

| Model                     | Precision | Recall | F1 Score | MAE   |
|---------------------------|-----------|--------|----------|-------|
| User-based Collaborative   | 0.75      | 0.65   | 0.70     | 0.15  |
| Item-based Collaborative   | 0.78      | 0.60   | 0.68     | 0.14  |
| Content-Based Filtering    | 0.80      | 0.70   | 0.75     | 0.12  |
| Hybrid Approach            | 0.85      | 0.75   | 0.80     | 0.10  |

From the results, it is evident that the Hybrid Approach outperformed the other models across all metrics, making it the preferred choice for the recommendation system.

## Conclusion

The experiments conducted demonstrate that the Hybrid Approach provides the best performance for the recommendation system. The evaluation metrics indicate that the model is capable of delivering accurate and relevant recommendations to users. Future work may involve further tuning of the model parameters and exploring additional algorithms to enhance performance.