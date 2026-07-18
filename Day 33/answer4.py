class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

node1=Node(8)
node2=Node(12)
node3=Node(5)
node4=Node(20)
node5=Node(9)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

head=node1
max_value=head.data
current=head
while current:
    if max_value < current.data:
        max_value=current.data
    current=current.next
print(max_value)
