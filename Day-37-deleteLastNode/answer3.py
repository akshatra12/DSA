class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(8)
node2=Node(12)
node3=Node(16)
node4=Node(20)
node5=Node(24)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
head=node1
current = head
if head.next==None:
    head=None
else:
    while current.next.next is not None:
         current=current.next
    current.next=None
count=0
current=head
while current is not None:
    count+=1
    current=current.next
print(count)
