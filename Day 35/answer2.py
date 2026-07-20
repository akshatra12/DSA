#2
class Node:
     def __init__(self,data):
           self.data=data  
           self.next=None 


head=None
current=head 
new_node=Node(100)  
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
          
         
       