class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(100)


head=node1
current = head
if head.next==None:
    head=None
else:
    while current.next.next is not None:
         current=current.next
    current.next=None

current=head
while current is not None:
    print(current.data,end="->")
    current=current.next
print("None")
