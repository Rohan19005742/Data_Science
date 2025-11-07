# Data Cleaning
- This is the second step in the data science pipeline
- In this step we identify and remove, duplicate, missing and irrelevant data.
- The goal of Data cleaning is to ensure the data is accurate, consistent and free of errors.

### Disadvantages
1. Time-consuming
1. Error-prone: It can result in loss of important information.
1. Cost and resource-intensive
1. Overfitting: Data cleaning can contribute to overfitting by removing too much data.


## 1. Check for Duplicate rows
- drop any duplicate rows

## 2. Find and drop any irrelevant columns
- There are multiple ways of doing this.
- we can remove based on:
    - Low correlation with the target feature
    - Low variance threshold
    - high correlation with another feature
    - missing values or text-heavy columns.
    - low importance using Random Forest
    - Manually seeing what features might not be relevant

## 3. Find and address Missing values
- Calculate Missing Values as Percentage
- Then decide wether to drop or impute missing data.

## 4. Find and address Outliers
- use box plot or
- use z score, where outlier if |z| > 3 (use when data is approx normal)
- IQR, A very popular and robust method.
    - Outlier if x<Q1−1.5 * IQR or x>Q3+1.5 * IQR
- visulise the data and manually see outliers
- Mahalanobis Distance (for multivariate numeric data)
    - Measures how far a point is from the center considering correlations.

## 5. recalc outlier bounds and remove outliers from the updated data.
- due to previous outliers, it may have allowed other outliers to sneek into the normal dataset, we need to get rid of them.

## 6. Data formatting
- normalistion: rescale the data to be in a specific range so it does not dominate other features because it has a larger range.
    - use when Distribution is Unknown or Non-Gaussian or when using Distance-Based Algorithms: knn, k-means, svm ...
    - min-max scaling normalisation:
        - (x - x_min) / (x_max - x_min)
        - put data into range 0-1
- standardistion: centers data around the mean
    - Z score: how many S.D is the data point away from the mean.
- data type conversion
    - data might be in the wrong format
- handling inconsistent data e.g. units
