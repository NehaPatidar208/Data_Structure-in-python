
def rotateList(head, k):
    tmp=first=second=head
    c=0
    while tmp.next !=None:
        c+=1
        tmp=tmp.next
    c=k%(c+1)
    tmp.next=first
    for i in range (c):
        tmp=tmp.next
    head=tmp.next
    tmp.next=None
    return head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        k = int(input())
        
        lis = LinkedList()
        for i in arr:
            lis.insert(i)
        
        head = rotateList(lis.head,k)
        printList(head)
