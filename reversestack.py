class Stack():
    def __init__(self):
        self.items=[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def isempty(self):
        return self.items == []
    def peek(self):
        if not self.isempty():
            return self.items[-1]
    def get_stack(self):
        return self.items

def reverse_str(stack,in_str):
    for i in range(len(in_str)):
        stack.push(in_str[i])
    rev_str=""
    while not stack.isempty():
        rev_str+=stack.pop()
    return rev_str

stack=Stack()
in_str="hineha"
print(reverse_str(stack,in_str))
