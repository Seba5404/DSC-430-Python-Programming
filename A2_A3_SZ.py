#“I have not given or received any unauthorized assistance on this assignment
#Sebastian Zdarowski 
#OCT 22 2018

import statistics
import math

def labMenu(): #set up menu selection greet user
    'Menu Selection screen' #docstring
    print("Hello there! Plese follow the below instructions. ")
    print('Enter 1 for problem a. ')
    print('Enter 2 for problem b. ')
    print('Enter 3 for problem c. ')
    print('Enter 4 for problem d. ')
    print('Enter 5 for problem e. ')
    print('Enter 6 to exit.')


def bringInData(text_file_name,column_name):
    'Function that brings in data and sorts list' #docstring
    temp_text_file = open(text_file_name, "r") # open text file 
    tempData = temp_text_file.readlines()
    tempLoc = tempData[0].split(',')
    loc = tempLoc.index(column_name) #find location of total volume
    tempData.pop(0) #remove title called TOTAL VOLUME 
    tempList = [] #hold list values 
    for x in tempData: #bring in column TOTAL VOLUME 
        tempList.append(float(x.split(',')[loc])) #volume is 4th column gets 3 value
    #tempList.pop(0) #remove title called TOTAL VOLUME 
    return tempList


def mean_HG(AvoList):
    'Homegrown code to compute mean'
    sumValue = sum(AvoList) #sum value of mean 
    lengthList = len(AvoList)

    mean_Home = sumValue/lengthList
    mean_Home = round(mean_Home,9) #round mean to 9 digits same as stats function 
    print("Mean is " +str(mean_Home))
    return mean_Home

def sd_HG(AvoList,mean_HG):
    'homegrown code to compute std Dev'
    topVar = 0 #set up value 
    for x in AvoList:
        var = mean_HG - x
        topVar += (var)**2 #sum of values in varaince 
    lengthList = len(AvoList)

    totalVar = topVar/(lengthList - 1) #divide up all variance values by length of list 

    sqrt = totalVar**(1/2.0) #sqrt the function
    print("STD is  " + str(sqrt)) #print SQRT
    return sqrt #return hold value 


def median_HG(AvoList):
    'cacl out median using avo list'
    lengthList = len(AvoList) #get length of list 
    if lengthList % 2 == 1: #if List is odd numbered
        AvoList.sort() #sort list 
        val = len(AvoList) // 2
        medianList = AvoList[int(val)] #get index value


    else: #if Even list 
        AvoList.sort(reverse = False) #sort list 
        middleList = lengthList/2 #get middle of list 
        lowMiddleList = middleList - .5 #get lower end
        highMiddleList = middleList + .5 #get higher end due to odd number
        lowVal = float(AvoList[int(lowMiddleList)])
        highval = float(AvoList[int(highMiddleList)])
        (medianList) = (lowVal + highval) / 2
    
    print("Median is " + str(medianList))


def mean_MMLF(text_file_name,column_name):
    'Function that computes MML Mean' #docstring
    temp_text_file = open(text_file_name, "r") # open text file 
    tempData = temp_text_file.readline()
    tempLoc = tempData.split(',')
    loc = tempLoc.index(column_name) #find location of total volume
    #tempData.pop(0) #remove title called TOTAL VOLUME 
    counter = 0
    AvoSum = 0 
    tempData = temp_text_file.readline()
    
    while tempData: # go until line is empty
        AvoList = tempData.split(",") #bring in column TOTAL VOLUME 
        AvoSum += float(AvoList[loc])
        counter += 1
        #print("1")
        tempData = temp_text_file.readline() #read next line 
            
    mean = AvoSum/counter #formula for mean 
    
    #tempList.pop(0) #remove title called TOTAL VOLUME 
    return mean

def std_MMLF(temp_text_file,column_name,mean_MML):
    'Function that computes MML STD ' #docstring
    temp_text_file = open(temp_text_file, "r") # open text file 
    tempData = temp_text_file.readline()
    tempLoc = tempData.split(',')
    loc = tempLoc.index(column_name) #find location of total volume
    #tempData.pop(0) #remove title called TOTAL VOLUME 
    counter = 0 #keep track amount of values 
    topVar = 0
    tempData = temp_text_file.readline()
    
    while tempData: # go until line is empty
        AvoList = tempData.split(",") #bring in column TOTAL VOLUME 
        stdDevValue = float(AvoList[loc])
        counter += 1
        var = mean_MML - stdDevValue #subtract value from mean 
        topVar += (var)**2 

        tempData = temp_text_file.readline() #read next line 
    
    totalVar = topVar/(counter - 1) #divide up all variance values by length of list 

    sqrt = totalVar**(1/2.0)
    
    return sqrt

def setupBins(counter,minValue,maxValue,temp_text_file,column_name):
    'function to get bounds of the list file'
    temp_text_file = open(temp_text_file, "r") # open text file 
    tempData = temp_text_file.readline()
    tempLoc = tempData.split(',')
    loc = tempLoc.index(column_name) #find location of total volume
    #tempData.pop(0) #remove title called TOTAL VOLUME 
    #counter = 0 #keep track amount of values 
    tempData = temp_text_file.readline()

    HoldBins = [0,0,0,0,0,0,0,0,0,0,0,0] #set up bins to hold 12 values
    step = (maxValue - minValue) / 10 
    while tempData: # go until line is 
        AvoList = tempData.split(",")
        tempVal = float(AvoList[loc])

        if tempVal < minValue:
            HoldBins[0] = HoldBins[0] + 1
        #if tempVal > maxValue:
         #   HoldBins[11] = HoldBins[11] + 1

        for i in range(10):
            lower = minValue + step * i
            upper = minValue + step * (i+1)

            if(tempVal >= lower and tempVal < upper):
                HoldBins[i+1] = HoldBins[i+1] + 1 #push out numbers and only keep 10 numbers within each lists

        tempData = temp_text_file.readline()

    return HoldBins #return bins

def findMed(temp_text_file,column_name,counter,minValue,maxValue):
    'function to get bounds of the list file'
    temp_text_file = open(temp_text_file, "r") # open text file 
    tempData = temp_text_file.readline()
    tempLoc = tempData.split(',')
    loc = tempLoc.index(column_name) #find location of total volume
    #tempData.pop(0) #remove title called TOTAL VOLUME 
    count = 0 #keep track amount of values 
    tempData = temp_text_file.readline()
    med = 0
    holdList = [0,0,0,0,0,0,0,0,0,0]
    while tempData: # go until line is empty
        AvoList = tempData.split(",") #bring in column TOTAL VOLUME 
        holdValue = float(AvoList[loc])
        
        if holdValue > minValue and holdValue < maxValue:
            med = holdValue
            count += 1
            for i in range(9):
                if med > float(holdList[i]):
                    holdList[i] = med
                    holdList.sort(reverse = False)
                    break


        tempData = temp_text_file.readline() #read next line

    return med

def displayholdlist(holdList,counter): #display our values within the lists 
    'Display list values '
    value = 0 
    for i in range((len(holdList))):
        c = holdList[i]
        value += c 
        print("{:8}{:8}{:8}{:20}".format(i,c,value,(value/counter))) #print out the lists
 

def newMinMax(holdList,counter,minValue,maxValue):
    'Set up new min and max values based of new HoldLists'
    value = 0 
    step = (maxValue - minValue)/10

    for i in range(len(holdList)):
        value = value + holdList[i]
        percentage = value/counter
        if (percentage > 0.5): #if the percentage is lower than .5 set a new min value 
            return ((minValue +step*(i-1),(minValue +step * i)))
    
    return 0

def getGoodCount(holdList):
    'Set list values equal'
    value = 0 
    for i in range(1,11):
        value += holdList[i] # add up range of values to keep count of bounds 

    return value

def median_MMLF(temp_text_file,column_name):
    'Calculate the median MML function '
    counter, minValue, maxValue = boundLoc(temp_text_file,column_name) #get min max and count of how many rows we have 
    goodCount = counter # set count of all values to goodCount

    while goodCount > 1: #keep count of rows within file and continue looping 
        holdList = setupBins(counter,minValue,maxValue,temp_text_file,column_name) #set up list to hold values 
        minValue,maxValue = newMinMax(holdList,counter,minValue,maxValue) #Set new min and max after bins get calculated
        goodCount = getGoodCount(holdList)
    
    med = ((maxValue + minValue) / 2) #calculate the median from min and max values 



    return med

def boundLoc(temp_text_file,column_name):
    'function to get bounds of the list file'
    temp_text_file = open(temp_text_file, "r") # open text file 
    tempData = temp_text_file.readline()
    tempLoc = tempData.split(',')
    loc = tempLoc.index(column_name) #find location of total volume
    #tempData.pop(0) #remove title called TOTAL VOLUME 
    counter = 0 #keep track amount of values 
    tempData = temp_text_file.readline()
    
    AvoList = tempData.split(",") #split single line
    
    minValue = float(AvoList[loc]) # set min value
    maxValue = float(AvoList[loc]) #set max value

    while tempData: # go until line is empty
        AvoList = tempData.split(",") #bring in column TOTAL VOLUME 
        holdValue = float(AvoList[loc])
        counter += 1

        if holdValue < minValue: #if less than minValue change it
            minValue = holdValue
        
        if holdValue > maxValue: #if greater than max value change it
            maxValue = holdValue

        tempData = temp_text_file.readline() #read next line

    return counter,minValue,maxValue




done = False

while not done:
    labMenu()
    temp_text_file = "avocado.csv" # For IDLE 
    #temp_text_file = "/Users/Sebastian/Graduate School/DSC 430 Python Programming/A2_HW/avocado.csv" #for Visual Code testing
    column_name = "Total Volume" #column name that we pull in 
    choice = int(input('Please make an entry: '))

    if choice == 1:
        AvoList = bringInData(temp_text_file,column_name)
        mean_SM = statistics.mean(AvoList) #get mean for problem A
        print("Mean is " +str(mean_SM)) # print problem A


    elif choice == 2:
        AvoList = bringInData(temp_text_file,column_name)
        sd_SM = statistics.stdev(AvoList) #get StdDev of List probelm b
        print("STD dev is " + str(sd_SM)) # print problem B

    elif choice == 3:
        AvoList = bringInData(temp_text_file,column_name)
        median_SM = statistics.median(AvoList)
        print("Median is " +str(median_SM)) # print problem C

    elif choice == 4:
        AvoList = bringInData(temp_text_file,column_name)
        mean_Home = mean_HG(AvoList) #HG code to compute mean
        std_home = sd_HG(AvoList,mean_Home) #HG code to compute STD Dev
        median_Home = median_HG(AvoList) #hg code to compute median 

    elif choice == 5:
        mean_MML = mean_MMLF(temp_text_file,column_name) #function to compute mean
        std_MML = std_MMLF(temp_text_file,column_name,mean_MML) #function to compute STD Dev
        median_MML = median_MMLF(temp_text_file,column_name)

        print("Mean is " + str(round(mean_MML,2)))
        print("STD is " + str(round(std_MML,2)))
        print("Median is " + str(round(median_MML,2)))
    else:
        done = True 

    
    
    
   




