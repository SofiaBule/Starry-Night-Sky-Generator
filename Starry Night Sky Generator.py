import matplotlib.pyplot as plt
import numpy as np

def draw_starry_sky():
    x = np.random.rand(100)
    y = np.random.rand(100)
    colors = np.random.rand(100)
    sizes = 1000 * np.random.rand(100)

    plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)
    plt.title("Starry Night Sky")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.show()

draw_starry_sky()
