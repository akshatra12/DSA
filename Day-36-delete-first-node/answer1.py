class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(5)
node2=Node(10)
node3=Node(15)

node1.next=node2
node2.next=node3

head=node1
current=head

head = head.next
current=head

while current:
    print(current.data , end="->")
    current=current.next
print("None")