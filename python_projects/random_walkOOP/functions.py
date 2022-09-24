"""
functions.py
This file contains the functions used in random_walk.py
"""
from typing import List, Callable
import math
import subprocess
import tempfile
import turtle
import classes
from random_walk import *
from math import dist, sqrt

def plot_dests(dests):
    '''Go to each destination and stamp the turtle.'''
    for dest in dests:
        (x_pos, y_pos) = dest
        turtle.goto(x_pos * scale(), y_pos * scale())
        turtle.stamp()

def plot(walkers: List[classes.Walker]):
    '''Perform one experiment of 50 trials of length 100 for each walker. Plot the destinations.'''
    walk_length = 100
    trials = 50
    turtle.Screen().setup(300, 400)
    turtle.speed(0)
    turtle.penup()
    turtle.shapesize(0.5, 0.5)
    for person in walkers:
        turtle.shape(person.icon)
        turtle.color(person.color)
        plot_dests(walk(walk_length, person.step, trials))

def stat_walk(length, trials, walker):
    '''For Trail Class: Perform the specified number of trials.'''
    return [stat_trial(length, walker) for _ in range(trials)]

def walk(length: int, get_step: Callable, steps):
    '''For Plot: Perform the specified number of trials.'''
    return [trial(length, get_step) for _ in range(steps)]

def simulate(length: int, trials: List[int], walker: str):
    """calls trial class to output valid stats from walks"""
    for event in trials:
        trial_1 = classes.Trial(walker, length, event)
        trial_1.run(length, event, walker)

def scale():
    '''A global constant.'''
    return 5

def stat_trial(length, walker):
    '''For Trial Class: Execute a trial. Return the scaled position.'''
    x_pos = 0
    y_pos = 0
    for _ in range(length):
        x_delta, y_delta = walker()
        x_pos += x_delta
        y_pos += y_delta
    return (x_pos, y_pos)

# get final positions
def trial(length: int, get_movement: Callable) -> tuple[int,int]:
    '''For Plot Execute a trial. Return the scaled position.'''
    x_pos = 0
    y_pos = 0
    for _ in range(length):
        x_delta, y_delta = get_movement()
        x_pos += x_delta
        y_pos += y_delta
    return (x_pos, y_pos)

def save_to_image(dest='random_walk.png'):
    '''Saves the turtle canvas to 'random_walk.png'. Do not modify this function.'''
    with tempfile.NamedTemporaryFile(prefix='random_walk',
                                     suffix='.eps') as tmp:
        turtle.getcanvas().postscript(file=tmp.name)
        subprocess.run(['gs', '-dSAFER', '-o', dest, '-r200', '-dEPSCrop', '-sDEVICE=png16m', tmp.name], stdout=subprocess.DEVNULL)

def distance(pos):
    '''Compute the euclidean distance of pos from the origin.'''
    (x_pos, y_pos) = pos
    return math.sqrt(x_pos ** 2 + y_pos ** 2)

def euclidean(location1, location2):
    '''finds the euclidean distance between two points'''
    dist(location1, location2)

def manhattan(location1, location2):
    '''finds the manhattan distance between two points'''
    return sum(abs(location1-location2))
