'''
Project Name: Turtle Project
Author: Samuel Oblad
Due Date: 2022-06-03
Course: CS1400-X02

A simple turtle program that creates a random pattern with stars, squares,
and triangles that change in size shape and color.

By Sam Oblad
'''

import turtle
from turtle import Screen
from random import randint


def main():
    '''
    Program starts here.
    '''
    try:
        color_modifier = input(
            "Please enter any number less than 256 to modify the colors: ")
        color_modifier = int(color_modifier)
    except ValueError:
        print('Please enter a number between 0 and 255')
        return

    if color_modifier > 255 or color_modifier < 0:
        print("Please enter a number between 0 and 255")
        return

    turtle_1 = turtle.Turtle()
    turtle_2 = turtle.Turtle()
    turtle_3 = turtle.Turtle()
    turtle_4 = turtle.Turtle()
    turtle_5 = turtle.Turtle()
    width = 1000
    height = 1000
    width = int(width)
    height = int(height)
    turtle.colormode(255)
    turtle_1.speed(0)
    turtle_2.speed(0)
    turtle_3.speed(0)
    turtle_4.speed(0)
    turtle_5.speed(0)

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
        """shuffles colors and positions"""
        turt.penup()
        turt.goto(randint((-width/10), (width/10)),
                  randint((-height/10), (height/10)))
        turt.color(randint(0, color_modifier), randint(
            color_modifier, 255), randint(0, color_modifier))
        turt.right(randint(0, 360))
        turt.pendown()

    def frame(turt, x_coord, y_coord):
        """draws a picture frame"""
        turt.penup()
        turt.goto(x_coord, y_coord)
        turt.pendown()
        for dummy in range(0, 4):
            turt.forward(abs(x_coord)*2)
            turt.right(90)

    def rectangle(turt, width, length, x_coord, y_coord):
        """draws a rectangle"""
        turt.penup()
        turt.goto(x_coord, y_coord)
        turt.pendown()
        for dummy in range(0, 2):
            turt.forward(width)
            turt.right(90)
            turt.forward(length)
            turt.right(90)

    def polaroid(turt, frame_x, frame_y, rect_w, rect_l, rect_x, rect_y):
        """draws a polaroid picture"""
        frame(turt, frame_x, frame_y)
        rectangle(turt, rect_w, rect_l, rect_x, rect_y)

    def pencil(turt, width, length, x_coord, y_coord):
        """draws a pencil"""
        turt.right(120)
        rectangle(turt, width, length, x_coord, y_coord)
        for dummy in range(0, 3):
            turt.forward(30)
            turt.left(120)

    screen = Screen()
    screen.setup(width, height)

    for dummy in range(int((width+height)/50)):
        sqr(randint(10, 90))
        tri(randint(10, 90))
        star(randint(10, 90))
        shuffle(turtle_1)
        shuffle(turtle_2)
        shuffle(turtle_3)

    polaroid(turtle_4, -205, 205, 450, 520, -225, 225)
    pencil(turtle_5, 30, 400, -100, 275)

    turtle_1.hideturtle()
    turtle_2.hideturtle()
    turtle_3.hideturtle()
    turtle_4.hideturtle()
    turtle_5.hideturtle()

    turtle.done()


if __name__ == "__main__":
    main()
