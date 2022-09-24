'''A random walk simulation
Demonstrates 3 different random walks and prints out stats of each walk
as well as a turtle graphic demonstration

by Sam Oblad
'''

import sys
import turtle
import functions
import classes

walker_1 = classes.Walker('pa', 'circle', 'black')
walker_2 = classes.Walker('mi_ma', 'square', 'green')
walker_3 = classes.Walker('reg', 'triangle', 'red')
walkers = [walker_1, walker_2, walker_3]

def main():
    '''Read parameters from sys.argv, run simulate(), and then run plot().'''
    if len(sys.argv) != 4:
        print('Usage: python3 random_walk.py <walk,lengths> <trials> <walker>')
        return
    args = sys.argv[1:]
    walk_lengths, trials, walker_str = args
    try:
        trials = trials.split(',')
        trials = list(map(int, trials))
    except:
        trials = [int(trials)]
    walk_lengths = int(walk_lengths)
    functions.simulate(walk_lengths, trials, walker_str)
    functions.plot(walkers)
    turtle.exitonclick()

if __name__ == '__main__':
    main()
