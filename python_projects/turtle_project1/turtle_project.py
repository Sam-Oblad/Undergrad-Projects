'''
Project Name: Turtle Project
Author: Samuel Oblad
Due Date: 2022-06-03
Course: CS1400-X02

A simple turtle program that creates a random pattern with stars, squares,
and triangles that change in size shape and color.
'''
def main():
    import turtle
    from turtle import Screen
    from random import randint
    '''
    Program starts here.
    '''
    try:
        turtle_1 = turtle.Turtle()
        turtle_2 = turtle.Turtle()
        turtle_3 = turtle.Turtle()
        width = input()  # 'Enter screen width: ')
        height = input()  # 'Enter screen height: ')
        width = int(width)
        height = int(height)
        turtle.colormode(255)
        turtle_1.speed(0)
        turtle_2.speed(0)
        turtle_3.speed(0)
    except ValueError:
        print('Width and height must be positive integers.')
        return

    if width < 1 or height < 1:
        print('Width and height must be positive integers.')
        return

    def sqr(num):
        """makes a square"""
        turtle_1.fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))
        turtle_1.begin_fill()
        for dummy in range(4):
            turtle_1.forward(num)
            turtle_1.left(90)
        turtle_1.end_fill()

    def tri(num):
        """makes a triange"""
        turtle_2.fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))
        turtle_2.begin_fill()
        for dummy in range(3):
            turtle_2.forward(num)
            turtle_2.left(120)
        turtle_2.end_fill()

    def star(num):
        """makes a star"""
        turtle_3.fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))
        turtle_3.begin_fill()
        for dummy in range(5):
            turtle_3.forward(num)
            turtle_3.right(144)
        turtle_3.end_fill()

    def shuffle(turt):
        turt.penup()
        turt.goto(randint((-width+100), (width-100)),
                  randint((-height+100), (height-100)))
        turt.color(randint(0, 255), randint(0, 255), randint(0, 255))
        turt.right(randint(0, 360))
        turt.pendown()

    screen = Screen()
    screen.setup(width, height)

    for dummy in range(int((width+height)/30)):
        sqr(randint(40, 300))
        tri(randint(40, 300))
        star(randint(40, 300))
        shuffle(turtle_1)
        shuffle(turtle_2)
        shuffle(turtle_3)
    turtle.done()


if __name__ == "__main__":
    main()
