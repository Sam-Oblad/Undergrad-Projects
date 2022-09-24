'''A random walk simulation
Students: You should start with your own code for
CS 1400 Random walk. Use htis code provided as a starting points
only of you don't have your own code.

You are also welcome to start from scratch if you wish.
A reminder NOT to download solutions you may find on the internet
and submit them as your own.
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
