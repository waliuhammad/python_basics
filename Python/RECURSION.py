def value(n):
    if(n==0):
        return
    print(n)
    value(n-1)

value(15)




def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n - 1) * n
 
print(fact(7))   

  


def sum(n):
    if(n==0):
        return 0
    return sum(n-1) + n

print(sum (10))



def print_list(list , idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

alpha=["a","b","c","d","e","f","g","h","i","j","k","l"]

print_list(alpha)


