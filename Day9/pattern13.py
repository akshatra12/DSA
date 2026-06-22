n=5
for i in range(n):
     for j in range(n-i-1):
         print(" ", end="")
     for j in range(1, i+2):
         print(j, end="")
     print()


# Output:

#     1
#    12
#   123
#  1234
# 12345