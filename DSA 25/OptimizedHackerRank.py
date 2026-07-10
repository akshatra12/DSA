# Optimize Version
def two_sum(arr,target):
        freq={}
        count=0
        for index,num in enumerate(arr):
             complement=target-num
             if complement in freq:
                 print(index,freq[complement])
                 count+=1
             else:
                  freq[num]=index
        return count
arr = [1,5,7,-1,5]
target = 6
print(two_sum(arr,target))

#Time Complexity: O(n)
#Space Complexity: O(1)
