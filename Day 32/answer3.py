class Node:
    def __init__(self,data):
        self.data=data
        self.next = None
a=Node(10)
b=Node(20)
c=Node(30)
d=Node(40)

a.next=b
b.next=c
c.next=d

head=a
current=head
count=0
while current:
    count+=1
    current=current.next
print("Length of linked list is:",count)