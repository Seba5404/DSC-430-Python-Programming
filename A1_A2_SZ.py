#Sebastian Zdarowski 
#“I have not given or received any unauthorized assistance on this assignment.”  
#September 24, 2018 
import math

done = False
def labMenu():
    'Menu Selection screen' #docstring
    print('Enter 1 to check if list contains exactly 3 ints: ')
    print('Enter 2 to check if list is a valid square: ')
    print('Enter 3 to enter in a list value and return the perimeter: ')
    print('Enter 4 to enter in a list value and return the area: ')
    print('Enter 5 to enter two list values and to compute the area of overlap between squares: ')
    print('Enter 6 if you are done: ')

def intcount(userlist): #check if user entered in a valid list with int values
    'Count INT from user list'
    userlist = userlist.split(",")
    #print(userlist)
    newlist = []
    for x in userlist:
        
        if len(userlist) != 3: #if length is not equal to 3 leave loop, entry is not valid
            newlist = False
            break #exit for loop

        try:
            if type(int(x)) == int: #if value is an int it will make a new list
                newlist.append(int(x))
        except ValueError: #incase of error catch and label new list false
            newlist = False
            break #exit for loop
    return newlist

def Checksquare(newlist):
    'Check if the value inputted by user is valid'
    valid = True 
    if newlist[2] < 0: #if third integer lower than 0 call it false
        valid = False
    return valid


def perimetercalc(newlist): #calculate perimeter
    'Calculate the permiter user input' #docstring
    s = newlist[2]
    calc = s * 4
    return calc 

def areacalc(newlist):
    'calculate area of square user input' #docstring
    s = newlist[2]
    calc = s**2
    return calc


def calcOverLap(x,y):
    X1 = int(x[0]) # Place numbers from list into single variables / Xaxis 1 
    Y1 = int(y[0]) # X axis 2 
    X2 = int(x[1]) # Y axis 1 
    Y2 = int(y[1]) # Y Axis 2 
    X3 = int(x[2]) #S1 
    Y3 = int(y[2])  #S2
    
    L1 = [X1,Y1] # Get Vertical placment of square 1
    L2  = [(X1 + X3),(Y1 + X3)] #Get Vertical placment of square 2
    R1 = [X2,Y2] #get Horzontial distance of square 1
    R2 = [(X2 + X3), (Y2 + Y3)] #get Horzontial distance of square 2
   
    mxAxis = max(L1) #Get Max of X axis
    minXaxis = min(L2) # Get min of X axis 
    myAxis = max(R1) # Get Max of Y axis
    minYaxis = min(R2) # Get min of Y axis
    
    
    vertDist = minYaxis - myAxis # Calc overlap of Vert
    horzdist = minXaxis - mxAxis #Calc overlap of Horz
    
    if vertDist <= 0: #incase we get a negative value, give a 0 
        vertDist = 0
    if horzdist <= 0: #incase we get a negative value, give a 0 
        horzdist = 0
    
  
    overLap = vertDist * horzdist # Get area of overlap 

    print("The overlap area is " +str(overLap)) #print out result

    #print(str(overLap))

while not done:
    labMenu() #give the user choice to make a selection based on HW problem 
    choice = int(input('Please make an entry: '))

    if choice == 1:
       
        userlist = input("Please enter a list of 3 numbers, enter in a list as such X,Y,Z: ")
        newlist = intcount(userlist)
       
        if newlist != False:
            print("TRUE")
        else:
            print("FALSE")

    elif choice == 2:
        
        userlist = input("Please enter a list of 3 numbers, enter in a list as such X,Y,Z: ")
        newlist = intcount(userlist)
       
        if newlist != False:
            #'print("TRUE")
            valid = Checksquare(newlist) #Check if valid square function
            if valid == True:
                print("TRUE") #if value is above 0 
            else:
                print("FALSE") #if value is below 0 

        else:
            print("FALSE")

    elif choice == 3:
        
        userlist = input("Please enter a list of 3 numbers, enter in a list as such X,Y,Z: ")
        newlist = intcount(userlist)
       
        if newlist != False:
            #'print("TRUE")
            valid = Checksquare(newlist) #Check if valid square function
            if valid == True:
                calc = perimetercalc(newlist)
                print("The perimeter is " + str(calc))
    
        else:
                print("-1") #if value is below 0 

    elif choice == 4:
        userlist = input("Please enter a list of 3 numbers, enter in a list as such X,Y,Z: ")
        newlist = intcount(userlist)
       
        if newlist != False:
            #'print("TRUE")
            valid = Checksquare(newlist) #Check if valid square function
            if valid == True:
                calc = areacalc(newlist) #call function
                print("The area is " + str(calc))
    
        else:
                print("-1") #if list is invalid
    
    elif choice == 5:
        userlist = input("Please enter a list of 3 numbers for 1st list, enter in a list as such X,Y,Z: ")
        userlist2 = input("Please enter a list of 3 numbers for 2nd list, enter in a list as such X,Y,Z: ")
        newlist1 = intcount(userlist) #check if they are valid entries
        newlist2 = intcount(userlist2)# check if they are valid entries
        if newlist1 and newlist2 != False:
            print("Inputs are valid")
            x = userlist.split(",")
            y = userlist2.split(",")
            calcOverLap(x,y)

        else:
            print("-1") #if list is invalid
            


    elif choice == 6:
        done = True


