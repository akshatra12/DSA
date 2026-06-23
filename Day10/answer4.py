# Largest Element
def largest(arr):
    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    return largest

if __name__ == "__main__":
    arr=[1,2,3,4,5]
    print(largest(arr))