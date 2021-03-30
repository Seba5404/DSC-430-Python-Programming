#Sebastian Zdarowski 
#I have not given or received any unauthorized assistance on this assignment
#OCT 8th, 2018

# function to import names of text files
def import_list(y):
    'Import function, brings in y which is the text file'
    temp_text_file = open(y, "r") # open text file 
    
    tempData = temp_text_file.read()
    tempList = tempData.splitlines() #split each name into list
    return tempList


def count_list(x): #count how many times letter ends in baby name
    'Function that counts how many times letter ends, brings in text list'
    temphold = []
    finalList = []
    i = range(97, 123) #range of numbers for ascii
    

    #get last letter of each name 
    for n in x:
        temphold.append(n[-1]) # hold each last letter
    
    for y in i: #cycle through range 97 to 120 
        count = 0 
        for n in temphold: # go through each letter 
            
            if chr(y) == n:
                count += 1 #increase count if match end letter
        #print(count)
        holdList = [y,count]
        finalList. append(holdList) #append double arrary to list 
        #print(chr(y))
    
    #print(finalList)
        


    return finalList


# in Idle I dont need to add path, Visual Studio gave issues so had to put in pathname in file name
#when running test, make sure you change pathname
boyTextString = 'namesBoys.txt' #for IDLE
girlTextString = 'namesGirls.txt' #for IDLE
#boyTextString = "/Users/Sebastian/Graduate School/DSC 430 Python Programming/A2_HW/namesBoys.txt" #for Visual Code
#girlTextString = "/Users/Sebastian/Graduate School/DSC 430 Python Programming/A2_HW/namesGirls.txt" #for Visual Code


# grab names of each txt files 
boyName = import_list(boyTextString) #call import_list function
girlName = import_list(girlTextString)

boyCount = count_list(boyName)
girlCount = count_list(girlName)
i = range(00, 26)
#print(boyCount)
#print(girlCount)

#print("Ending    Boys    Girls")
heading = '{:5} {:5} {:5}'.format('Ending','Boys','Girls')
print(heading)
for x in i: 
    char = chr(boyCount[x][0])
    boyC = boyCount[x][1]
    girlC = girlCount[x][1]

    #print(char +"        "+str(boyC)+"       "+str(girlC))

    print('{:5} {:5} {:5}'.format(str(char),(boyC),(girlC))) #format text 

# differences in naming list 
# Girls seem to have more names ending in A and Y than boys do, Boys, tend to have
# most names ending in N and E. There are no names that end in Q for both genders
#Boys tend to have names that end in all letters of alphabet besides q unlike girl names
   










