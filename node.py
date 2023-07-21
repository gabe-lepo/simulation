import random
from config import *

class Node:
   def __init__(self, size: int, x_pos: int, y_pos: int):
      #init the basic attributes
      self.size = size
      self.x_pos = x_pos
      self.y_pos = y_pos

      self.x_new_pos = 0
      self.y_new_pos = 0
      self.x_last_pos = 0
      self.y_last_pos = 0

      self.top_border = self.y_pos - (1/2) * HEIGHT
      self.bottom_border = self.y_pos + (1/2) * HEIGHT
      self.left_border = self.x_pos - (1/4) * WIDTH
      self.right_border = self.x_pos + (1/4) * WIDTH

      self.attitude = ""
   
   def move(self, other):
      #define movement and check for wall collisions
      distance_x = other.x_pos - self.x_pos
      distance_y = other.y_pos - self.y_pos
      
      if self.attitude == "patrol":
         move_distance = STD_WEIGHT * 50

         if self.x_last_pos <= self.x_pos:
            self.x_new_pos = self.x_pos + random.randint(-move_distance, move_distance*2)
         else:
            self.x_new_pos = self.x_pos + random.randint(-move_distance, move_distance)

         self.y_new_pos = self.y_pos + random.randint(-move_distance, move_distance)
      elif self.attitude == "aggressive":
         self.x_new_pos = self.x_pos + (1/2) * int(distance_x * AGG_WEIGHT)
         self.y_new_pos = self.y_pos + (1/2) * int(distance_y * AGG_WEIGHT)
         self.feed_on(other)
      elif self.attitude == "defensive":
         move_distance = 3
         defensive_distance = SIZE
         distance_to_other = ((distance_x) ** 2 + (distance_y) ** 2) ** 0.5
         
         if distance_to_other < defensive_distance:
            dx_normalized = distance_x / distance_to_other if distance_to_other > 0 else 0
            dy_normalized = distance_y / distance_to_other if distance_to_other > 0 else 0

            movement_speed = 3
            self.x_new_pos = self.x_pos - int(dx_normalized * movement_speed)
            self.y_new_pos = self.y_pos - int(dy_normalized * movement_speed)
         else:
            self.x_new_pos = self.x_pos + random.randint(-move_distance, move_distance)
            self.y_new_pos = self.y_pos + random.randint(-move_distance, move_distance)
      elif self.attitude == "dead":
         self.x_new_pos = self.x_last_pos
         self.y_new_pos = self.y_last_pos

      self.x_last_pos = self.x_pos
      self.y_last_pos = self.y_pos
      if self.check_wall_collision():
         #print(f"Hit a border at {self.x_pos}, {self.y_pos}")
         self.x_pos = self.x_last_pos
         self.y_pos = self.y_last_pos
      else:
         self.x_pos = self.x_new_pos
         self.y_pos = self.y_new_pos

   def check_wall_collision(self):
      if (self.x_new_pos + self.size > WIDTH) or (self.x_new_pos - self.size < 0):
         return True
      if (self.y_new_pos + self.size > HEIGHT) or (self.y_new_pos - self.size < 0):
         return True
      return False
   
   def feed_on(self, other):
      if self.distance_to(other) <= self.size + other.size and not(other.size == 0):
         self.size += 1
         other.size -= 1
   
   def distance_to(self, other):
      return round(((self.x_pos - other.x_pos) ** 2 + (self.y_pos - other.y_pos) ** 2) ** 0.5)
      #distance_x = other.x_pos - self.x_pos
      #distance_y = other.y_pos - self.y_pos
      #return distance_x, distance_y