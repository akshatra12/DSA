#Revision 2: Prefix Sum
def prefix_sum(arr):
     prefix=[0]*len(arr)
     prefix[0]=arr[0] 
     for i in range(1,len(arr)):
         prefix[i]=prefix[i-1]+arr[i] 
     return prefix 
arr=[3,6,9,12] 
print(prefix_sum(arr))