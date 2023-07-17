import random

class Node:
   def __init__(self, size, x, y):
      self.size = size
      self.x = x
      self.y = y
   
   def move(self):
      self.x += random.uniform(-1, 1)
      self.y += random.uniform(-1, 1)

   def collide(self, other):
      if self.distance_to(other) <= self.size + other.size:
         self.size += other.size
         return True
      return False
   
   def distance_to(self, other):
      return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5