import random
from config import *

class Node:
   def __init__(self, name: str, size: int, x_pos: int, y_pos: int):
      #init the basic attributes
      self.name = name
      self.size = size
      self.x_pos = x_pos
      self.y_pos = y_pos
   
   def wall_collision(self):
      #see if node collides with the walls given the node bounds
      left = self.x_pos - self.size
      right = self.x_pos + self.size
      top = self.y_pos - self.size
      bottom = self.y_pos + self.size

      if top <= 0:
         return True
      elif bottom >= HEIGHT:
         return True
      elif left <= 0:
         return True
      elif right >= WIDTH:
         return True
      else:
         return False
   
   def move(self):
      #define movement and check for wall collisions
      x_add = random.randint(-MOVERANGE, MOVERANGE)
      y_add = random.randint(-MOVERANGE, MOVERANGE)

      self.x_pos += x_add
      self.y_pos += y_add

      if self.wall_collision():
         if self.y_pos - self.size <= 0:
            self.y_pos = HEIGHT - self.size
         elif self.y_pos + self.size >= HEIGHT:
            self.y_pos = self.size
         elif self.x_pos - self.size <= 0:
            self.x_pos = WIDTH - self.size
         elif self.x_pos + self.size >= WIDTH:
            self.x_pos = self.size

   def collide(self, other):
      if self.distance_to(other) <= self.size + other.size:
         self.size += other.size
         return True
      return False
   
   def distance_to(self, other):
      return ((self.x_pos - other.x_pos) ** 2 + (self.y_pos - other.y_pos) ** 2) ** 0.5