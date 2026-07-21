class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(1)
node2=Node(2)
node3=Node(6)
node4=Node(3)
node5=Node(4)
node6=Node(5)
node7=Node(6)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6
node6.next=node7

head=node1
current=head

key=6
while current.next:
    if current.data==key:
        current=current.next
    print(current.data,end="->")
    current=current.next
print("None")
