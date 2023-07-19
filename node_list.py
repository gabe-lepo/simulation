from config import *
import random

LIST = [
    {
      "ATTITUDE": "aggressive",
      "SIZE": random.randint(SIZE, SIZE*4),
      "X_POS": (1/4)*WIDTH,
      "Y_POS": (1/2)*HEIGHT
    },
    {
      "ATTITUDE": "defensive",
      "SIZE": random.randint(SIZE, SIZE*4),
      "X_POS": (3/4)*WIDTH,
      "Y_POS": (1/2)*HEIGHT
    }
]