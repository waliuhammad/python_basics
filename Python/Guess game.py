import random

target = random.randint(1, 50)

while True:
    userchoice = (input("Guess the number OR Quite (Q) : "))
    
    if( userchoice == "Q"):
        break
    
    userchoice = int(userchoice)
    
    if( userchoice == target):
        print("Successed!!!!!! You Guess the right number.")
        break
    
    elif(userchoice < target):
        print("Sorry, Please guess again. Your number is small !!!!!!!")
     
    else:
        print("Sorry, Please guess again. Your number is big !!!!!!!")    
        
print("_____________GAME OVER_____________")        
            