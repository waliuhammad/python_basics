def binary_search(arr, val):
    start = 0
    end = len(arr) -1
    
    while start <= end:
        mid = (start + end) // 2 
        
        if arr[mid] == val:
            return mid 
       
        if arr[mid] < val:
            start = mid + 1
    
        else:
            end = mid - 1
    return -1

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
x = 16

result = binary_search(list, x)

if result != -1:
    print("Number found at index at",result)
else:
    print("Number not found")    
    

