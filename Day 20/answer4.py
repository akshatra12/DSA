def insertion(arr):
     n=len(arr)
     count=0
     for i in range(1,n):
         key=arr[i]
         j=i-1
         while j>=0 and key<arr[j]:
             arr[j+1]=arr[j]
             count+=1
             j-=1
         arr[j+1]=key
     return count

arr=[5,2,4,1,3]
print(insertion(arr))