"""
Machine Learning Fundamentals - Practice Exercises
===================================================

Core ML concepts: train/test split, linear regression,
classification, model evaluation.

Run with Claude Code: "Run ML exercise 1"

Prerequisites: Python, NumPy, Pandas basics
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    mean_squared_error, r2_score,
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report
)

# =============================================================================
# EXERCISE 1: Train/Test Split
# =============================================================================
"""
Practice splitting data for model training and evaluation.
"""

def create_sample_data():
    """Generate sample data for exercises"""
    np.random.seed(42)
    n = 200

    X = pd.DataFrame({
        'feature1': np.random.randn(n),
        'feature2': np.random.randn(n) * 2,
        'feature3': np.random.randn(n) + 1
    })

    # Regression target
    y_reg = 3 * X['feature1'] + 2 * X['feature2'] - X['feature3'] + np.random.randn(n) * 0.5

    # Classification target
    y_clf = (X['feature1'] + X['feature2'] > 0).astype(int)

    return X, y_reg, y_clf

def basic_train_test_split(X, y, test_size=0.2):
    """
    Split data into training and test sets.

    Requirements:
    - 80% training, 20% test
    - Set random_state=42 for reproducibility

    Return: X_train, X_test, y_train, y_test
    """
    pass

def stratified_split(X, y, test_size=0.2):
    """
    Split classification data with stratification.
    Ensures class proportions are preserved in both sets.

    Return: X_train, X_test, y_train, y_test
    """
    pass

def create_validation_set(X, y, test_size=0.2, val_size=0.2):
    """
    Create train/validation/test split.

    Example: 60% train, 20% validation, 20% test

    Return: X_train, X_val, X_test, y_train, y_val, y_test
    """
    pass


# =============================================================================
# EXERCISE 2: Linear Regression
# =============================================================================
"""
Build and evaluate linear regression models.
"""

def train_linear_regression(X_train, y_train):
    """
    Train a linear regression model.

    Return: trained model
    """
    pass

def predict_and_evaluate_regression(model, X_test, y_test):
    """
    Make predictions and calculate metrics.

    Return: dict with 'predictions', 'mse', 'rmse', 'r2'
    """
    pass

def get_feature_importance_linear(model, feature_names):
    """
    Get feature importance from linear regression coefficients.

    Return: DataFrame with 'feature' and 'coefficient' columns,
            sorted by absolute coefficient value (descending)
    """
    pass


# =============================================================================
# EXERCISE 3: Logistic Regression Classification
# =============================================================================
"""
Build and evaluate classification models.
"""

def train_logistic_regression(X_train, y_train):
    """
    Train a logistic regression classifier.

    Return: trained model
    """
    pass

def predict_and_evaluate_classification(model, X_test, y_test):
    """
    Make predictions and calculate classification metrics.

    Return: dict with:
        'predictions': array
        'accuracy': float
        'precision': float
        'recall': float
        'f1': float
        'confusion_matrix': array
    """
    pass

def predict_probabilities(model, X_test):
    """
    Get probability predictions instead of class labels.

    Return: array of shape (n_samples, 2) with probabilities
            for each class
    """
    pass


# =============================================================================
# EXERCISE 4: Decision Tree Classifier
# =============================================================================
"""
Build decision tree models and understand their behavior.
"""

def train_decision_tree(X_train, y_train, max_depth=None):
    """
    Train a decision tree classifier.

    Parameters:
    - max_depth: maximum depth of tree (None = no limit)

    Return: trained model
    """
    pass

def compare_tree_depths(X_train, X_test, y_train, y_test, depths=[2, 5, 10, None]):
    """
    Train trees with different max_depth values and compare.

    Return: DataFrame with columns:
        'max_depth', 'train_accuracy', 'test_accuracy'

    This demonstrates overfitting as depth increases.
    """
    pass

def get_feature_importance_tree(model, feature_names):
    """
    Get feature importance from decision tree.

    Return: DataFrame with 'feature' and 'importance' columns,
            sorted by importance (descending)
    """
    pass


# =============================================================================
# EXERCISE 5: Feature Scaling
# =============================================================================
"""
Understand when and how to scale features.
"""

def scale_features(X_train, X_test):
    """
    Apply StandardScaler to features.

    Important: Fit on training data, transform both train and test.

    Return: X_train_scaled, X_test_scaled, scaler
    """
    pass

def compare_with_without_scaling(X_train, X_test, y_train, y_test):
    """
    Compare logistic regression performance with and without scaling.

    Return: dict with:
        'accuracy_unscaled': float
        'accuracy_scaled': float
    """
    pass


# =============================================================================
# EXERCISE 6: Cross-Validation
# =============================================================================
"""
Implement cross-validation for more robust evaluation.
"""

from sklearn.model_selection import cross_val_score, KFold

def basic_cross_validation(X, y, model, cv=5):
    """
    Perform k-fold cross-validation.

    Return: dict with:
        'scores': array of scores for each fold
        'mean': mean score
        'std': standard deviation of scores
    """
    pass

def compare_models_cv(X, y, models_dict, cv=5):
    """
    Compare multiple models using cross-validation.

    models_dict = {
        'LogisticRegression': LogisticRegression(),
        'DecisionTree': DecisionTreeClassifier()
    }

    Return: DataFrame with 'model', 'mean_score', 'std_score'
    """
    pass


# =============================================================================
# BONUS: Model Pipeline
# =============================================================================
"""
Create a complete ML pipeline.
"""

from sklearn.pipeline import Pipeline

def create_ml_pipeline():
    """
    Create a pipeline that:
    1. Scales features (StandardScaler)
    2. Applies logistic regression

    Return: sklearn Pipeline object
    """
    pass

def full_ml_workflow(X, y):
    """
    Complete ML workflow:
    1. Train/test split (80/20)
    2. Create and fit pipeline
    3. Evaluate on test set
    4. Return metrics and predictions

    Return: dict with all relevant metrics and the trained pipeline
    """
    pass


# =============================================================================
# TEST RUNNER
# =============================================================================
if __name__ == "__main__":
    print("Machine Learning Exercises - Run with Claude Code")
    print("=" * 50)
    print("\nExample: 'Run ML exercise 1'")
    print("\nExercises:")
    print("1. Train/Test Split")
    print("2. Linear Regression")
    print("3. Logistic Regression Classification")
    print("4. Decision Tree Classifier")
    print("5. Feature Scaling")
    print("6. Cross-Validation")
    print("Bonus: Model Pipeline")

    # Generate sample data for testing
    X, y_reg, y_clf = create_sample_data()
    print(f"\nSample data created: {X.shape[0]} samples, {X.shape[1]} features")
