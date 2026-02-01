# Statistics for Data Science

Essential statistics concepts for interviews and practice.

---

## Descriptive Statistics

### Measures of Central Tendency

| Measure | Description | When to Use |
|---------|-------------|-------------|
| **Mean** | Sum / Count | Symmetric data, no outliers |
| **Median** | Middle value | Skewed data, with outliers |
| **Mode** | Most frequent | Categorical data |

```python
import numpy as np

data = [1, 2, 2, 3, 4, 5, 100]  # 100 is an outlier

np.mean(data)    # 16.7 (pulled by outlier)
np.median(data)  # 3.0 (robust to outlier)
```

### Measures of Spread

| Measure | Description |
|---------|-------------|
| **Range** | Max - Min |
| **Variance** | Average of squared deviations from mean |
| **Standard Deviation** | √Variance (same units as data) |
| **IQR** | Q3 - Q1 (robust to outliers) |

### Percentiles
- **25th percentile (Q1)**: 25% of data below this value
- **50th percentile (Q2)**: Median
- **75th percentile (Q3)**: 75% of data below

---

## Probability Basics

### Key Concepts

**Sample Space**: All possible outcomes
**Event**: A subset of outcomes
**Probability**: P(Event) = Favorable outcomes / Total outcomes

### Rules

```
P(A or B) = P(A) + P(B) - P(A and B)    # Addition
P(A and B) = P(A) × P(B|A)               # Multiplication
P(A|B) = P(B|A) × P(A) / P(B)            # Bayes' Theorem
```

### Independence
Events A and B are independent if:
```
P(A and B) = P(A) × P(B)
```

---

## Distributions

### Normal Distribution
- Bell-shaped, symmetric
- Defined by mean (μ) and standard deviation (σ)
- 68% within 1σ, 95% within 2σ, 99.7% within 3σ

```python
from scipy import stats

# Generate normal data
data = stats.norm.rvs(loc=0, scale=1, size=1000)

# Probability of value < x
stats.norm.cdf(1.96)  # ≈ 0.975
```

### Other Common Distributions

| Distribution | Use Case |
|--------------|----------|
| **Binomial** | Number of successes in n trials |
| **Poisson** | Events per time period |
| **Exponential** | Time between events |
| **Uniform** | Equal probability across range |

---

## Hypothesis Testing

### The Process

1. **State hypotheses**
   - H₀ (null): No effect / no difference
   - H₁ (alternative): There is an effect

2. **Choose significance level (α)**
   - Usually 0.05 (5% chance of Type I error)

3. **Collect data and compute test statistic**

4. **Calculate p-value**
   - Probability of seeing this result if H₀ is true

5. **Make decision**
   - p < α → Reject H₀
   - p ≥ α → Fail to reject H₀

### Errors

| | H₀ True | H₀ False |
|--|---------|----------|
| **Reject H₀** | Type I Error (α) | Correct |
| **Fail to Reject** | Correct | Type II Error (β) |

- **Type I (False Positive)**: Claiming effect when there isn't one
- **Type II (False Negative)**: Missing effect that exists

### P-Value Explained

> "If there really is no effect (H₀ true), how likely is it
> that we'd see a result this extreme?"

- Small p-value: Result is unlikely under H₀ → reject H₀
- Large p-value: Result is plausible under H₀ → can't reject H₀

**Common misconception**: p-value is NOT the probability that H₀ is true

---

## Common Statistical Tests

### Comparing Means

| Test | When to Use |
|------|-------------|
| **1-sample t-test** | Compare sample mean to known value |
| **2-sample t-test** | Compare means of two independent groups |
| **Paired t-test** | Compare means of paired observations |
| **ANOVA** | Compare means of 3+ groups |

```python
from scipy import stats

# Two-sample t-test
group_a = [23, 25, 28, 22, 24]
group_b = [27, 29, 31, 26, 28]

statistic, p_value = stats.ttest_ind(group_a, group_b)
```

### Comparing Proportions
- **Chi-square test**: Compare observed vs expected frequencies
- **Z-test for proportions**: Compare two proportions

### Checking Assumptions
- **Shapiro-Wilk**: Test for normality
- **Levene's test**: Test for equal variances

---

## A/B Testing

Controlled experiment to compare two versions.

### Steps

1. **Define metric**: What are you measuring? (conversion rate, revenue)
2. **Determine sample size**: Use power analysis
3. **Randomize**: Split users into A and B groups
4. **Run experiment**: Collect data for both groups
5. **Analyze**: Compare metrics, calculate p-value
6. **Decide**: Is the difference statistically significant?

### Key Concepts

**Statistical Significance**: Is the difference real or due to chance?
**Practical Significance**: Is the difference meaningful for business?

```python
# A/B test example
conversions_a = 120  # out of 1000
conversions_b = 145  # out of 1000

# Use chi-square or proportion z-test
from scipy.stats import chi2_contingency

table = [[120, 880], [145, 855]]
chi2, p_value, dof, expected = chi2_contingency(table)

if p_value < 0.05:
    print("Statistically significant difference")
```

### Common Pitfalls
- **Peeking**: Checking results before reaching sample size
- **Multiple testing**: Running many tests increases false positives
- **Novelty effect**: New features may have temporary boost
- **Selection bias**: Non-random assignment to groups

---

## Correlation

### Pearson Correlation (r)
- Measures linear relationship
- Range: -1 to +1
- 0 = no linear relationship

```python
import numpy as np

np.corrcoef(x, y)[0, 1]

# Or with scipy
from scipy.stats import pearsonr
r, p_value = pearsonr(x, y)
```

### Interpreting Correlation

| r Value | Strength |
|---------|----------|
| 0.0 - 0.3 | Weak |
| 0.3 - 0.7 | Moderate |
| 0.7 - 1.0 | Strong |

### Key Points

> **Correlation ≠ Causation**

- Ice cream sales correlate with drownings (both caused by summer)
- Correlation can be coincidental
- Need controlled experiments to establish causation

---

## Sampling

### Key Concepts

**Population**: All individuals of interest
**Sample**: Subset we actually measure
**Sampling Bias**: When sample doesn't represent population

### Sampling Methods

| Method | Description |
|--------|-------------|
| **Simple Random** | Each individual has equal chance |
| **Stratified** | Divide into groups, sample from each |
| **Cluster** | Divide into clusters, randomly select clusters |
| **Systematic** | Every nth individual |

### Central Limit Theorem

> "The distribution of sample means approaches normal
> as sample size increases, regardless of population distribution."

- Sample size n ≥ 30 is often sufficient
- Enables use of normal distribution for inference

---

## Interview Questions

1. **Explain p-value in simple terms**
   > "If nothing is happening (null hypothesis true), how surprised
   > would we be to see this result? Low p-value = very surprised
   > = probably something is happening."

2. **Type I vs Type II error?**
   > "Type I: false alarm (detect effect that isn't there).
   > Type II: miss (fail to detect effect that exists)."

3. **When use median vs mean?**
   > "Median for skewed data or when outliers present.
   > Mean for symmetric data without extreme values."

4. **How detect outliers?**
   > "IQR method (below Q1-1.5×IQR or above Q3+1.5×IQR),
   > or z-score (>3 standard deviations from mean)."

5. **Explain A/B testing**
   > "Controlled experiment: randomly split users, show different
   > versions, measure key metric, use statistics to determine
   > if difference is significant or just random noise."

---

*Last updated: February 2026*
