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
node_gray = Node(LIST[2]["NAME"], LIST[2]["SIZE"], LIST[2]["X_POS"], LIST[2]["Y_POS"])
node_white = Node(LIST[3]["NAME"], LIST[3]["SIZE"], LIST[3]["X_POS"], LIST[3]["Y_POS"])

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