#Revision 1: Sliding Window
def max_sum(arr,k):
     win_sum=0
     for i in range(k):
         win_sum+=arr[i]
         total=win_sum
     for i in range(1,len(arr)-k+1):
         win_sum=win_sum-arr[i-1]+arr[i+k-1]
         if total<win_sum:
            total=win_sum
     return total
arr=[5,2,8,1,9] 
k=2 
print(max_sum(arr,k))