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
new_node=Node(50)  
if head==None: 
     new_node.next=head 
     head=new_node 
else: 
    while current.next is not None:
          current=current.next
    current.next=new_node
current=head
max_value=current.data
while current is not None:
          max_value=max(max_value,current.data)
          current=current.next
print(max_value)  
          
         
       