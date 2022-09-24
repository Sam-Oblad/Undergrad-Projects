"""
classes.py
This file contains the classes used in random_walk.py
"""
import random
import functions
import statistics



def north():
    '''Take one step north.'''
    return (0, 1)

def south():
    '''Take one step south.'''
    return (0, -1)

def east():
    '''Take one step east.'''
    return (1, 0)

def west():
    '''Take one step west.'''
    return (-1, 0)

class Walker:
    def __init__(self, name, icon, color):
        self.name = name
        self.icon = icon
        self.color = color

    def step(self):
        if self.name == "pa":
            return random.choice([north(), east(), south(), west()])
        elif self.name == "mi_ma":
            return random.choice([north(), east(), south(), south(), west()])
        elif self.name == "reg":
            return random.choice([east(), west()])
        # return step

    def __str__(self):
        return self.name
walker_1 = Walker('pa', 'circle', 'black')
walker_2 = Walker('mi_ma', 'square', 'green')
walker_3 = Walker('reg', 'triangle', 'red')
walkers = [walker_1, walker_2, walker_3]

class Trial():
    def __init__(self, walker, number_of_steps, number_of_walks):
        self.number_of_steps = number_of_steps
        self.number_of_walks = number_of_walks
        self.walker = walker

    def plot(self):
        '''plots walks via turtle'''
        functions.plot(self.walker)

    def run(self, walk_lengths, trials, walker):
        '''called in trial class to compute stats on a given walk'''
        # input = Walk_lengths: 1000, Trials: 100, Walker: 'all'
        pa_pair = (walker_1.step, 'Pa')
        mi_ma_pair = (walker_2.step, 'Mi-Ma')
        reg_pair = (walker_3.step, 'Reg')
        walkers_lookup = {walker_1.name: [pa_pair],
                        walker_2.name: [mi_ma_pair],
                        walker_3.name: [reg_pair],
                        'all': [pa_pair, mi_ma_pair, reg_pair]}
        for walker, name in walkers_lookup[walker]:
            for walk_length in [walk_lengths]:
                dests = functions.stat_walk(walk_length, trials, walker)
                distances = list(map(functions.distance, dests))
                print(f'{name} random walk of {walk_length} steps')
                mean = statistics.mean(distances)
                print(f'Mean = {mean:.1f} CV = {statistics.stdev(distances)/mean:.1f}')
                print(f'Max = {max(distances):.1f} Min = {min(distances):.1f}')

    def __str__(self):
        pass
