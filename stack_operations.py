class Stack():
    def __init__(self):                                 #constructor of class
        self.items=[]
    def push(self,item):                                #push method 
        self.items.append(item)
    def pop(self):                                      #pop method
        return self.items.pop()
    def get_stack(self):                                #get_stack method
        return self.items
    def is_empty(self):                                 #is_empty method
        return self.items==[]
    def peek(self):                                     #peek method
        if not self.is_empty():
            return self.items[-1]
s=Stack()                                                #reference variable of class

t=int(input("Enter 1 for apply operation sn stack "))    

while(t==1):
    strng="""\nEnter 1: for push item\nEnter 2: for pop item\nEnter 3: to print stack items
Enter 4: for check whether the stack is empty or not\nEnter 5: for print top of the stack/peek\n"""
    n=int(input(strng))
    if n==1:
        pushitem=input("Enter an element to push into the stack")
        s.push(pushitem)
    elif n==2:
        print("popped item is : ",s.pop())
    elif n==3:
        print("stack elements are : ",s.get_stack())
    elif n==4:
        print(s.is_empty())
    elif n==5:
        print("top of the stack is : ",s.peek())
    else:
        print("Invalid input")
    t=int(input("\nEnter 1 for apply operation sn stack "))
            
    

