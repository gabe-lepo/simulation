import tkinter as tk
import csv
from node import Node

from config import *
from node_list import LIST

window = tk.Tk()
window.title('Simulation')

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

node_blue = Node(LIST[0]["ATTITUDE"], LIST[0]["SIZE"], LIST[0]["X_POS"], LIST[0]["Y_POS"])
node_red = Node(LIST[1]["ATTITUDE"], LIST[1]["SIZE"], LIST[1]["X_POS"], LIST[1]["Y_POS"])
blue_x_positions = []
blue_y_positions = []
red_x_positions = []
red_y_positions = []
distance_to = []

def cleanup():
    window.destroy()

    with open("./records/blue_position_record.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Iteration', 'x_pos', 'y_pos'])
        for _ in range(len(blue_x_positions)):
            writer.writerow([_, blue_x_positions[_], blue_y_positions[_]])
        blue_x_positions.clear()
        blue_y_positions.clear()
    
    with open("./records/red_position_record.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Iteration', 'x_pos', 'y_pos'])
        for _ in range(len(red_x_positions)):
            writer.writerow([_, red_x_positions[_], red_y_positions[_]])
        red_x_positions.clear()
        red_y_positions.clear()

    with open("./records/distance_records.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Iteration', 'Distance', 'Difference from last'])
        for _ in range(len(distance_to)):
            writer.writerow([_, distance_to[_], distance_to[_] - distance_to[_-1]])
        distance_to.clear()
    
    print("Program exited successfully")

def draw_grid(event=None):
    canvas.create_rectangle(0, 0, WIDTH / 2, HEIGHT, fill="blue", outline="")
    canvas.create_rectangle(WIDTH / 2, HEIGHT, WIDTH, 0, fill="red", outline="")

def movement_loop():
    canvas.delete("nodes")
    canvas.delete("size")
    if node_blue.size > 0:
        canvas.create_oval(node_blue.x_pos - node_blue.size, node_blue.y_pos - node_blue.size,
                        node_blue.x_pos + node_blue.size, node_blue.y_pos + node_blue.size,
                        fill="blue", tags="nodes")
        canvas.create_text(node_blue.x_pos, node_blue.y_pos, text=f"{node_blue.size}", fill="black", tags="size")
    if node_red.size > 0:
        canvas.create_oval(node_red.x_pos - node_red.size, node_red.y_pos - node_red.size,
                        node_red.x_pos + node_red.size, node_red.y_pos + node_red.size,
                        fill="red", tags="nodes")
        canvas.create_text(node_red.x_pos, node_red.y_pos, text=f"{node_red.size}", fill="black", tags="size")

    node_blue.attitude = "patrol"
    node_red.attitude = "patrol"
    
    node_blue.move(node_red)
    node_red.move(node_blue)
    
    distance_to.append(node_blue.distance_to(node_red))
    blue_x_positions.append(node_blue.x_pos)
    blue_y_positions.append(node_blue.y_pos)
    red_x_positions.append(node_red.x_pos)
    red_y_positions.append(node_red.y_pos)

    window.after(REFRESH_MS, movement_loop)

canvas.bind("<Configure>", draw_grid)
movement_loop()

window.protocol("WM_DELETE_WINDOW", cleanup)
window.mainloop()