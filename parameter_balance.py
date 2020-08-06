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


def is_matche(p1,p2):
    if ((p1=='{' and p2=='}')or(p1=='[' and p2==']')or(p1=='(' and p2==')')):
        return True
    else:
        return False

def is_paren_balanced(paren_string):
    s=Stack()
    is_balanced=True
    index = 0
    while index <len(paren_string) and is_balanced:
        paren=paren_string[index]
        if paren in'{[(':
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced=False
            else:
                top=s.pop()
                if not is_matche(top,paren):
                    is_balanced=False
        index +=1
    if s.is_empty() and is_balanced:
        return "Balanced"
    else:
        return "Not Balanced"
st=input("Enter a string")
print(is_paren_balanced(st))
