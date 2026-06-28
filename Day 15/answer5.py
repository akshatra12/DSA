# Subarrays of Size 2
def subarrays(arr):
      k = 2

      for i in range(len(arr) - k + 1):
          print(arr[i:i+k]) 


arr=[2,4,6,8,10]
print(subarrays(arr))


