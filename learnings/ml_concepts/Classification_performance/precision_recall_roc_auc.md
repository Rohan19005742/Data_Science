# Techniques for measuring the performance of classification algorithms.

- Commonly used metrics include Accuracy, Precision, Recall, Specificity, F1 Score, ROC Curve, AUC, and Log Loss.

## Accuracy 

- correct predicitons over total predictions
- not useful when there is a class imbalance

## Precision

- TP / (TP+FP)
- of all the instances predicted as positive, how many were actually correct?
- use when there is a high cost of false positive (convicting someone)

## Recall

- TP / (TP + FN)
- of all the positive instances, how many did we correctly predict.
- use when there is a high cost of false negative (disease prediction)

## Specificity (True Negative Rate)

- TN / (TN + FP)
- how much of the negative cases did we actually get correct
- use when it is important to find negative cases (e.g., confirming healthy patients).

## F1

- 2 * Precision * recall / (precision + recall)
- use when precesion and recall are equally important


## ROC

- A curve that plots TP rate and FP rate
- Evaluates model performance across different classification thresholds.
- The best point is the point closes to the top left (high TPR, low FPR).


## AUC

- Measures the area under the ROC curve.
- Interpretation:
    - 1.0 → Perfect classifier
    - 0.5 → Random guessing
- Advantage:
    - Threshold-independent and works well with imbalanced data.

## Log loss (for prob classifiers)

- Measures the error between predicted probabilities and actual labels
- Penalizes confident but wrong predictions
- Lower values indicate better performance
- makes model to be not only accurate but confident in their predictions.

