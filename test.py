from data_generator import DataGenerator
import pandas as pd
import matplotlib.pyplot as plt
from k_means import KMeansClusterer

if __name__ == "__main__":
    data_gen = DataGenerator(500, 2, 5)
    data_gen.gen_data()
    data = data_gen.get_data()

    clusterer = KMeansClusterer(3, data)
    clusterer.kmeans()
    

    plt.scatter(data[:, 0], data[:, 1], c=data[:, 2])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Scatter Plot')

    # Show the plot
    plt.show()
