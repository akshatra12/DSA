class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(100)

head=node1
current=head

head = head.next
current=head

while current:
    print(current.data , end="->")
    current=current.next
print("None")

