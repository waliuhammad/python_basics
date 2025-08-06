array=[54,62,76,43,20,10,65,4,7,3,51,1,89,40]
minval=array[0]
for i in array:
    if i < minval:
        minval = i
print("LOWEST VALUE IS => ",minval)




list=[1,2,3,2,1]
copy_list=list.copy()
list.reverse()

if(copy_list==list):
    print("palindrome")
else:
    print("not a palindrome")




movie=[]
movie1=input("Enter name of first movie:")
movie2=input("Enter name of second movie:")
movie3=input("Enter name of third movie:")
movie.append(movie1)
movie.append(movie2)
movie.append(movie3)
print(movie)