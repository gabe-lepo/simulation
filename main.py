import tkinter as tk
import random
from node import Node

MOVERANGE = 50
WIDTH = 1024
HEIGHT = 768
REFRESH_MS = 1

window = tk.Tk()
window.title('Simulation')

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

node_blue = Node("blue", 50, (1/4)*WIDTH, (1/4)*HEIGHT)
node_red = Node("red", 50, (3/4)*WIDTH, (1/4)*HEIGHT)
node_gray = Node("gray", 50, (1/4)*WIDTH, (3/4)*HEIGHT)
node_white = Node("white", 50, (3/4)*WIDTH, (3/4)*HEIGHT)

def draw_grid(event=None):
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

#    canvas.create_rectangle(0, 0, canvas_width, canvas_height,
#                            fill="red", outline="")
    canvas.create_rectangle(0, 0, canvas_width / 2, canvas_height / 2,
                            fill="blue", outline="")
    canvas.create_rectangle(canvas_width / 2, 0, canvas_width, canvas_height / 2,
                            fill="red", outline="")
    canvas.create_rectangle(0, canvas_height / 2, canvas_width / 2, canvas_height,
                            fill="gray", outline="")
    canvas.create_rectangle(canvas_width / 2, canvas_height / 2, canvas_width, canvas_height,
                            fill="white", outline="")

def movement_loop():
    canvas.delete("nodes")
    canvas.create_oval(node_blue.x_pos - node_blue.size, node_blue.y_pos - node_blue.size,
                       node_blue.x_pos + node_blue.size, node_blue.y_pos + node_blue.size,
                       fill="blue", tags="nodes")
    canvas.create_oval(node_red.x_pos - node_red.size, node_red.y_pos - node_red.size,
                       node_red.x_pos + node_red.size, node_red.y_pos + node_red.size,
                       fill="red", tags="nodes")
    canvas.create_oval(node_gray.x_pos - node_gray.size, node_gray.y_pos - node_gray.size,
                       node_gray.x_pos + node_gray.size, node_gray.y_pos + node_gray.size,
                       fill="gray", tags="nodes")
    canvas.create_oval(node_white.x_pos - node_white.size, node_white.y_pos - node_white.size,
                       node_white.x_pos + node_white.size, node_white.y_pos + node_white.size,
                       fill="white", outline="black", tags="nodes")
    
    blue_top = node_blue.y_pos - node_blue.size
    blue_right = node_blue.x_pos + node_blue.size
    blue_bottom = node_blue.y_pos + node_blue.size
    blue_left = node_blue.x_pos - node_blue.size
    
    red_top = node_red.y_pos - node_red.size
    red_right = node_red.x_pos + node_red.size
    red_bottom = node_red.y_pos + node_red.size
    red_left = node_red.x_pos - node_red.size

    gray_top = node_gray.y_pos - node_gray.size
    gray_right = node_gray.x_pos + node_gray.size
    gray_bottom = node_gray.y_pos + node_gray.size
    gray_left = node_gray.x_pos - node_gray.size

    white_top = node_white.y_pos - node_white.size
    white_right = node_white.x_pos + node_white.size
    white_bottom = node_white.y_pos + node_white.size
    white_left = node_white.x_pos - node_white.size

    if blue_top <= 0:
        node_blue.move(0, MOVERANGE)
    elif blue_bottom >= HEIGHT:
        node_blue.move(0, -MOVERANGE)
    elif blue_right >= WIDTH:
        node_blue.move(-MOVERANGE, 0)
    elif blue_left <= 0:
        node_blue.move(MOVERANGE, 0)
    else:
        node_blue.move(random.randint(-MOVERANGE, MOVERANGE), random.randint(-MOVERANGE, MOVERANGE))

    if red_top <= 0:
        node_red.move(0, MOVERANGE)
    elif red_bottom >= HEIGHT:
        node_red.move(0, -MOVERANGE)
    elif red_right >= WIDTH:
        node_red.move(-MOVERANGE, 0)
    elif red_left <= 0:
        node_red.move(MOVERANGE, 0)
    else:
        node_red.move(random.randint(-MOVERANGE, MOVERANGE), random.randint(-MOVERANGE, MOVERANGE))

    if gray_top <= 0:
        node_gray.move(0, MOVERANGE)
    elif gray_bottom >= HEIGHT:
        node_gray.move(0, -MOVERANGE)
    elif gray_right >= WIDTH:
        node_gray.move(-MOVERANGE, 0)
    elif gray_left <= 0:
        node_gray.move(MOVERANGE, 0)
    else:
        node_gray.move(random.randint(-MOVERANGE, MOVERANGE), random.randint(-MOVERANGE, MOVERANGE))

    if white_top <= 0:
        node_white.move(0, MOVERANGE)
    elif white_bottom >= HEIGHT:
        node_white.move(0, -MOVERANGE)
    elif white_right >= WIDTH:
        node_white.move(-MOVERANGE, 0)
    elif white_left <= 0:
        node_white.move(MOVERANGE, 0)
    else:
        node_white.move(random.randint(-MOVERANGE, MOVERANGE), random.randint(-MOVERANGE, MOVERANGE))

    window.after(REFRESH_MS, movement_loop)

canvas.bind("<Configure>", draw_grid)
movement_loop()
window.mainloop()