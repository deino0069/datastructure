def binary_search(arr, n): # Function: Used to perform binary search.
    l = 0
    u = len(arr) - 1

    while l <= u:
        mid = (l + u) // 2
        if arr[mid] == n:
            return mid 
        elif arr[mid] < n:
            l = mid + 1
        else:
            u = mid - 1

    return False

arr = [2, 3, 6, 8, 9, 12, 13]
n = 9

result = binary_search(arr, n)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")