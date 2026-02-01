# Machine Learning Fundamentals

Core concepts every data scientist should know.

---

## The ML Workflow

```
Data → Clean → Split → Train → Evaluate → Deploy
              ↓
         Features
```

### Key Steps

1. **Data Collection** - Gather relevant data
2. **Exploration (EDA)** - Understand distributions, patterns, outliers
3. **Preprocessing** - Clean, handle missing values, encode categories
4. **Feature Engineering** - Create informative features
5. **Train/Test Split** - Never evaluate on training data
6. **Model Selection** - Choose algorithm based on problem type
7. **Training** - Fit model to training data
8. **Evaluation** - Assess on held-out test data
9. **Iteration** - Improve based on results

---

## Problem Types

### Supervised Learning
- **Regression**: Predict continuous value (price, temperature)
- **Classification**: Predict category (spam/not spam, churn/stay)

### Unsupervised Learning
- **Clustering**: Group similar items (customer segments)
- **Dimensionality Reduction**: Reduce features (PCA)

### Key Question
> "What am I predicting, and do I have labels?"

| Have Labels? | Output Type | Problem Type |
|--------------|-------------|--------------|
| Yes | Continuous | Regression |
| Yes | Categorical | Classification |
| No | Groups | Clustering |

---

## Train/Test Split

**Why?** Evaluate on unseen data to estimate real-world performance.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

### Split Ratios
- Small dataset (<1000): 80/20 or use cross-validation
- Medium dataset: 70/15/15 (train/val/test)
- Large dataset: 90/5/5 or 98/1/1

### Key Rules
1. **Never peek at test data** during training/tuning
2. **Fit preprocessing on training only**, then transform test
3. **Use stratification** for imbalanced classification

---

## Bias-Variance Tradeoff

### Bias
- Error from overly simple assumptions
- **High bias** = Underfitting (too simple)
- Model misses relevant patterns

### Variance
- Error from sensitivity to training data fluctuations
- **High variance** = Overfitting (too complex)
- Model memorizes training data, fails on new data

### The Sweet Spot
```
             Error
               │
High Bias      │    ╲      ╱
(Underfit)     │     ╲    ╱   High Variance
               │      ╲  ╱    (Overfit)
               │       ╲╱
               │    Sweet Spot
               └────────────────── Complexity
```

### Signs of Overfitting
- Train accuracy >> Test accuracy
- Model is very complex (deep tree, many features)
- Small training set

### Solutions
- More training data
- Simpler model
- Regularization
- Cross-validation

---

## Model Evaluation

### Regression Metrics

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| MSE | Mean of (actual - predicted)² | Lower is better, penalizes large errors |
| RMSE | √MSE | Same units as target |
| MAE | Mean of \|actual - predicted\| | Average error magnitude |
| R² | 1 - (SS_res / SS_tot) | % of variance explained (1.0 = perfect) |

### Classification Metrics

**Confusion Matrix:**
```
              Predicted
              Pos    Neg
Actual Pos    TP     FN
Actual Neg    FP     TN
```

| Metric | Formula | When to Use |
|--------|---------|-------------|
| Accuracy | (TP+TN) / Total | Balanced classes |
| Precision | TP / (TP+FP) | Cost of false positives high (spam filter) |
| Recall | TP / (TP+FN) | Cost of false negatives high (disease detection) |
| F1 | 2 × (P×R)/(P+R) | Balance precision/recall |

### Precision vs Recall
> **Precision**: "Of things I said were positive, how many actually were?"
> **Recall**: "Of all actual positives, how many did I catch?"

---

## Common Algorithms

### Linear Regression
- Predicts continuous output
- Assumes linear relationship
- Fast, interpretable

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

### Logistic Regression
- Predicts probability of class membership
- Good baseline for classification
- Outputs between 0 and 1

### Decision Trees
- Splits data on feature thresholds
- Easy to interpret
- Prone to overfitting

### Random Forest
- Ensemble of decision trees
- Reduces overfitting via averaging
- Good default choice

### Gradient Boosting (XGBoost, LightGBM)
- Sequentially builds trees to correct errors
- Often wins Kaggle competitions
- Requires tuning

---

## Feature Engineering

### Why It Matters
> "Applied machine learning is basically feature engineering"
> — Andrew Ng

### Common Techniques

**Numeric Features:**
- Scaling (StandardScaler, MinMaxScaler)
- Log transform (for skewed distributions)
- Binning (age → age_group)

**Categorical Features:**
- One-hot encoding (color → is_red, is_blue, is_green)
- Label encoding (for ordinal categories)
- Target encoding (replace category with target mean)

**Date Features:**
- Year, month, day, day_of_week
- Is_weekend, is_holiday
- Days_since_event

**Text Features:**
- Bag of words, TF-IDF
- Word embeddings
- Length, word count

---

## Regularization

Prevents overfitting by penalizing model complexity.

### L1 (Lasso)
- Adds sum of |coefficients| to loss
- Drives some coefficients to zero (feature selection)
- Sparse models

### L2 (Ridge)
- Adds sum of coefficients² to loss
- Shrinks coefficients toward zero
- Keeps all features

### When to Use
- **L1**: Many features, want automatic feature selection
- **L2**: All features potentially useful
- **ElasticNet**: Combine both

---

## Cross-Validation

More robust evaluation by training on multiple splits.

### K-Fold
1. Split data into K parts (folds)
2. Train on K-1 folds, test on remaining 1
3. Repeat K times
4. Average the scores

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5)
print(f"Mean: {scores.mean():.3f}, Std: {scores.std():.3f}")
```

### Benefits
- Uses all data for training and testing
- More reliable estimate of performance
- Essential for small datasets

---

## Class Imbalance

When one class vastly outnumbers another (e.g., 95% negative, 5% positive).

### Problems
- Accuracy is misleading (95% by always predicting negative)
- Model ignores minority class

### Solutions
1. **Resampling**: Oversample minority or undersample majority
2. **Class weights**: Penalize misclassifying minority more
3. **Different metrics**: Use precision, recall, F1, AUC-ROC
4. **SMOTE**: Generate synthetic minority examples

---

## Key Interview Questions

1. **Explain bias-variance tradeoff**
   - Bias = underfitting, Variance = overfitting
   - Need to balance model complexity

2. **When use precision vs recall?**
   - Precision: minimize false positives (spam, recommendations)
   - Recall: minimize false negatives (disease, fraud)

3. **How handle overfitting?**
   - More data, simpler model, regularization, cross-validation

4. **L1 vs L2 regularization?**
   - L1 creates sparse models (feature selection)
   - L2 shrinks all coefficients

5. **How handle class imbalance?**
   - Resampling, class weights, different metrics

---

*Last updated: February 2026*
