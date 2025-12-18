## Normalization 
- scales data to a fixed range (commonly 0–1).
- Best for distance-based or gradient-based models like KNN, K-Means, Neural Networks.
- More sensitive to outliers.

## Standardization 
- scales data using mean and standard deviation.
- Useful when features have different scales, especially if data is roughly normal.
- Works well for algorithms that assume Gaussian distribution or use distance. (regression, SVM, PCA, KMeans)
- Can be influenced by outliers.

1. Either works depending on model and distribution, but standardization is generally preferred unless the model specifically benefits from normalization (like KNN, NN).