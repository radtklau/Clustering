import numpy as np

class KMeansClusterer:
    def __init__(self, k, data):
        self.k = k
        self.data = data
        
    def prepare_data(self):
        d = np.empty((len(self.data), len(self.data.columns) + 1))
        for i in range(len(self.data)):
            row = self.data.iloc[i].values
            row = np.concatenate((row, np.array([None])))
            d[i] = row
        
        self.data = d
        
        
    def init_centroids(self):
        pass
        
            
        
    
    