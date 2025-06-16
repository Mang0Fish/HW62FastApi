import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs, make_moons
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.model_selection import train_test_split


# create data
x1, _ = make_moons(n_samples=300, noise=0.05, random_state=0)
x2, _ = make_blobs(n_samples=300, centers=3, cluster_std=0.60, random_state=0)
# 1

plt.subplot(1, 2, 1)
plt.scatter(x1[:,0], x1[:,1])
plt.title("Moons Dataset")

plt.subplot(1, 2, 2)
plt.scatter(x2[:,0], x2[:,1], color='orange')
plt.title("Blobs Dataset")
plt.show()

# 2
#The moons is dbscan, which excels in finding special forms, like halfmoons here,
#The blobs is kmeans, which looks for distance from centroids, and finds blobs and clusters

modelDb = DBSCAN()

modelKmeans = KMeans(n_clusters= 3, random_state=0)
modelKmeans.fit(x2)
yKmeans = modelKmeans.predict(x2)
plt.scatter(x2[:, 0], x2[:, 1], c=yKmeans)
plt.show()

modelDb = DBSCAN(eps= 0.05, min_samples=5)
modelDb.fit(x1)
yDb = modelDb.labels_
plt.scatter(x1[:, 0], x1[:, 1], c=yDb)
plt.show()