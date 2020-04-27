from tkinter import *
import numpy as np
from PIL import Image, ImageDraw
from rules import start_state


class Cells(object):
    def __init__(self):
        self.current_state = []
        self.neighbors = 0
        self.next_state = []


ca = Cells
width = 500
height = 500
scl = 5

image1 = Image.new("RGB", (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image1)

ca.current_state = start_state(width, height, scl, 'cross')
print(ca.current_state)
# ca.next_state = np.zeros((int(width / scl), int(height / scl)))
ca.neighbors = 0


def update():

    ca.next_state = np.zeros((int(width / scl), int(height / scl)))
    for i in range(0, width, scl):
        for j in range(0, height, scl):
            # ca.neighbors =
            # wrap edges around corresponding axis
            i_minus = int(i / scl) - 1
            if i_minus < 0:
                i_minus = int(width / scl) - 1

            i_plus = int(i / scl) + 1
            if i_plus > int(width / scl) - 1:
                i_plus = 0

            j_minus = int(j / scl) - 1
            if j_minus < 0:
                j_minus = int(height / scl) - 1

            j_plus = int(j / scl) + 1
            if j_plus == int(height / scl):
                j_plus = 0

            topLeft = ca.current_state[i_minus][j_minus]
            origin = ca.current_state[int(i/scl)][int(j/scl)]
            topCenter = ca.current_state[int(i / scl)][j_minus]
            topRight = ca.current_state[i_plus][j_minus]
            midLeft = ca.current_state[i_minus][int(j / scl)]
            midRight = ca.current_state[i_plus][int(j / scl)]
            bottomLeft = ca.current_state[i_minus][j_plus]
            bottomCenter = ca.current_state[int(i / scl)][j_plus]
            bottomRight = ca.current_state[i_plus][j_plus]

            ca.neighbors = int(topLeft + topCenter + topRight + midLeft \
                           + midRight + bottomLeft + bottomCenter + bottomRight)
     
            # dope quilt plaid pattern start with cross
            if ca.current_state[int(i/scl)][int(j/scl)] == 1 and (ca.neighbors == 1 or ca.neighbors == 2 or ca.neighbors == 5):
                ca.next_state[int(i/scl)][int(j/scl)] = 1
            elif ca.current_state[int(i/scl)][int(j/scl)] == 0 and (ca.neighbors == 2 or ca.neighbors == 6):
                ca.next_state[int(i/scl)][int(j/scl)] = 1
#            else:
#                ca.next_state[int(i/scl)][int(j/scl)] = ca.current_state[int(i/scl)][int(j/scl)]

            # game of life good stuff with cross or random
            # if ca.current_state[int(i/scl)][int(j/scl)] == 0 and ca.neighbors == 3:
            #     ca.next_state[int(i/scl)][int(j/scl)] = 1
            # elif ca.current_state[int(i/scl)][int(j/scl)] == 1 and (ca.neighbors < 2 or ca.neighbors > 3):
            #     ca.next_state[int(i/scl)][int(j/scl)] = 0
            # else:
            #     ca.next_state[int(i/scl)][int(j/scl)] = ca.current_state[int(i/scl)][int(j/scl)]


            if ca.current_state[int(i / scl)][int(j / scl)] == 1:
                canvas.create_rectangle(i, j, i + scl, j + scl, fill='red', outline='')
                draw.rectangle((i, j, i + scl, j + scl), fill=(153,0,17), outline=None)
            else:
                canvas.create_rectangle(i, j, i + scl, j + scl, fill='white', outline='')
                draw.rectangle((i, j, i + scl, j + scl), fill=(252, 246, 245), outline=None)

    # keyboard.wait("p")

    my_window.after(100, update)
    filename = "my_CA.jpg"
    image1.save(filename)
    ca.current_state = ca.next_state


my_window = Tk()
canvas = Canvas(my_window, width=width, height=height, background='black')
canvas.pack()

# update()
my_window.after(100, update)
my_window.mainloop()
