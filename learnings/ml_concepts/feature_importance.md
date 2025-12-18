# Feature importance

## Model based
- Decision trees

## For Numerical Features
Pearson correlation (linear)
Spearman correlation (non-linear)

## For categorical
- gini index
- information gain (how much entropy remains after split) ( most affected by large sample size)
- entropy 

## Correlation

- Covariance measures how two features vary together.
- correlation = covariance / (s.dx * s.dy)
- correlation measures the strength and direction of a relationship between two variables

## Multicollinearity 
- occurs when two or more independent features (predictors) in a dataset are highly correlated with each other.
- This means they provide redundant or overlapping information to the model.
- it is difficult to identify values for coefficients.

- Mainly impacts regression models (linear/logistic), less problematic for tree models.
- Issues caused:
- Coefficient estimates become unstable
- Hard to determine which feature truly affects the target

## How to detect multicollinearity?
1. Correlation Matrix / Heatmap
Look for correlation > |0.8| or |0.9|
2. Variance Inflation Factor (VIF)
VIF > 5 or 10 indicates problems

## How to deal with it
- Regularisation
- Remove one of the correlated features
- combine the features (PCA)
