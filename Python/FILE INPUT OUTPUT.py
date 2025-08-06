f=open("demo.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()



f=open("demo.txt","r")
l1=f.readline()
print(l1)
l2=f.readline()
print(l2)
l3=f.readline()
print(l3)
f.close()



f=open("demo.txt","a")
f.write("\nI will Learn Data structure further.")
f.close()



f=open("sample.txt","w")
f.close()



f=open("demo.txt","a+")
f.write("am wali")
f.read()
f.close()



with open("demo.txt", "r") as f:
    data=f.read()
    print(data)

with open("demo.txt", "w") as f:
    f.write("I Am Wali Muhammad.")



import os
os.remove("sample.txt")



with open ("practise.txt" , "r") as f:
    data=f.read()
new_data=data.replace("java", "python")   
print(new_data) 
with open ("practise.txt" , "w") as f:
    f.write(new_data)



def check_word():
   word="learning"
   with open("practise.txt", "r") as f:
       data=f.read()
       if(data.find(word) != -1):
          print("Found")
       else:
        print("Not Found")
check_word()




def check_word():
    word="learning"
    data= True
    line_no=1
    with open("practise.txt", "r") as f:
        while data: 
            data=f.readline()
            if word in data:
                print(line_no)
                return
            line_no +=1

    return -1
check_word()      


count=0
with open("practise.txt", "r") as f:
    data=f.read()
    print(data)
# num=""
# for i in range(len(data)):
#     if data[i]==",":
#         print(int(num))
#         num=""
#     else:
#         num+=data[i]  
    num = data.split(",")
    for i in num:
        if (int(i)) % 2 == 0:
            count += 1
print(count)            


