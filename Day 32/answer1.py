# 1
class Node:
    def __init__(self,data):
        self.data=data
        self.next = None
a=Node(10)
b=Node(20)
c=Node(30)

a.next=b
b.next=c

head=a
current=head
while current:
    print(current.data,"\n")
    current=current.next
