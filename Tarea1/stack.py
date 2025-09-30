class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return "The stack is empty"
        
    def peek(self):
         if self.stack:
            return self.stack[-1]
         else:
            return "The stack is empty"
         
    def empty(self):
         return len(self.stack) == 0
         
    def size(self):
        return len(self.stack)

stack = Stack()
print(f"The stack initialized is {stack.stack}")
print("--------------------------------")
print(f"Appendings Element")
stack.push(1)
print(stack.stack)
stack.push(2)
print(stack.stack)
stack.push(3)
print(stack.stack)
stack.push(4)
print(stack.stack)
print("--------------------------------")
print(f"Popping elements")
stack.pop()
print(stack.stack)
stack.pop()
print(stack.stack)
print("--------------------------------")
print(f"The Stack is emtpy: {stack.empty()}")
print("--------------------------------")
print(f"The peek element is {stack.peek()}")
print("--------------------------------")
print(f"The size of the stack is: {stack.size()}")
print("--------------------------------")
