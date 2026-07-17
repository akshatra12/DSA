class Node:
    def __init__(self,data):
        self.data=data
        self.next = None
a=Node(5)
b=Node(10)
c=Node(15)

a.next=b
b.next=c

head=a
current=head
sum=0
while current:
    sum+=current.data
    current=current.next
print("Sum of all elements in the linked list is:", sum)
