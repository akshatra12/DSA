4
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(9)
node2=Node(3)
node3=Node(11)
node4=Node(6)

node1.next=node2
node2.next=node3
node3.next=node4

head=node1
current=head

head = head.next
current=head
max_val=0
while current:
    if max_val<current.data:
        max_val=current.data
    current=current.next
print(max_val)
