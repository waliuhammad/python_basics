arr = [4, 54, 78, 23, 1, 76, 3, 29, 50, 34, 25, 100, 8]
# Selection Sort
n = len(arr)
for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
print("Sorted list:", arr)