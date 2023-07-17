from node import Node

node1 = Node(10, 0, 0)
node2 = Node(15, 5, 5)

print("Before collision:")
print(f"Node 1 size: {node1.size}")
print(f"Node 2 size: {node2.size}")

if node1.collide(node2):
    print("Collision occurred!")
   

print("Before collision:")
print(f"Node 1 size: {node1.size}")
print(f"Node 2 size: {node2.size}")