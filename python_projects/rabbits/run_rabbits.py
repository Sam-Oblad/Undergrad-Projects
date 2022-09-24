'''A simple runner for testing and to demonstrate how to import a module from a
local directory. Models the overall growth of rabbit population according to
given parameters

By Sam Oblad
'''

import rabbits

def main():
    '''Call the do_research function with default arguments.
    '''
    rabbits.do_research(500, 1, 0)

if __name__ == '__main__':
    main()
