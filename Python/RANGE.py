seq=range(100)
print(seq[9])
idx=1
for i in seq:
    if(i==49):
        print("49 is at ",idx)
        break
    idx+=1

###########################################################################################################

seq=range(1,150,7)
print(seq[4])
print(seq[9])
print(seq[11])
for i in seq:
    if(i==seq[15]):
        print("no on index 15 is",i)
    print(i)

###########################################################################################################

n=int(input("enter no."))
seq=range(1,11)
for i in seq:
    print(n*i)  