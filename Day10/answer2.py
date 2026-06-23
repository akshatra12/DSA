# Even Check Function
def is_even(num):
    if num%2==0:
        return True
    else:
        return False


if __name__ == "__main__":
    num=int(input("Enter a number: "))
    print(is_even(num))