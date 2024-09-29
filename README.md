Predictive Model for Payment Outcomes

Overview

This project focuses on building a predictive model to classify payment outcomes (successful or failed). The modeling pipeline includes feature engineering, model selection, training, evaluation, and deployment strategy.

Project Files:

* the models folder contains the best v0.0.1 performing model developed `winner.pkl`

* the models folder also contains the `tpot_pipeline.py` the base model pipeline generated using auto-ml

* the results generated for a CI/CD pipeline to pick up in `results.txt`.

* lastly, a `review.csv` for a sense check by an stakeholder to this project.



1. Feature Engineering Process

Feature engineering is crucial for improving model performance. In this project, key transformations included:

•	Time Differences: We calculated time gaps between transactions to capture user behavior patterns, applying logarithmic scaling (np.log) for normalization.

•	Transaction Amount: Logarithmic scaling was applied to transaction amounts to reduce skewness and make the features more uniform.

•	Categorical Encoding: Variables like department and payment method were encoded using one-hot encoding.

•	Missing Data Handling: Missing values were imputed using median or constant values based on feature distribution.

2. Model Selection Process

We experimented with several models, including Logistic Regression, Random Forest, and Extra Trees Classifier. After comparing their performance metrics, we selected the Extra Trees Classifier for its robust handling of non-linear relationships and efficiency in handling high-dimensional data.

Reason for Choosing Extra Trees Classifier:

•	Handling of Imbalanced Data: Extra Trees Classifier performed well with imbalanced datasets, especially after we applied class weights to balance the misclassification costs.

•	Feature Importance: It provides good interpretability by ranking the importance of various features, helping us to understand which aspects of the data drive the model’s predictions.

•	Stability: Extra Trees offers more stability compared to a traditional Random Forest due to the use of a larger subset of the data in constructing decision trees, resulting in reduced variance.

3. Final Model: Extra Trees Classifier (Weighted)

Model Overview

The final model is a Weighted Extra Trees Classifier, which assigns more weight to the minority class (failed payments) to address the class imbalance. This classifier was tuned to maximize recall for the minority class while maintaining strong precision for the majority class.

Model Hyperparameters:

•	Criterion: entropy — used to measure the quality of splits in decision trees.

•	Max Features: 0.1 — controls how many features are considered when splitting nodes.

•	Min Samples Split: 12 — minimum number of samples required to split a node, ensuring the model doesn’t overfit to small subsets.

•	Class Weights: Balanced weights were used to handle the imbalance between failed and successful payments.

4. Model Training and Evaluation

Training Process:

The training data was split into 80% training and 20% testing. We used the Pipeline object from scikit-learn to ensure consistency between feature transformation and model training.

Evaluation Metrics:

We used various evaluation metrics to assess the performance of the model:

	1.	Classification Report:

                precision    recall  f1-score   support

        0       0.41      0.99      0.58     14682
        1       1.00      0.75      0.86     85318

 accuracy                           0.79    100000
macro avg       0.70      0.87      0.72    100000


- **Precision (Class 0 - Failed Payments)**: 0.41
  - This means that when the model predicts a failed payment, it is correct 41% of the time. Lower precision reflects that some successful payments are being misclassified as failed.

- **F1-Score (Class 0 - Failed Payments)**: 0.58
  - The F1-Score balances precision and recall for the failed payment class. It reflects the overall balance between identifying actual failures and minimizing false positives.


#### **Key Observations**:
- **Focus on Recall**: Given the project's goal to minimize the risk of missed failed payments, the model’s high recall for failed payments (0.99) is crucial. The trade-off is that precision for this class is lower (0.41), meaning there are some false positives.
- **Balanced Performance**: The overall accuracy of 79% and the weighted average precision of 0.91 reflect that the model is well-balanced across both classes, especially after applying class weights.
- **AUC-ROC Score**: The score of 0.9199 suggests that the model is capable of distinguishing between successful and failed payments with high accuracy.



6. Conclusion

The Weighted Extra Trees Classifier proved to be the best model for this task, achieving strong recall for failed payments, which is crucial for minimizing undetected failed transactions. The model strikes a good balance between identifying failed payments and maintaining precision for successful ones. Future improvements might involve further tuning of hyperparameters and incorporating additional features from transaction metadata. 
