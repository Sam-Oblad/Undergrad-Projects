# Benchmarking Sorting Algorithms
## Introduction:
- For this project, you will investigate the performance differences between a set of sorting algorithms. Like Project 1, this project is about important theoretical and practical algorithms rather than abstract data types. Sorting and searching are at the heart of many ideas and algorithms in Computer Science. Studying such algorithms will help develop your intuition for algorithm selection and design, and your ability to use Big-O notation to analyze and communicate about algorithms.

## Part 1: Implementation
You will be investigating 4 algorithms

Quicksort
Mergesort
Insertion Sort
Selection Sort
- Even though most of these are in-place, destructive sorts (meaning that they sort the actual list, “destroying” its original configuration) - each function should return the sorted list, as well as the number of comparisons and swaps performed during the sort. In addition to the four sorting functions, you will also need to implement a function to determine if a given list is sorted. Here is a list of the function prototypes and descriptions for the functions our unit tests will be looking for:

- boolean is_sorted(lyst): This is a predicate function that returns True if lyst is sorted, False otherwise. In addition to verifying that lyst is a list, is_sorted() must also verify that every element in the list is an integer. If lyst is not a list, or a non-integer element is found in it, is_sorted should raise a TypeError exception. Note: We recommend implementing this function first, so that you can use it to do unit testing as you develop your sorting functions.

- (list, int, int) quicksort(lyst): This function implements the quicksort algorithm to sort the items in lyst. the function returns a tuple containing the sorted list, followed by the number of comparisons, and finally the number of swaps performed while sorting. lyst must be a Python list containing comparable data (i.e. things that the >,<, etc. operators can be used on to determine an ordering between two items). If lyst is not a list, quicksort() must raise a TypeError Exception.

- (list, int, int) mergesort(lyst): This function implements the mergesort algorithm to sort the items in lyst. the function returns a tuple containing the sorted list, followed by the number of comparisons, and finally the number of swaps performed while sorting. lyst must be a Python list containing comparable data (i.e. things that the >,<, etc. operators can be used on to determine an ordering between two items). If lyst is not a list, mergesort() must raise a TypeError Exception.

- (list, int, int) selection_sort(lyst): This function implements the selection sort algorithm to sort the items in lyst. the function returns a tuple containing the sorted list, followed by the number of comparisons, and finally the number of swaps performed while sorting. lyst must be a Python list containing comparable data (i.e. things that the >,<, etc. operators can be used on to determine an ordering between two items). If lyst is not a list, selection_sort() must raise a TypeError Exception.

- (list, int, int) insertion_sort(lyst): This function implements the insertion sort algorithm to sort the items in lyst. the function returns a tuple containing the sorted list, followed by the number of comparisons, and finally the number of swaps performed while sorting. lyst must be a Python list containing comparable data (i.e. things that the >,<, etc. operators can be used on to determine an ordering between two items). If lyst is not a list, insertion_sort() must raise a TypeError Exception.