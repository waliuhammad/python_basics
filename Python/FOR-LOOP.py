tuple=("wali",19,"Ehtisham",21,"Hassan",20)
for item in tuple:
    print(item)

###########################################################################################################

str="WalliMuhammad"
for char in str:
    if(char=="u"):
        print("founded....")
    print(char)

###########################################################################################################

tup=(1,4,9,16,25,36,49,64,81,100,16)
x=16

idx=0
for num in tup:
    if(num==x):
        print("num found ",idx)
        continue
    idx+=1

###########################################################################################################
n=5
fac=1
for i in range(0,n):
    print(i)
    i+=1
    fac*=i
print(fac)    
