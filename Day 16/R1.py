# Find First Duplicate
def duplicate(arr):
    
     freq={}
     for i in arr:
         if i in freq:
              freq[i]+=1
              return i
        
         else:
              freq[i]=1
arr = [1,2,3,2,4,5]
print(duplicate(arr))
