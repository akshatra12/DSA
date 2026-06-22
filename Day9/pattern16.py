n=5
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,i+2):
        print(j,end="")
    for j in range(i):
        print(i-j,end="")
    print()
# Output
#      1
#     121
#    12321
#   1234321
#  123454321