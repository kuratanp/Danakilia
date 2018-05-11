#!/usr/bin/env python

"""
mlclusters library to fit the KMean model, evaluate clustering performance and create a visual plot.
"""

class Mlclusters:
    
    def __init__(self, ddrad, n_cluster):
        
        self.ddrad = ddrad
        self.n_cluster = n_cluster
        self.kmeans_labels = self._fit_kmeans
        self.evaluate_performance = self._evaluate_performance
        self.plot_kmeans = self._plot_kmeans
         

    # private functions
    def _fit_kmeans(self):
        """
        Fit a clustering method Kmeans
        """  
        kmeans_model = KMeans(self.n_cluster, random_state=1).fit(self.ddrad)
        labels = kmeans_model.labels_
        return labels
    
        
    def _evaluate_performance(self):
        """
        Evaluate clustering performace using Silhouette Coefficient and Calinski-Harabaz Index
        """  
        s_score = metrics.silhouette_score((self.ddrad), self.kmeans_labels(), metric='euclidean')
        ch_score = metrics.calinski_harabaz_score((self.ddrad), self.kmeans_labels())

        return pd.Series(
            {"Silhouette Coefficient": s_score,
             "Calinski-Harabaz Index": ch_score,
            })
    
    
    def _plot_kmeans(self):
        """
        Creating a visual plot
        """  

        # Compute clustering with KMeans

        k_means = KMeans(self.n_cluster, init='k-means++', n_init=10)
        k_means.fit(self.ddrad)

        # The following bandwidth can be automatically detected using

        labels = k_means.labels_
        cluster_centers = k_means.cluster_centers_

        labels_unique = np.unique(labels)
        n_clusters_ = len(labels_unique)

        # Plot result
        plt.figure(1)
        plt.clf() # Clear the current figure.

        colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
        for k, col in zip(range(n_clusters_), colors):
            my_members = labels == k
            cluster_center = cluster_centers[k]
            plt.plot(self.ddrad[my_members, 0], self.ddrad[my_members, 1], col + '.')
            plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=14)
        plt.title('Estimated number of clusters: %d' % n_clusters_)
        plt.show()   
    
       