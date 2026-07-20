#1 
class Node:
     def __init__(self,data):
           self.data=data  
           self.next=None 
node1=Node(1) 
node2=Node(2)
node3=Node(3)
node4=Node(4) 
node1.next=node2 
node2.next=node3  
node3.next=node4  
head=node1 
current=head 
new_node=Node(7)  
if head==None: 
     new_node.next=head 
     head=new_node 
else: 
    while current.next is not None:
          current=current.next
    current.next=new_node
current=head
sum=0
while current is not None:
          sum+=current.data
          current=current.next
print(sum)  
          
         
       