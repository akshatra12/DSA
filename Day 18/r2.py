#Revision 2: Recursion Power
def power(num,expo):
    if expo==0:
        return 1
    else:
        return num * power(num,expo-1)
print(power(3,4))