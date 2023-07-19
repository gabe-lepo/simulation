import tkinter as tk
from node import Node

from config import *
from node_list import LIST

window = tk.Tk()
window.title('Simulation')

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

node_blue = Node(LIST[0]["NAME"], LIST[0]["SIZE"], LIST[0]["X_POS"], LIST[0]["Y_POS"])
node_red = Node(LIST[1]["NAME"], LIST[1]["SIZE"], LIST[1]["X_POS"], LIST[1]["Y_POS"])

def draw_grid(event=None):
    canvas.create_rectangle(0, 0, WIDTH / 2, HEIGHT, fill="blue", outline="")
    canvas.create_rectangle(WIDTH / 2, HEIGHT, WIDTH, 0, fill="red", outline="")

def movement_loop():
    canvas.delete("nodes")
    canvas.create_oval(node_blue.x_pos - node_blue.size, node_blue.y_pos - node_blue.size,
                       node_blue.x_pos + node_blue.size, node_blue.y_pos + node_blue.size,
                       fill="blue", tags="nodes")
    canvas.create_oval(node_red.x_pos - node_red.size, node_red.y_pos - node_red.size,
                       node_red.x_pos + node_red.size, node_red.y_pos + node_red.size,
                       fill="red", tags="nodes")
    
    node_blue.move("random")    
    node_red.move("random")

    window.after(REFRESH_MS, movement_loop)

canvas.bind("<Configure>", draw_grid)
movement_loop()
window.mainloop()