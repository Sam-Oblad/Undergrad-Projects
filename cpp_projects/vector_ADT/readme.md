# Vector
### In this project I created my own vector ADT using pointers and an array in CPP. Here is the instructions:

Background
You have been using std::vector for a while now. In this assignment you will implement a simple
version of vector, that just holds ints. You will define some of the same member functions that
std::vector does, and they will behave the same way. The goal of this project is to learn how to
manage dynamic memory on the heap. You will allocate an array on the heap for your Vector class to
store ints in. When your underlying memory is used up, and you want to append or insert a new
element, you will need to allocate a new array, copy the current elements to it, and then delete the
old array.
Requirements
Call your class Vector (capital-v). Your constructor should allocate an initial array big enough to hold
10 ints (a constant named CHUNK), which is its initial "capacity", but the "size" (the numbers of
elements currently in use) will initially be zero. Do not hard-code the 10. (See the header below).
When you expand the array, make the new capacity 1.6 times the current capacity (initially CHUNK).
The following diagram illustrates a Vector instance managing heap memory.
Figure 1 How Vector uses a Dynamic Array
I am providing the Vector.h file for you that declares everything in the class. Your job is to implement
the member functions in the file Vector.cpp. The file Vector.h is found in the Canvas assignment,
along with a test driver for it.

In this project we are introducing the size_t type synonym, defined in <cstddef>. size_t is used for
array/vector index positions and for the size (number of elements) of allocated memory. It
is synonym because it is equivalent to either an unsigned int or an unsigned long, depending on the
platform. We use it whenever we refer to array sizes or positions.
You are also provided a test driver, testVector.cpp, and a test framework in test.h, to rigorously test
your project before you turn it in. The expected output is:
grow
 
Test Report: 
Number of Passes = 78
Number of Failures = 0
 
The occurrence of “grow” above is a trace statement from your grow function, to verify that it
executed once. It is best to comment-out much of the testing while you are developing your solution,
so you test a little at a time. Your grade will be the percentage of tests that you pass, modulo some
minor adjustment in points for coding style.
Implementation Notes
I have given you the hint that will need a private grow function whenever you need to expand the
array from the push_back or insert functions.
In all cases where an array position is mentioned, check if it is within bounds, except for in
the operator[] function. Throw a std::range_error (defined in <stdexcept>) in that case. This
includes front and back as well, since they fail when the size is 0. Six functions need to throw
exceptions. Include an informational message inside the exception object.
Remember that you will be doing dynamic memory allocation in the copy constructor, copy
assignment operator and copy assignment operator. The destructor frees the heap memory with
the delete [] operato