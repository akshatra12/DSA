# R2
def check_anagram(s,t):
    freq1={}
    freq2={}
    for i in s:
        if i in freq1:
            freq1[i]+=1
        else:
            freq1[i]=1
    for i in t:
        if i in freq2:
            freq2[i]+=1
        else:
            freq2[i]=1
    if freq1==freq2:
        arr = [2,4,6,8,10]
        Target=8
        return binary(arr,Target,left=0,right=len(arr)-1)
    else:
        return "Not anagram"
def binary(arr,target,left,right):
    if left>right:
        return "Not found"
    mid=(left+right)//2
    if target==arr[mid]:
        return mid
    elif target>arr[mid]:
        return binary(arr,target,mid+1,right)
    else:
        return binary(arr,target,left,mid-1)
s="listen"

t="silent"
print(check_anagram(s,t))
