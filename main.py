import tkinter as tk
import csv
from node import Node

from config import *
from node_list import LIST

window = tk.Tk()
window.title('Simulation')

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

node_blue = Node(LIST[0]["NAME"], LIST[0]["SIZE"], LIST[0]["X_POS"], LIST[0]["Y_POS"])
node_red = Node(LIST[1]["NAME"], LIST[1]["SIZE"], LIST[1]["X_POS"], LIST[1]["Y_POS"])
blue_x_positions = []
blue_y_positions = []
red_x_positions = []
red_y_positions = []

def on_close():
    window.destroy()
    print("Window destroyed")

    with open("blue_position_record.csv", "w", newline='') as file:
        writer = csv.writer(file)
        for _ in range(len(blue_x_positions)):
            writer.writerow([_, blue_x_positions[_], blue_y_positions[_]])
        blue_x_positions.clear()
        blue_y_positions.clear()
    with open("red_position_record.csv", "w", newline='') as file:
        writer = csv.writer(file)
        for _ in range(len(red_x_positions)):
            writer.writerow([_, red_x_positions[_], red_y_positions[_]])
        red_x_positions.clear()
        red_y_positions.clear()

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
    blue_x_positions.append(node_blue.x_pos)
    blue_y_positions.append(node_blue.y_pos)
    node_red.move("random")
    red_x_positions.append(node_red.x_pos)
    red_y_positions.append(node_red.y_pos)

    window.after(REFRESH_MS, movement_loop)

canvas.bind("<Configure>", draw_grid)
movement_loop()

window.protocol("WM_DELETE_WINDOW", on_close)
window.mainloop()