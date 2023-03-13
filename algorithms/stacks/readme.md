# Project 5: A Stack Machine to Evaluate Expressions

- In this project, we will write your own Stack ADT, then use the stack to do the conversion based on pseudocode given below. Input will be from a text file, and output will be written to a text file.

# Stack ADT (stack.py)
### You will implement a Stack ADT (class Stack) that supports the following operations:

- push(item): push an item onto the stack. Size increases by 1.
- pop(): remove the top item from the stack and return it. Raise an IndexError if the stack is empty.
- top(): return the item on top of the stack without removing it. Raise an IndexError if the stack is empty.
- size(): return the number of items on the stack.
- clear(): empty the stack.

# Pseudocode For Main Program (main.py)


- Open file data.txt.
- Read an infix expression from the file.
- Display the infix expression.
- Call function in2post(expr), which you write. in2post() takes an infix expression as an input and returns an equivalent postfix expression as a string. If the expression is not valid, raise a SyntaxError. If the parameter expr is not a string, raise a ValueError.
- Display the postfix expression
- Call function eval_postfix(expr), which you write. eval_postfix() takes a postfix string as input and returns a number. If the expression is not valid, raise a SyntaxError.
- Display the result of eval_postfix().
# Output MUST match the example below. THIS INCLUDES WHITESPACE AND PUNCTUATION.

infix: 4
postfix: 4
answer: 4.0

infix: 5  +7
postfix: 5 7 +
answer: 12.0


infix: 7*5
postfix: 7 5 *
answer: 35.0

infix: (5-3)
postfix: 5 3 -
answer: 2.0

infix: 5/5
postfix: 5 5 /
answer: 1.0

infix: 8*5+3
postfix: 8 5 * 3 +
answer: 43.0

infix: 8*(5+3)
postfix: 8 5 3 + *
answer: 64.0

infix: 8+3*5-7
postfix: 8 3 5 * + 7 -
answer: 16.0

infix: (8+3)*(5-6)
postfix: 8 3 + 5 6 - *
answer: -11.0

infix: ((8+3)*(2-7))
postfix: 8 3 + 2 7 - *
answer: -55.0

infix: ((8+3)*2)-7
postfix: 8 3 + 2 * 7 -
answer: 15.0

infix: (8*5)+((3-2)-7*3)
postfix: 8 5 * 3 2 - 7 3 * - +
answer: 20.0

infix: ((8*5+3)-7)-(5*3)
postfix: 8 5 * 3 + 7 - 5 3 * -
answer: 21.0

infix: 7*9+7-5*6+3-4
postfix: 7 9 * 7 + 5 6 * - 3 + 4 -
answer: 39.0

# Pseudocode
Evaluate a Postfix Expression
Initialize a stack.
If next input is a number:
Read the next input and push it onto the stack.
Else:
Read the next character, which is an operator symbol.
Use top and pop to get the two numbers off the top of the stack.
Combine these two numbers with the operation.
Push the result onto the stack.
Go to #2 while there is more of the expression to read.
There should be one element on the stack, which is the result. Return it.
Infix to Postfix Pseudocode
Initialize stack to hold operation symbols and parenthesis.
If the next input is a left parenthesis:
Read the left parenthesis and push it onto the stack.
else if the next input is a number or operand:
Read the operand (or number) and write it to the output.
else if the next input is an operator:
while (stack is not empty AND stack's top is not left parenthesis AND stack's top is an operation with equal or higher precedence than the next input symbol):
Print the stack's top.
Pop the stack's top.
Push the next operation symbol onto the stack.
else:
Read and discard the next input symbol (should be a right parenthesis).
Print the top operation and pop it.
while stack's top is not a left parenthesis:
Print next symbol on stack and pop stack.
Pop and discard the last left parenthesis.
Go to #2 while there is more of the expression to read.
Print and pop any remaining operations on the stack.
There should be no remaining left parentheses.