#1 
class Node:
     def __init__(self,data):
           self.data=data  
           self.next=None 
node1=Node(5) 
node2=Node(10)
node3=Node(15) 
node4=Node(20)
node1.next=node2 
node2.next=node3  
node3.next=node4  
head=node1 
current=head 
new_node=Node(25)  
if head==None: 
     new_node.next=head 
     head=new_node 
else: 
    while current.next is not None:
          current=current.next
    current.next=new_node
current=head
count=0
while current is not None:
          count+=1
          current=current.next
print(count)  
          
         
       