'''
Project: BST
Author: Sam Oblad
Course: cs2420
Date: April 2, 2023

Description:

Lessons Learned:

'''
from pathlib import Path
from string import whitespace, punctuation
from bst import BST

class Pair:
    ''' Encapsulate letter,count pair as a single entity.
    
    Realtional methods make this object comparable
    using built-in operators. 
    '''
    def __init__(self, letter, count = 1):
        self.letter = letter
        self.count = count
    
    def __eq__(self, other):
        return self.letter == other.letter
    
    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'
    
    def __str__(self):
        return f'({self.letter}, {self.count})'

def make_tree():
    tree = BST()

    # Open the file and read it character by character
    with open("around-the-world-in-80-days-3.txt", "r") as file:
        for char in file.read():
            if not char.isspace() and not char.isalnum():
                continue
            if char == '\n' or char == " ":
                continue
            char = char.lower()

            # Check if the character is already in the BST
            try:
                pair = tree.find(Pair(char, None))
                pair.count += 1
            except ValueError:
                # Insert the character with count 1
                tree.add(Pair(char, 1))

    return tree

def main():
    make_tree()
    
if __name__ == "__main__":
    main()
