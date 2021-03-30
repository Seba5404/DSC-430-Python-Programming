#Sebastian Zdarowski
#I have not given or received any unauthorized assistance on this assignment.”  
#Sept 24th, 2018

def labMenu(): #user input
    'Menu selection' #docstring
    print('Enter 1 to check if your number is prime.')
    print('Enter 2 to check if integer is happy number ')
    print('Enter 3 to check if integer is a prime and happy number. ')
    print('Enter 4 to enter a list of values to get 100 happy primes ')
    print('Enter 5 to enter a list of values to get 100 sad primes ')
    print('Enter 6 to end program: ')
   
def checkprime(userinput):
    #'check if number is prime' #docstring
    checklist = [2,3,5,7,9,11,13,17,19] # prime number list check 
    for x in checklist:
        checkV = userinput % x
        if userinput % x == 0 and userinput != x: #if value is 0 then its not a prime number / not equal keeps num out of list
            prime = False 
            break #if prime is false get out of loop 
        else:
            prime = True
    return prime

def happyNumCheck(userinput): # check if the number is 'happy'
    #'happy number check, userinput will drive this function' #docstring
    finish = False
    numhold = []
    happy = False
    while not finish:
        numlist = [] #blank list to hold
        rlist = [] #blank list to hold range
        r2list = [] #BLANK LIST to hold range 2
        numlen = len(str(userinput))
        rlist.extend(range(0,numlen))
        #print(rlist)
        for x in rlist:
            numlist.append(str(userinput)[x])
        userinput2 = 0
        for x in numlist: #calculation of values, depending on integer length 
            userinput2 += int(x)**2
            #print(userinput2)
        
        
        listLength = len(numhold)
        r2list.extend(range(0,listLength)) #check list length 
        if userinput == 1: #check if number is happy
            finish = True 
            happy = True 
            
            #print(numlist)
        
        userinput = userinput2

        for x in r2list: #check if number is already in list, if so then exit 
            hold = int(numhold[x])
            if userinput == hold:
                if happy == True:
                    break
                else:
                    happy = False 
                    finish = True 
                #print(numlist)
            
        
        numhold.append(userinput2) #append new value to list 

    finish = True
    return happy



done = False # while loop by default stays false unless user chooses 3 

while not done:
    labMenu() #give the user choice to make a selection based on HW problem 
    choice = int(input('Please make an entry: '))

    if choice == 1:
        userinput = int(input('Please enter an integer value: '))
        prime = checkprime(userinput)
        if prime == True: 
            print("True")
        else:
            print("False")


    if choice == 2: 
        userinput = int(input("please enter an integer value: "))
        happy = happyNumCheck(userinput)
        if happy == True:
            print(str(userinput) + " is a happy number!")
        else:
            print(str(userinput) + " is a sad number!")

    if choice == 3: 
         userinput = int(input('Please enter an integer value: '))
         prime = checkprime(userinput) #combine both functions 
         happy = happyNumCheck(userinput) #function from choice 2 

         if prime and happy == True: #if both functions come up true, then we are set
             print('True')
         else:
             print("False")

    if choice == 4:
        finalList = [] #store values of list 
        x = str(input("Please enter in your list: ")) #enter in numbers with commas
        primeX = x.split(",") #split string into list 
        for userinput in primeX: #focus on userinput to be driven through program
            userinput = int(userinput)
            prime = checkprime(userinput)
            happy = happyNumCheck(userinput)
            if prime and happy == True: #if both functions come up true, then we are set
             finalList.append(userinput)
        print(finalList)

    if choice == 5:
        finalList = [] #store values of list 
        x = str(input("Please enter in your list: ")) #make sure to input 100 characters numbers with commas
        primeX = x.split(",") #split string into list 
        for userinput in primeX: #focus on userinput to be driven through program
            userinput = int(userinput)
            prime = checkprime(userinput)
            happy = happyNumCheck(userinput)
            if prime == True and happy == False: #check if values are sad and prime and add to list
             finalList.append(userinput)
        print(finalList) #spit out list 


    if choice == 6:
        done = True #end program 