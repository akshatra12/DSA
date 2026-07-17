class Node:
    def __init__(self,data):
        self.data=data
        self.next = None
a=Node(5)
b=Node(10)
c=Node(15)
d=Node(20)

a.next=b
b.next=c
c.next=d

print(c.data)