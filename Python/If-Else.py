print("Please enter your Name and Age:")
name = input("Name: ")
print("Name is:", name)
try:
    age = int(input("Age: "))
    print("Age is:", age)
    print("Let's check whether you are eligible to vote or not?")
    if age >= 18:
        print("You are eligible to cast the vote.")
    else:
        print("Sorry, you are not eligible to cast the vote.")
except ValueError:
    print("Invalid age input. Please enter a numeric value.")