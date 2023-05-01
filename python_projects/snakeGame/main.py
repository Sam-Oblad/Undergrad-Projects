from snake import Snake
from apple import Apple
import sys
import threading
import time

UP = (-1,0)
DOWN = (1,0)
LEFT = (0,-1)
RIGHT = (0,1)

class Game():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.snake = Snake([(4,7),(4,8),(5,8),(5,9)], LEFT, self.height, self.width)
        self.apple = Apple(self.height, self.width)
        self.score = 0

    def boardMatrix(self):
        #returns a list of lists containing none based on size of game
        self.matrix = []
        for _ in range(self.height):
            innerMatrix = []
            for _ in range(self.width):
                innerMatrix.append(None)
            self.matrix.append(innerMatrix)
        return self.matrix

    def render(self):
        #renders the matrix returned by boardMatrix() and adds a border to it and renders snake in it
        matrix = self.boardMatrix()
        ax, ay = self.apple.returnPos()
        matrix[ax][ay] = "*" 

        for segment in self.snake.body:
            x,y = segment
            matrix[x][y] = "0"

        head = self.snake.head()
        x,y = head
        matrix[x][y] = "X"

        print("+" + "-" * self.width + "+")
        for row in self.matrix:
            output = "|"
            for item in row:
                if item is None:
                    output += " "
                else:
                    output += item
            output += "|"
            print(output)
        print("+" + "-" * self.width + "+")

    def updateGame(self):
        self.snake.takeStep(self.snake.direction)
        self.checkPos()
        
    def checkPos(self):
        if self.snake.head() in self.snake.body[1:]:
            print("Game Over")
            print(f"Total score: {self.score}")
            quit()
        if self.snake.head() == self.apple.returnPos():
            self.snake.add(self.snake.head())
            self.score += 1
            del self.apple
            self.apple = Apple(self.height, self.width)


    def play(self):
        #main game loop
        while True:
            self.render()
            userInput = input("Enter WASD to move, then press enter, or 'q' to quit. . . ")
            userInput = userInput.lower()
            if userInput == 'q':
                break
            if userInput == "w":
                self.snake.setDirection(UP)
            elif userInput == 'd':
                self.snake.setDirection(RIGHT)
            elif userInput == 's':
                self.snake.setDirection(DOWN)
            elif userInput == 'a':
                self.snake.setDirection(LEFT)
            self.updateGame()
                
def main():
    game = Game(10, 20)
    game.play()

if __name__ == "__main__":
    main()