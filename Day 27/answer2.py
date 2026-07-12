#2
arr = [9,7,5,5,2]
increasing=True
decreasing=True
for i in range(1,len(arr)):
    if arr[i-1]<arr[i]:
        decreasing=False
    else:
        increasing=False
    i+=1
if decreasing==False and increasing == True:
    print("monotonic")
elif decreasing==True and increasing == False:
    print("monotonic")
else:
    print("not monotonic")