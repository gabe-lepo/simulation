import random
from config import *

class Node:
   def __init__(self, name: str, size: int, x_pos: int, y_pos: int):
      #init the basic attributes
      self.name = name
      self.size = size
      self.x_pos = x_pos
      self.y_pos = y_pos

      self.x_new_pos = 0
      self.y_new_pos = 0
      self.x_last_pos = 0
      self.y_last_pos = 0
   
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
   
   def move(self, type: str):
      #define movement and check for wall collisions
      if type == "random":
         self.x_new_pos = random.randint(0 + SIZE, WIDTH - SIZE)
         self.y_new_pos = random.randint(0 + SIZE, HEIGHT - SIZE)
      elif type == "standard":
         self.x_new_pos = self.x_pos + random.choice([-MOVERANGE, MOVERANGE])
         self.y_new_pos = self.y_pos + random.choice([-MOVERANGE, MOVERANGE])
      
      if self.x_new_pos > WIDTH or self.x_new_pos < 0:
         self.move("standard")
      if self.y_new_pos > HEIGHT or self.y_new_pos < 0:
         self.move("standard")
         
      self.x_last_pos = self.x_pos
      self.y_last_pos = self.y_pos
      self.x_pos = self.x_new_pos
      self.y_pos = self.y_new_pos

   def collide(self, other):
      if self.distance_to(other) <= self.size + other.size:
         self.size += other.size
         return True
      return False
   
   def distance_to(self, other):
      return ((self.x_pos - other.x_pos) ** 2 + (self.y_pos - other.y_pos) ** 2) ** 0.5