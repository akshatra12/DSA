class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(1)
node2=Node(1)
node3=Node(2)
node4=Node(3)
node5=Node(3)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
head=node1
current = head
seen=set()
if head.next==None:
    head=None
else:
    prev=None
    while current:
         if current.data in seen:
             prev.next=current.next
         else:
             seen.add(current.data)
             prev=current
         current=current.next
print(seen)
