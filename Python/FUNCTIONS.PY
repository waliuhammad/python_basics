def cal_avg(a, b, c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg
cal_avg(4,6,9)

###########################################################################################################

fruits=["apple","banana","gauva","pear","apricort","grapes"]
cities=["multan","lahore","karachi","islamabad","mumbai","channei","Delhi","abbotbad"]
vegetables=["tomota","potato","garlic","chilli"]

def print_len(list):
    print(len(list))


def print_list(list):
    for items in list:
        print(items, end=" ")
print_list(fruits)       

###########################################################################################################

def cal_fact(n):
    fact=1 
    for i in range(1,n+1):
        fact*=i
    print(fact)    
cal_fact(6)

###########################################################################################################

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "usd =", inr_val, "idr")
converter(23)

###########################################################################################################

def choice(num):
    if num % 2:
        print("Even")
    else:
        print("Odd")

choice(1756)       