class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)

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
sum=0
current=head
while current is not None:
    sum+=current.data
    current=current.next
print(sum)
