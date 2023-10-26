class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None  # Return None if the stack is empty

    def print_stack(self):
        print(self.items)

    def size(self):
        return len(self.items)

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None  # Return None if the stack is empty

    def is_empty(self):
        return len(self.items) == 0

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:")
stack.print_stack()

print("Size of Stack:", stack.size())
print("Top item:", stack.top())

print("Popped item:", stack.pop())
print("Stack after popping:")
stack.print_stack()

print("Is the stack empty?", stack.is_empty())

    
    





