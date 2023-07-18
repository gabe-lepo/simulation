import tkinter as tk
from node import Node

from config import *

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
    
    node_blue.move()
    node_red.move()
    node_gray.move()
    node_white.move()

    window.after(REFRESH_MS, movement_loop)

canvas.bind("<Configure>", draw_grid)
movement_loop()
window.mainloop()