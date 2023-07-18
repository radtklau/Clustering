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
    
    def calc_closest_centroid(self):
        for point in self.data:
            min_dist = 100000000
            closest_centroid = 0
            for label, centroid in enumerate(self.centroids):
                a = (point[0], point[1])
                b = (centroid[0], centroid[1])
                dist = self.calc_dist(a, b)
                if dist < min_dist:
                    closest_centroid = label
                    min_dist = dist
            point[2] = closest_centroid
                
    def update_centroids(self):
        aux_array = []
        for _ in range(self.k): #add one array for each centroid
            aux_array.append([0, 0, 1]) #x values, y values, count to calc mean
            
        for point in self.data:
            aux_array[int(point[2])][0] += point[0]
            aux_array[int(point[2])][1] += point[1]
            aux_array[int(point[2])][2] += 1
        
        for i, centroid in enumerate(aux_array):
            new_x = centroid[0] / centroid[2]
            new_y = centroid[1] / centroid[2]
            self.centroids[i] = np.array([new_x, new_y])
            
    def kmeans(self):
        self.prepare_data()
        for i in range(100):
            self.calc_closest_centroid()
            self.update_centroids()
            
    def get_data(self):
        return self.data
        
                
            
                
        
            
        
    
    