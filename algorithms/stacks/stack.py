class Stack:
    def __init__(self):
        self.stack_list = []
    
    def push(self, item):
        self.stack_list.append(item)
    
    def pop(self):
        if len(self.stack_list) == 0:
            raise IndexError("List is empty")
        else:
            return self.stack_list.pop()

    def top(self):
        if len(self.stack_list) == 0:
            raise IndexError("List is empty")
        else:
            return self.stack_list[-1]
    
    def size(self):
        return len(self.stack_list)
    
    def clear(self):
        self.stack_list = []