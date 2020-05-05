from tkinter import *
from PIL import Image, ImageDraw
from cells import ca, initialize

win_width = 500
win_height = 500
scl = 5
cells_width = int(win_width/scl)
cells_height = int(win_height/scl)
print(cells_height)

image1 = Image.new("RGB", (win_width, win_height), (255, 255, 255))
draw = ImageDraw.Draw(image1)
cells_arr = initialize(cells_width, cells_height, 'diag')


def update():

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
            ca.maze(cells_arr[i][j])

    # draw frames canvas cuts it off so starting at 2
    for i in range(0, win_width, scl):
        for j in range(0, win_height, scl):

            if cells_arr[int(i / scl)][int(j / scl)].current_state == 1:
                canvas.create_rectangle(i, j, i + scl, j + scl, fill='orange', outline='')
                draw.rectangle((i, j, i + scl, j + scl), fill='orange', outline=None)
            else:
                canvas.create_rectangle(i, j, i + scl, j + scl, fill='blue', outline='')
                draw.rectangle((i, j, i + scl, j + scl), fill='blue', outline=None)

            cells_arr[int(i/scl)][int(j/scl)].current_state = cells_arr[int(i/scl)][int(j/scl)].next_state

    my_window.after(40, update)
    filename = "my_CA.jpg"
    image1.save(filename)


my_window = Tk()
canvas = Canvas(my_window, width=win_width, height=win_height, background='black')
canvas.pack()

my_window.after(40, update)
my_window.mainloop()
