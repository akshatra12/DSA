#R1 Factorial
def fact(num):
    if num==1 or num==0:
        return 1
    else:
        return num * fact(num-1)
num=6
print(fact(num))