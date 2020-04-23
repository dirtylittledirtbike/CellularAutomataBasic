from tkinter import *
import numpy as np
from PIL import Image, ImageDraw
from rules import start_state
#import keyboard


class Cell(object):
    def __init__(self):
        self.current_state = []
        self.neighbors = []
        self.next_state = []


ca = Cell
width = 600
height = 600
scl = 4

image1 = Image.new("RGB", (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image1)

def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 10)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value


def start_state(w, h, s, state):

    if state == 'pad' and int(w/s) % 3 == 0:
        x = int((w/s)/3)
        y = int(((w/s) - x)/2)
        ab = np.zeros((x, x), dtype=int)
        cd = np.pad(ab, int(y/2), pad_with, padder=1)
        ef = np.pad(cd, int(y/2), pad_with, padder = 0)
        return ef

    elif state == 'cross':
        aa = np.eye(int(w/s), dtype=int)
        bb = np.rot90(aa).copy()
        cc = np.array(aa + bb)
        return cc

    elif state == 'rand':
        return np.random.randint(0, 2, (int(w/s), int(h/s)))

    else:
        print('wrong dimensions')


ca.current_state = start_state(width, height, scl, 'cross')
ca.next_state = np.zeros((int(width / scl), int(height / scl)))
ca.neighbors = 0


def update():
    for i in range(0, width, scl):
        for j in range(0, height, scl):
            
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
            if j_plus > int(height / scl) - 1:
                j_plus = 0

            topLeft = ca.current_state[i_minus][j_minus]
            topCenter = ca.current_state[int(i / scl)][j_minus]
            topRight = ca.current_state[i_plus][j_minus]
            midLeft = ca.current_state[i_minus][int(j / scl)]
            midRight = ca.current_state[i_plus][int(j / scl)]
            bottomLeft = ca.current_state[i_minus][j_plus]
            bottomCenter = ca.current_state[int(i / scl)][j_plus]
            bottomRight = ca.current_state[i_plus][j_plus]

            ca.neighbors = topLeft + topCenter + topRight + midLeft + \
                           midRight + bottomLeft + bottomCenter + bottomRight

            if ca.current_state[int(i/scl)][int(j/scl)] == 1 and (ca.neighbors == 1 or ca.neighbors == 6 or ca.neighbors == 2):
                ca.next_state[int(i/scl)][int(j/scl)] = 0
            elif ca.current_state[int(i/scl)][int(j/scl)] == 0 and (ca.neighbors < 3 or ca.neighbors == 7):
                ca.next_state[int(i/scl)][int(j/scl)] = 1

            if ca.current_state[int(i / scl)][int(j / scl)] == 1:
                canvas.create_rectangle(i, j, i + scl, j + scl, fill='orange', outline='')
                draw.rectangle((i, j, i + scl, j + scl), fill='orange', outline=None)
            else:
                canvas.create_rectangle(i, j, i + scl, j + scl, fill='blue', outline='')
                draw.rectangle((i, j, i + scl, j + scl), fill='blue', outline=None)

            ca.current_state[int(i / scl)][int(j / scl)] = ca.next_state[int(i / scl)][int(j / scl)]

    # keyboard.wait("p")
    my_window.after(500, update)
    filename = "my_CA.jpg"
    image1.save(filename)


my_window = Tk()
canvas = Canvas(my_window, width=width, height=height, background='black')
canvas.pack()

my_window.after(500, update)
my_window.mainloop()
