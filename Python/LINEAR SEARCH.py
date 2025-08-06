                        # Finding number by linear search

list = [2, 4, 7, 9, 1, 10, 25, 56, 3]
if 5 in list:
    print("NO. found")
else:
    print("NO. not found")    
    
    
    
                        # Finding number index by linear search
                        
                        

def linear_search(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return -1
    
list = [1,3,5,7,9,25,78,45,98,65]
x = 65
result = linear_search(list, x)

if result != -1:
    print("Number found at index", result)    
else:
    print("Number not found.")
                                       