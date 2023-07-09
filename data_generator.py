import pandas as pd
import numpy as np

class DataGenerator:
    def __init__(self, n, dim, dtype):
        self.data = pd.DataFrame()
        self.n = n
        self.dim = dim
        self.dtype = dtype

    def gen_data(self):
        shape = (self.n, self.dim)
        np_data = np.random.rand(shape)
        self.data = pd.DataFrame(np_data)