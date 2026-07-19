class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(9)
node2=Node(12)
node3=Node(15)

node1.next=node2
node2.next=node3

head=node1


new_node=Node(7)
new_node.next=head
head=new_node
current=head
while current:
    print(current.data , end="->")
    current=current.next
print("None")
