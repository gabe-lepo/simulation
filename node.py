class Node:
   def __init__(self, name: str, size: int, x_pos: int, y_pos: int):
      self.name = name
      self.size = size
      self.x_pos = x_pos
      self.y_pos = y_pos
   
   def move(self, x_add, y_add):
      self.x_pos += x_add
      self.y_pos += y_add

   def collide(self, other):
      if self.distance_to(other) <= self.size + other.size:
         self.size += other.size
         return True
      return False
   
   def distance_to(self, other):
      return ((self.x_pos - other.x_pos) ** 2 + (self.y_pos - other.y_pos) ** 2) ** 0.5