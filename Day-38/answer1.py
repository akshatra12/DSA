class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(5)
node2=Node(10)
node3=Node(20)
node4=Node(30)

node1.next=node2
node2.next=node3
node3.next=node4

head=node1
current=head
new_node=Node(15)

while current and current.data!=10:
    current=current.next
new_node.next=current.next
current.next=new_node

current=head
while current:
    print(current.data,end="->")
    current=current.next
print("None")
