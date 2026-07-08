def unique(arr1,arr2):
    seen1=set()
    seen2=set()
    for i in arr1:
        if i not in seen1:
            seen1.add(i)
    for i in arr2:
        if i not in seen2:
            seen2.add(i)
    if seen1==seen2:
        return True
    else :
        return False

arr1 = [1,2,3]
arr2 = [1,2,4]
print(unique(arr1,arr2))