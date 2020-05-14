from cells import ca, initialize
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.animation import FuncAnimation
import numpy as np

cells_width = 100
cells_height = 100
# initialize cells array with a starting state/initial matrix
# arguments include diag, border, cross, rand
cells_arr = initialize(cells_width, cells_height, 'cross')


def update_cells():

    # update cells
    for i in range(cells_width):
        for j in range(cells_height):

            i_minus = i - 1
            if i_minus < 0:
                i_minus = cells_width - 1

            i_plus = i + 1
            if i_plus > cells_width - 1:
                i_plus = 0

            j_minus = j - 1
            if j_minus < 0:
                j_minus = cells_height - 1

            j_plus = j + 1
            if j_plus > cells_height - 1:
                j_plus = 0

            topLeft = cells_arr[i_minus][j_minus].current_state
            topCenter = cells_arr[i][j_minus].current_state
            topRight = cells_arr[i_plus][j_minus].current_state
            midLeft = cells_arr[i_minus][j].current_state
            midRight = cells_arr[i_plus][j].current_state
            bottomLeft = cells_arr[i_minus][j_plus].current_state
            bottomCenter = cells_arr[i][j_plus].current_state
            bottomRight = cells_arr[i_plus][j_plus].current_state

            sum = int(topLeft + topCenter + topRight + midLeft \
                      + midRight + bottomLeft + bottomCenter + bottomRight)

            cells_arr[i][j].neighbors = sum
            # pick a rule from the cells class
            ca.life(cells_arr[i][j])

    for i in range(cells_width):
        for j in range(cells_height):
            cells_arr[i][j].update_states()
            # matr[i][j] = cells_arr[i][j].current_state

    current_state_mat = [[cells_arr[i][j].current_state for i in range(cells_width)] for j in range(cells_height)]

    return current_state_mat


def animate(itr):
    ax.cla()
    arr = update_cells()
    ax.set_xticks([])
    ax.set_yticks([])
    ax.imshow(arr, cmap=cm.jet, interpolation='nearest')


fig, ax = plt.subplots()
animation = FuncAnimation(fig, animate, 50)
#plt.show()

animation.save('./CA.gif', writer='PillowWriter')
