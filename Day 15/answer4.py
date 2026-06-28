# General Function
def range_sum(arr,left,right):
     prefix=[0]*len(arr)
     prefix[0]=arr[0]
     for i in range(1,len(arr)):
         prefix[i]=prefix[i-1]+arr[i]
     if left==0:
         sum=prefix[right]
     else:
         sum=prefix[right] - prefix[left-1]
     return sum
     
    
     
left = int(input("Enter the left range of array :"))
right = int(input("Enter the right range of array :"))

arr=[2,4,6,8,10]
print(range_sum(arr,left,right))

