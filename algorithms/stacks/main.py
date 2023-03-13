from stack import Stack
import os
def openFile(file):
    with open(file) as file:
        return file.readlines()
        
def eval_postfix(expr = ''):
    pass
    stack = Stack()
    operators = ['+', '-', '*', '/']
    op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: x / y}
    if type(expr) != str:
        raise ValueError
    for char in expr:
        if char.isdigit():
            stack.push(float(char))
        elif char in operators and stack.size() == 1:
            raise SyntaxError()
        elif char != ' ':
            y = stack.pop()
            x = stack.pop()
            result = op[char](float(x), float(y))
            stack.push(result)
    return stack.pop()

def in2post(expr):
    if not isinstance(expr, str):
        raise ValueError("Input expression is not a string")
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0}
    stack = Stack()
    postfix = ""

    for char in expr:
        if char.isdigit():
            postfix += char + " "
        elif char in ["+", "-", "*", "/"]:
            while not stack.size() == 0 and stack.top() != "(" and precedence[stack.top()] >= precedence[char]:
                postfix += stack.pop() + " "
            stack.push(char)
        elif char == "(":
            stack.push(char)
        elif char == ")":
            while not stack.size() == 0 and stack.top() != "(":
                postfix += stack.pop() + " "
            if not stack.size() == 0 and stack.top() == "(":
                stack.pop()
            else:
                raise SyntaxError("Mismatched parentheses")
    while not stack.size() == 0:
        if stack.top() == "(":
            raise SyntaxError("Mismatched parentheses")
        postfix += stack.pop()
        postfix += " "
    return postfix

def main():
    lines = openFile("data.txt")
    for line in lines:
        print(f"infix: {line}", end="")
        postfix = in2post(line)
        print(f"postfix: {postfix}") 
        print(f"answer: {eval_postfix(postfix)}")
        print()
    
if __name__=="__main__":
    main()