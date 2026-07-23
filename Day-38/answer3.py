class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(8)
node2=Node(12)
node3=Node(16)
node4=Node(20)

node1.next=node2
node2.next=node3
node3.next=node4

head=node1
current=head
new_node=Node(18)

while current and current.data!=12:
    current=current.next
new_node.next=current.next
current.next=new_node

current=head
count=0
while current:
    count+=1
    current=current.next
print(count)
