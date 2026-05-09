import pandas as pd
import numpy as np

# Dataset
data = {
    'user_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'nb_orders': [5, 0, 3, None, 8, 1, 0, 4, 7, 2],
    'avg_order_value': [120, 45, None, 200, 310, 80, 55, 175, 400, 90],
    'days_since_last_order': [10, 90, 30, 5, None, 60, 120, 20, 3, 45],
    'nb_complaints': [0, 2, 0, 1, 0, 3, 1, 0, 0, 2],
    'churned': [0, 1, 0, 0, 0, 1, 1, 0, 0, 1]
}
df = pd.DataFrame(data)

# YOUR TASKS:
# 1. Handle missing values (justify your strategy)
# For simplicity, we'll fill missing values with the median of each column.
# Justification: The median is a robust measure of central tendency that is not affected by outliers, making it a good choice for filling missing values in this context.
# Alternatively, I could use mean, default value, or even a predictive model to fill missing values, but median is a simple and effective approach for this dataset.
df['nb_orders'].fillna(df['nb_orders'].median(), inplace=True)
df['avg_order_value'].fillna(df['avg_order_value'].median(), inplace=True)
df['days_since_last_order'].fillna(df['days_since_last_order'].median(), inplace=True)

# 2. Create a feature: "high_value_customer" (avg_order_value > 150)
df['high_value_customer'] = df['avg_order_value'] > 150

# 3. Create a feature: "at_risk" (days_since_last_order > 50 AND nb_complaints > 0)
df['at_risk'] = (df['days_since_last_order'] > 50) & (df['nb_complaints'] > 0)
# 4. Train a classifier to predict "churned" (any sklearn model)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

X_train, X_test, y_train, y_test = train_test_split(df.drop(columns=['user_id', 'churned']), df['churned'], test_size=0.2, random_state=42, train_size=0.8)
cls = RandomForestClassifier(n=5, random_state=42).fit(X_train, y_train)
y_pred = cls.predict(X_test)
print(classification_report(y_test, y_pred, target_names=['Not Churned', 'Churned']))
# 5. Print: precision, recall, F1 for the positive class
precision = classification_report(y_test, y_pred, output_dict=True)
precision_churned = (y_pred == y_test).sum() / (y_pred == 1).sum()
TP = ((y_test == 1) & (y_pred == 1)).sum()  # True Positives
FP = (y_pred == 1).sum() - TP  # False Positives
precision_churned = TP / (TP + FP) if (TP + FP) > 0 else 0
FN = (y_test == 1).sum() - TP  # False Negatives
recall_churned = TP / (TP + FN) if (TP + FN) > 0 else 0
f1_churned = 2 * (precision_churned*recall_churned) / (precision_churned + recall_churned) if (precision_churned + recall_churned) > 0 else 0
# 6. BONUS: What would you do differently with 100k rows?
# With 100k rows, I would consider using more sophisticated techniques for handling missing values, such as using a predictive model to impute missing values based on other features. I would also consider using more complex models for classification, such as gradient boosting or deep learning models, and I would perform hyperparameter tuning to optimize model performance. Additionally, I would implement cross-validation to ensure that the model generalizes well to unseen data. Finally, I would also consider feature engineering and selection techniques to improve model performance and reduce overfitting.