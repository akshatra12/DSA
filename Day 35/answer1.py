#1 
class Node:
     def __init__(self,data):
           self.data=data  
           self.next=None 
node1=Node(10) 
node2=Node(20)
node3=Node(30) 
node1.next=node2 
node2.next=node3  
head=node1 
current=head 
new_node=Node(40)  
if head==None: 
     new_node.next=head 
     head=new_node 
else: 
    while current.next is not None:
          current=current.next
    current.next=new_node
current=head
while current is not None:
          print(current.data , end="->")
          current=current.next
print("None")  
          
         
       