# SMOTE (Synthetic Minority Over-sampling Technique)

- This technique is used to produce synthetic samples for minority classes.
- For fraud detection for example, there are many cases when there is no fraud, however only a small percentage that are fraud. This could lead to a class imbalance bias in the model. To improve the model's performance on minority class, we use the SMOTE technqique to generate synthetic samples of minority class.
- It mainly improves Recall and F1.
- SMOTE should be applied only to the training data, after the train/test split, to avoid data leakage. if done before, the test data might be linked to train data, causing leakage.

## How it creates new samples

- The idea is to balance the classes. (Have same number of samples for both classes)
    - This might not be sutible in some cases and could lead to overfitting.

1) It chooses a random sample from the minority class and then chooses one of its k nearest neighbours.
2) choose a random point between the samples and the random point is the new sample.
3) repeat until you have desired number of samples.

## Overfiiting

- SMOTE can cause overfitting when the minority class is noisy or when there is high-dimensional data.
- SMOTE performs poorly fro highly skewed or sparese data.

## Works best with numerical features
- it uses knn and therefor needs a notion of distance. 
- SMOTE performs poorly for categorical variables unless they have been encoded.