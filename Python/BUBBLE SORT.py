# Improved Bubble Sort
arr = [4, 54, 78, 23, 1, 76, 3, 29, 50, 34, 25, 100, 8]
n = len(arr)
for i in range(n - 1):
    swapped = False
    
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
                    
    if not swapped:
        break  # Stop if already sorted
    
print("Sorted list:", arr)



