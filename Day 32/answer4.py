class Node:
    def __init__(self,data):
        self.data=data
        self.next = None
a=Node(12)
b=Node(8)
c=Node(25)
d=Node(10)

a.next=b
b.next=c
c.next=d

head=a
current=head
max_value=current.data
while current:
    if current.data > max_value:
        max_value = current.data

    current=current.next
print("Maximum value in the linked list is:", max_value)