#Darryl Terrobias
#17/02/2024

#Write a program here that finds the first four perfect numbers.
#Put your name and date at the top of the file.
#The pseudocode in the README.md file will help you write this program.

from perfectNumber import perfectNumber

#set the totalPFs variable to 0
totalPFs = 0

#set the testNumber variable to 1
testNumber = 1

#while the totalPFs variable is less than or equal to 3
while totalPFs < 4:
    
    #if the testNumber is a perfect
        if isPerfectNumber(testNumber):
            
        #print the testNumber is a perfect number
            print (f"{testNumber} is a perfect number")
        
        #increment the totalPFs variable by 1
            totalPFs += 1
            
   #increment the testNumber variable
        testNumber += 1
