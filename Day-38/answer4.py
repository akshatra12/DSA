class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(2)
node2=Node(5)
node3=Node(8)
node4=Node(10)

node1.next=node2
node2.next=node3
node3.next=node4

head=node1
current=head
new_node=Node(6)

while current and current.data!=5:
    current=current.next
new_node.next=current.next
current.next=new_node

current=head
max_val=current.data
while current:
    if max_val<current.data:
        max_val=current.data
    current=current.next
print(max_val)
