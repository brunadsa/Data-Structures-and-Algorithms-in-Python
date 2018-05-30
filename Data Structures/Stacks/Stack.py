
#Stack with Arrays

class Stack_array:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1] #delete
        return data

    def peek(self):
        return self.stack[-1]

    def sizeStack(self):
        return len(self.stack)


stack = Stack_array()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.sizeStack())
print("Popped: ", stack.pop())
print("Popped: ", stack.pop())
print(stack.sizeStack())
print("Peek: ", stack.peek())
print(stack.sizeStack())