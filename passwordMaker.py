import random
import math
import string 
password = []
lengthOfPassword = random.randint(12,25)

for i in range(lengthOfPassword):
    upperOrLower=random.randint(1,4)
    if upperOrLower==1:
        thisLetter=random.choice(string.ascii_uppercase)
        while(password.count(thisLetter)>3):
            thisLetter=random.choice(string.ascii_uppercase)
    elif(upperOrLower==2):
        thisLetter=random.choice(string.ascii_lowercase)
        while(password.count(thisLetter)>3):
            thisLetter=random.choice(string.ascii_lowercase)
    elif(upperOrLower==3):
        thisLetter="!"
    else:
        thisLetter=random.choice(string.digits)
        while(password.count(thisLetter)>3):
            thisLetter=random.choice(string.digits)
    password.append(thisLetter) 
   
password.append('!')
password=' '.join(password)
print("Your New Random Password is: ",password.strip())