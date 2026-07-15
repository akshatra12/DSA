# #R1
# observation:find first duplicate element and then push every unique element into stack and print the stack
# pattern:stack+hsahing
# Algorithm:
# 1.initialize a empty set  for stack 
# 2.run the loop from 0 to arr:
#     if i in stack:
#         clear the stack 
#         and print the duplicate element
#         break
#     else:
#         add the elements of array in stack
# 3.after breaking this loop run a loop again from 0 to arr:
#     if i not in stack then add the values in stack
# 4.return stack
# Time Complexity:O(n)
# space complexity:O(n)
# code:
def printUnique(arr):
    seen=set()
    stack=[]
    found=False
    for i in arr:
        if i in seen and found==False:
            found=True
            print(f"Duplicate is {i} ")
        else:
             seen.add(i)
             stack.append(i)
            
    return stack
    
arr = [2,5,2,7,8,7,9]
print(printUnique(arr))
