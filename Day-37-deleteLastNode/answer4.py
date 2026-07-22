class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(3)
node2=Node(7)
node3=Node(2)
node4=Node(11)


node1.next=node2
node2.next=node3
node3.next=node4

head=node1
current = head
if head.next==None:
    head=None
else:
    while current.next.next is not None:
         current=current.next
    current.next=None
max_value=0
current=head
while current is not None:
    if max_value<current.data:
        max_value=current.data
    current=current.next
print(max_value)

