# 2.12 Project 2 - Benchmarking Search Algorithms
## Introduction
- Rather than focussing on a particular data structure, this project is about some of the important theoretical and practical realities that must be considered when choosing and implementing algorithms. Sorting and searching are at the heart of many ideas in Computing as a Science. This project will help train your intuition for algorithm analysis and Big-O notation.

- It is claimed that for sufficiently large lists, differing search algorithms exhibit significantly different performance characteristics. For this project, you will benchmark the temporal efficiency (speed) of the linear search, binary search, and jump search algorithms. You will do this by implementing the search functions yourself and including a built-in measure their performance by counting the number of comparison operations performed - an approximation for how hard the algorithm has to work.

- For this project a comparison is defined as a comparison between the value or target being searched for, and a value in the list. Do not count other comparisons. For example you should not count comparisons you perform when checking the validity of an index. Expected performance values (the number of comparisons performed) assume that you implement reasonable versions of the algorithms (i.e. you aren't performing a lot of needless work). Recursion is not required for this project though you may use it if you want.

# Search Functions
## Implement the following search algorithm functions:

- (boolean, int) linear_search(lyst, target) : Performs a linear search through lyst for target. Returns True if found, False otherwise; followed by the number of comparisons performed during the search.
(boolean, int) binary_search(lyst, target) : Performs a binary search through lyst for target. Returns True if found, False otherwise; followed by the number of comparisons performed during the search.
(boolean, int) jump_search(lyst, target) : Performs a jump search through lyst for target. Returns True if found, False otherwise; followed by the number of comparisons performed during the search.
As shown, each function should return a tuple containing first a boolean value (True/False) indicating if the search value was found, followed next by the number of comparisons performed by the algorithm while searching for the target value. Assume the target type is integer, and the list contains only integers. Use of "lyst" as an identifier is NOT a typo since "list" is a data type in Python. All algorithms may assume the list is sorted. (Note: this means that when testing your functions with random data you should first sort the data)

## Testing Your Code
- As with Project 1, when you submit this project for grading the performance of your functions will be evaluated using an automated test suite. In general it is NOT a good idea to become dependent upon your professors (or anyone else) to test your code for you. Ultimately YOU are responsible for making sure that your code runs properly.

- To help you avoid becoming overly dependent upon our tests some of them have been hidden - meaning that if your project is not implemented correctly you may fail one of our tests without it being apparent why. This is to help you by encouraging you to develop YOUR OWN tests to validate your work. On this and future projects we highly recommend taking advantage of a conditionally executed main function (provided for you in the template), and any test functions you choose to implement, to assist you as you develop your solutions.