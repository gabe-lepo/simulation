import random
from config import *

class Node:
   def __init__(self, attitude: str, size: int, x_pos: int, y_pos: int):
      #init the basic attributes
      self.attitude = attitude
      self.size = size
      self.x_pos = x_pos
      self.y_pos = y_pos

      self.x_new_pos = 0
      self.y_new_pos = 0
      self.x_last_pos = 0
      self.y_last_pos = 0
   
   def move(self, other):
      #define movement and check for wall collisions
      distance_x = other.x_pos - self.x_pos
      distance_y = other.y_pos - self.y_pos
      
      if self.attitude == "patrol":
         self.x_new_pos = self.x_pos + int(distance_x * STD_WEIGHT)
         self.y_new_pos = self.y_pos + int(distance_y * STD_WEIGHT)
      elif self.attitude == "aggressive":
         self.x_new_pos = self.x_pos + int(distance_x * AGG_WEIGHT)
         self.y_new_pos = self.y_pos + int(distance_y * AGG_WEIGHT)
         self.feed_on(other)
      elif self.attitude == "defensive":
         self.x_new_pos = self.x_pos - int(distance_x * DEF_WEIGHT)
         self.y_new_pos = self.y_pos - int(distance_y * DEF_WEIGHT)
         self.feed_on(other)
      
      self.check_wall_collision()
      self.x_last_pos = self.x_pos
      self.y_last_pos = self.y_pos
      self.x_pos = self.x_new_pos
      self.y_pos = self.y_new_pos

   def check_wall_collision(self):
      if self.x_new_pos > WIDTH or self.x_new_pos < 0:
         self.x_new_pos = -self.x_pos
      if self.y_new_pos > HEIGHT or self.y_new_pos < 0:
         self.y_new_pos = -self.y_pos
   
   def feed_on(self, other):
      if self.distance_to(other) <= self.size + other.size and other.size > 0:
         self.size += 1
         other.size -= 1
   
   def distance_to(self, other):
      return round(((self.x_pos - other.x_pos) ** 2 + (self.y_pos - other.y_pos) ** 2) ** 0.5)
      #distance_x = other.x_pos - self.x_pos
      #distance_y = other.y_pos - self.y_pos
      #return distance_x, distance_y