class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=None


new_node=Node(100)
new_node.next=head
head=new_node
current=head
while current:
    print(current.data , end="->")
    current=current.next
print("None")
    
