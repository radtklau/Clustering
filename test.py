from data_generator import DataGenerator
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    data_gen = DataGenerator(500, 2, 10)
    data_gen.gen_data()
    data = data_gen.get_data()

    plt.scatter(data[0], data[1])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Scatter Plot')

    # Show the plot
    plt.show()