dict={
    "Name":"Wali",
    "Age":19,
    "Profession":"Student",
    "City":"Multan",
    "Degree":"Bs_It",
    "Session":"2023_2027",
    "Subject":{
 "PF":34,
 "SE":45,
 "IS":41,
 "DB":65
    }
}
print(list(dict.keys()))
print(dict.values())
pairs=(list(dict.items()))
print(pairs[2])
dict.update({"city":"Lahore"})
print(list(dict))

####################################################################################################

dict={
    "cat":"a small animal",
    "table":("a piece of furniture","list of facts and figures")
}
print(dict)

####################################################################################################

subject={"python","java","c++","pyhton","javascript","java",
         "python","java","c","C++"}
print(subject)
print(len(subject))

####################################################################################################

marks={}
A=(int(input("Enter marks of Phy :")))
marks.update({"Phy": A})
B=(int(input("Enter marks of Che :")))
marks.update({"Che": B})
C=(int(input("Enter marks of Bio :")))
marks.update({"Bio": C})
print(marks)

####################################################################################################
