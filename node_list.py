from config import *
import random

LIST = [
    {
      "ATTITUDE": "standard",
      "SIZE": random.randint(SIZE, SIZE*4),
      "X_POS": (1/4)*WIDTH,
      "Y_POS": (1/2)*HEIGHT
    },
    {
      "ATTITUDE": "standard",
      "SIZE": random.randint(SIZE, SIZE*4),
      "X_POS": (3/4)*WIDTH,
      "Y_POS": (1/2)*HEIGHT
    }
]