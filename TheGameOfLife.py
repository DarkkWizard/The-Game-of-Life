import matplotlib; matplotlib.use("TkAgg")
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animate
import random

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], 'yx')


def create_grid(size):
    f = np.zeros((size, size))
    f = f.astype(int)
    return f


def survival(x, y, array):
    num_neighbours = np.sum(array[x - 1: x + 2, y - 1: y + 2]) - array[x, y]
    if array[x, y] and not 2 <= num_neighbours <= 3:
        return 0
    elif num_neighbours == 3:
        return 1
    return array[x, y]


def new_grid(array):
    global grid
    return_grid = np.copy(array)
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            return_grid[i, j] = survival(i, j, array)
    grid = return_grid
    return return_grid


def rand_data():
    global grid
    for i in range(int(input_size**2 / 2)):
        grid[int(random.randint(0, input_size - 1)), int(random.randint(0, input_size - 1))] = 1


def defined_data(inp):
    global grid
    grid = input("input wanted grid: ")


def initialize():
    global n_generations
    global input_size
    global grid
    n_generations = int(input('How many generations? : '))
    input_size = int(input('How large should the grid be?: '))
    defined = bool(input("Defined Data? (True or False): "))
    grid = create_grid(input_size)
    if defined == True:
        defined_data(input_size)
    else:
        rand_data()


# setting up
initialize()
plt.style.use('_mpl-gallery-nogrid')


ims = []
for thangs in range(n_generations):
    ims.append((plt.imshow(grid),))
    universe = new_grid(grid)

im_ani = animate.ArtistAnimation(
    fig, ims, repeat_delay=20, blit=True
)

plt.show()
