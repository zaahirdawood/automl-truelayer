# Model Payment Failures at TrueLayer - Documentation

## Feature Engineering Process
1. **Data Cleaning**: Ensure the dataset is free from missing values and inconsistencies.
2. **Feature Creation**: 
   - **Time-based Features**: Extract day of the week, month, and hour from transaction timestamps to capture temporal patterns.
   - **Aggregated Features**: Calculate rolling averages of transaction amounts to identify trends over time.
3. **Feature Scaling**: Apply techniques like Min-Max Scaling or Standardization to ensure all features contribute equally to model performance.

## Model Selection
- **Model Type**: A pipeline was created using TPOT, an automated machine learning tool that optimizes machine learning pipelines.
- **Justification**: The choice of TPOT allows for the exploration of various models and hyperparameters, ensuring the best-performing model is selected based on the dataset characteristics.

## Training
- The model was trained using a dataset of payment transactions, with features engineered to enhance predictive power.
- The training process involved splitting the data into training and testing sets to validate model performance.

## Evaluation
- **Metrics Used**: The model's performance was evaluated using the F1 score, particularly focusing on the weighted F1 score to account for class imbalances.
- **ROC Curve**: The Receiver Operating Characteristic (ROC) curve was plotted to visualize the trade-off between true positive and false positive rates, with an emphasis on achieving a high area under the curve (AUC).

## Deployment Strategy
- The trained model and pipeline were exported using joblib for future predictions.
- The model is saved as `winner.pkl` in the `models` directory, ensuring it can be easily loaded for inference in production environments.
- A results file (`results.txt`) is generated to log the final model score, facilitating monitoring and evaluation post-deployment.

## Conclusion
This documentation outlines the comprehensive approach taken to engineer features, select and train a model, evaluate its performance, and deploy it effectively. The focus on high recall for failed payments ensures that the model meets business requirements while maintaining a balance with successful payment predictions.