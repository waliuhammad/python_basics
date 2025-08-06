import random
import string

pass_len = 15
val = string.ascii_letters + string.digits + string.punctuation

value = "".join([random.choice(val) for i in range(pass_len)])
print(value)

# password = ""
# for i in range(pass_len): 
#    password += random.choice(val)

# print("Your Random Password is =>", password) 

