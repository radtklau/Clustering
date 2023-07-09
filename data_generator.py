import pandas as pd
import numpy as np

class DataGenerator:
    def __init__(self, n=None, dim=None, num_clusters=1):
        self.data = pd.DataFrame()
        self.n = n
        self.dim = dim
        self.num_clusters = num_clusters

    def gen_data(self):
        points_per_cluster = self.n // self.num_clusters
        np_data = np.empty((0, 2))
        for i in range(self.num_clusters):
            shape = (points_per_cluster, self.dim)
            mean_x = np.random.uniform(0, 100)  # Mean for the x dimension
            mean_y = np.random.uniform(0, 100)  # Mean for the y dimension
            cluster = np.random.normal([mean_x, mean_y], np.random.uniform(1, 20), size=shape)
            np_data = np.concatenate((np_data, cluster), axis=0)

        self.data = pd.DataFrame(np_data)

    def get_data(self):
        return self.data
    
    def set_params(self, n, dim, num_clusters):
        self.n = n
        self.dim = dim
        self.num_clusters = num_clusters