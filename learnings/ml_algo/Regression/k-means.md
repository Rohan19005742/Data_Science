# K-means Clustering

K-means is an **unsupervised clustering algorithm** that groups data points into **k clusters**, where each data point belongs to the cluster with the nearest mean.

## Steps

1. Randomly select **k data points** as initial cluster centers (centroids).
2. Calculate the distance between each data point and each centroid (commonly Euclidean distance).
3. **Assign** each data point to the nearest centroid.
4. **Recalculate** each centroid as the mean of the data points assigned to it.
5. Repeat steps 2–4 until:
   - the cluster assignments no longer change, or  
   - a maximum number of iterations is reached.

## Notes

- The initial choice of centroids matters; different initializations can lead to different final clusters.
- Methods like **k-means++** are often used to choose better initial centroids.

## Advantages

- Simple and easy to understand.
- Computationally efficient for small to medium-sized datasets.
- Used for **image compression** by reducing color precision.
- Helps find **similar items** (e.g., documents, users).
- Can help identify **outliers**.

## Disadvantages

- Sensitive to the choice of **k** (number of clusters).
- Sensitive to initial centroid placement.
- Affected by **outliers**, which can distort cluster centers.
- Assumes clusters are roughly **spherical and equally sized**. (K-means tries to minimize average distance to centroids, which biases it toward equal-sized clusters.) however in reality, not every cluster is of equal size.
- Can be slow for very large datasets.
