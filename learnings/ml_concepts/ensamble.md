# Ensamble

What? - Ensamble is a method that uses many smaller models instead of one.

Why? - Each model makes its own mistakes and combining them will average out the individual mistakes.

Methods - Bagging, Boosting and Stacking.

## Bagging

- Models are trained independently on differennt subsets of the training data. Their results are then combined—usually by averaging (for regression) or voting (for classification). This helps reduce variance and prevents overfitting 

but can lead to underfitting if the smaller models lose the complexity of the big model.

- Use when the model is prone to overfitting.

### Bagging Algo

1) Bootstap sampling: Divide the training data into N subsets randomnly with replacment (subsets can have overlapping data).

2) Base Model Training: For each subset we train a base model independently.

3) Prediction: vote or average based on ML method.

4) Out-of-Bag (OOB) Evaluation: Some samples are excluded from training subset during the bootstap. These samples then can be used to evalute the model without the need for cross-validation.

## Boosting

- Models are trained one after the other (sequentially). Each new model focuses on improving on the mistakes of the previous model. The final prediction is a weighted combination of all models, which helps reduce bias and improve accuracy.

but can lead to overfitting.

### Boosting Algo
Most common is AdaBoost

- Initialize Model Weights: Begin with a single model and assign equal weights to all training examples.

- Weight Adjustment: Assign weights to training datapoints. Missclassifed examples are weighted higher. A new model then learns from this. Keep doing this until all samples are correctly classified.

## Stacking

- Multiple different models (of different types) are trained and their predictions are used as inputs to a final model called meta-model. The meta-model learns how to best combine the predictions of the base models


![](https://media.geeksforgeeks.org/wp-content/uploads/20250911170744782776/training_dataset.webp)




