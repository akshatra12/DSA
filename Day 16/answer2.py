# Print reverse numbers:

def print_rev_num(n):
    if n==0:
          return
    print(n)
    print_rev_num(n-1)
print_rev_num(5)
