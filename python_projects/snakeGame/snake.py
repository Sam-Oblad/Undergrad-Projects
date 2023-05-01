#snake.py

class Snake():
    def __init__(self, body, direction, height, width):
        self.body = body
        self.direction = direction
        self.height = height
        self.width = width

    def takeStep(self, position):
        x,y = position
        hx, hy = self.head()
        hx += x
        hy += y

        if hx < 0:
            hx = self.height - 1
        elif hx >= self.height:
            hx = 0
        if hy < 0:
            hy = self.width - 1
        elif hy >= self.width:
            hy = 0

        newHead = (hx, hy)
        self.body.insert(0, newHead)
        self.body.pop()
        
    def add(self, apple):
        tail = self.body[-1]
        tx, ty = tail
        try:
            if self.direction == (-1,0):
                self.body.append((tx-1, ty))
            elif self.direction == (1,0):
                self.body.append((tx+1, ty))
            elif self.direction == (0,-1):
                self.body.append((tx, ty-1))
            elif self.direction == (0,1):
                self.body.append((tx, ty+1))
        except IndexError():
            pass

    def setDirection(self, direction):
        self.direction = direction

    def head(self):
        return self.body[0]