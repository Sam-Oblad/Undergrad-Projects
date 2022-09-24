'''A simple runner for testing and to demonstrate how to import a module from a
local directory.
'''

import rabbits

def main():
    '''Call the do_research function with default arguments.
    '''
    rabbits.do_research(500, 1, 0)

if __name__ == '__main__':
    main()
