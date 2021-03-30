#“I have not given or received any unauthorized assistance on this assignment
#Sebastian Zdarowski 
#OCT 8 2018

def labMenu(): #set up menu selection greet user
    'Menu Selection screen' #docstring
    print("Hello there! Plese follow the below instructions. ")
    print('Enter 1 to pull in first stem plot. ')
    print('Enter 2 to pull in second stem plot. ')
    print('Enter 3 to pull in third stem plot. ')
    print('Enter 4 if you are done.')

def bringInData(text_file_name):
    'Function that brings in data and sorts list' #docstring
    temp_text_file = open(text_file_name, "r") # open text file 
    tempList =[] #create empty list to number values
    for x in temp_text_file.read().split(): #convert to interger so we can sort value low to high
        tempList.append(int(x))
    temp_text_file.close()
    tempList.sort() #sort numbers
 
    return tempList

def Stem_Leaf(stemData): #set up DICT
    'set up Dict for text files, input is the text file brought in from bringinData function'
    maxValue =max(stemData) #Get Max Value of List 
    minValue =min(stemData) #get Min Value of List
    stemLeafDict ={} #dict value
    maxLen  = len(str(maxValue)) - 1 #get length of maxvalue for stem
    minLen = len(str(minValue)) - 1  #get Length of min value for stem

    stemList = [] #list to hold stem values 
    for x in stemData: #get Stems from the list 
        if len(str(x)) - 1 == minLen: #min value of stem length  
             y = int(str(x)[:minLen]) #slice of starting digit based on min value
             if y not in stemList:
               stemList.append(y)
        elif len(str(x)) - 1 == maxLen: #max value of stem length 
             y = int(str(x)[:maxLen]) #slice of starting digit based on max value 
             if y not in stemList:
               stemList.append(y)

    leafList = [] #hold Leaf values temp
    for x in stemList: #loop through stemlist 
        for y in stemData:
            z = len(str(y)) - 1
            v = int(str(y)[:z]) 
            if x == v: #if the steam value = leaf stem
                 t = int(str(y)[z:]) #grab last digits of leafs - stem
                 leafList.append(t) #append digit to temp leafList 
        tempDict = {x:leafList} #temp Dict 
        stemLeafDict.update(tempDict) # store temp Dict values into final DICT
        leafList = [] #clear temp list 

    return stemLeafDict #return final DICT containing all values 

def print_dict(finalDict): #print out stem/leaf plots of dict 
    'bring in finalDict value and print out stem/leaf plots'
    for keys in finalDict:
        space = "|"
        outputString = ""
        printList = finalDict[keys]
        printList.sort(reverse=True) #sort List in descending order 
        for x in printList: #loop through list within dict
            outputString = " " + str(x) + outputString #make one string value of all values in list
    
        print('{:3} {:1} {:5}'.format(str(keys),(space),(outputString))) #format text and print out



done = False # set to false to keep while loop going until user opts out 
while not done:
    labMenu()
    choice = int(input('Please make an entry: '))

    if choice == 1:
        text_file_name = "StemAndLeaf1.txt" #use for IDLE testing
        #text_file_name = "/Users/Sebastian/Graduate School/DSC 430 Python Programming/A2_HW/StemAndLeaf1.txt" #visual Code testing 
        stemData = bringInData(text_file_name) #Bring in file 
        finalDict = Stem_Leaf(stemData) #format DICT 
        print_dict(finalDict) #print out DICT values 

    elif choice == 2: 
        text_file_name = "StemAndLeaf2.txt" #use for IDLE testing 
        #text_file_name = "/Users/Sebastian/Graduate School/DSC 430 Python Programming/A2_HW/StemAndLeaf2.txt" #visual code testing 
        stemData = bringInData(text_file_name)
        finalDict = Stem_Leaf(stemData) #format DICT 
        print_dict(finalDict) #print out DICT values 

    elif choice == 3:
        text_file_name = "StemAndLeaf3.txt" #use for IDLE testing 
        #text_file_name = "/Users/Sebastian/Graduate School/DSC 430 Python Programming/A2_HW/StemAndLeaf3.txt" #visual Code testing 
        stemData = bringInData(text_file_name) #grab info from text
        finalDict = Stem_Leaf(stemData) # #format DICT 
        print_dict(finalDict) #print out DICT values 

    else:
        done = True
    
