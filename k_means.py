import numpy as np
import math

class KMeansClusterer:
    def __init__(self, k, data, centroids=None):
        self.k = k
        self.data = data
        self.centroids = centroids
        
    def prepare_data(self):
        d = np.empty((len(self.data), len(self.data.columns) + 1))
        for i in range(len(self.data)):
            row = self.data.iloc[i].values
            row = np.concatenate((row, np.array([None])))
            d[i] = row
        
        self.data = d
        
        self.centroids = self.init_centroids()
        
    def init_centroids(self):
        max_x = np.max(self.data[:,0])
        min_x = np.min(self.data[:,0])
        max_y = np.max(self.data[:,1])
        min_y = np.min(self.data[:,1])
        
        centroids = np.empty((self.k, 2))

        for i in range(self.k):
            x_val = np.random.uniform(min_x, max_x)
            y_val = np.random.uniform(min_y, max_y)
            centroid = np.array([x_val, y_val])
            centroids[i] = centroid
        
        return centroids
    
    def calc_dist(self, a: tuple, b: tuple):
        x1, y1 = a
        x2, y2 = b
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance
        
            
        
    
    