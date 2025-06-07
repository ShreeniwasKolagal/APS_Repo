import random
import math

def kmeans(points, K, max_iters=100):
    """
    points: list of data points (tuples of floats)
    K: number of clusters
    Returns: (centroids, labels)—centroids as list of K points, labels as list of cluster indices per point.
    """
    # 1. Initialize centroids by selecting K random points
    centroids = random.sample(points, K)

    for _ in range(max_iters):
        # 2. Assign points to nearest centroid
        clusters = [[] for _ in range(K)]
        labels = []
        for p in points:
            dists = [math.dist(p, c) for c in centroids]
            idx = dists.index(min(dists))
            clusters[idx].append(p)
            labels.append(idx)

        # 3. Recompute centroids
        new_centroids = []
        for cluster in clusters:
            if not cluster:
                # reinitialize randomly if cluster is empty
                new_centroids.append(random.choice(points))
            else:
                # mean of cluster
                dim = len(cluster[0])
                mean = tuple(sum(p[i] for p in cluster) / len(cluster) for i in range(dim))
                new_centroids.append(mean)

        # 4. Check for convergence
        if all(math.isclose(math.dist(centroids[i], new_centroids[i]), 0.0) for i in range(K)):
            break
        centroids = new_centroids

    return centroids, labels


# Example:
data = [(1.0, 2.0), (1.5, 1.8), (5.0, 8.0), (8.0, 8.0), (1.0, 0.6), (9.0, 11.0)]
centroids, labels = kmeans(data, K=2)
print("Centroids:", centroids)
print("Labels:", labels)
