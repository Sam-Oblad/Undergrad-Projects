#apple.py
import random

class Apple():
    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.position = (0,0)
        self.randomize_position()

    def returnPos(self):
        return self.position

    def randomize_position(self):
        x = random.randint(0, self.max_x - 1)
        y = random.randint(0, self.max_y - 1)
        self.position = (x, y)
