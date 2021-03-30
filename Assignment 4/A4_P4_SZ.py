#November 6th, 2018 Sebastian 
# I have not given or received any unauthorized assistance on this assignment.”  
import random
import math
class ellipse(object):
    'Class that holds ellipse information'
    
    def __init__(self,Major,Minor):
        'Set up the primary numbers to calc the ellipse, major and minor axis '
        self.Major = Major # major axis radius 
        self.Minor = Minor #minor axis radius 
    
    def setFocli(self,Major,Minor,C1):
        'Figure out what the Folci points are in the ellipse'
        self.focli = round(math.sqrt(Major**2 - Minor**2),2) #formula to obtian focli points in ellipse 
        self.F1 = self.focli + C1 # set equal to folci 
        self.F2 = self.focli * -1 + C1  # give neg to get opposite side of axis 
        
        return (self.F1, self.F2)

    def setMajor_Minor_Axis(self,Major,Minor,C1,C2):
        'Set up the bounds of the ellipse '
       # self.fMajor = Major * 2 # double the major radius to get full major axis
       # self.fMinor = Minor * 2 # doulbe the minor radius to get full minor axis 
        self.V1 = Major + C1# upper bound of Major axis 
        self.V2 = Major * -1 - C1 # Lower bound of major axis
        self.V3 = Minor + C2  # Upper bound of minor axis 
        self.V4 = Minor * -1 + C2  #Lower bound of minor axis 
        self.vertList = [self.V1,self.V2,self.V3,self.V4]

        return (self.vertList)

    def setCenter(self,ellipseOne):
        'Set Center point of the ellipse'
        self.C1 = int(random.randint(-10,10)) #set center one 
        self.C2 = int(random.randint(-10,10)) #set center two 
        return (self.C1,self.C2) #return values into ellipse class 

    def Unit_setCenter(self,ellipseOne,X,Y):
        'Set up for unit test, to manual set center '
        print(" Set_Center FN : set up for unit test, to manual set center ")        
        self.C1 = X
        self.C2 = Y
        print("Center is " + str(self.C1) + " " + str(self.C2))
        return (self.C1,self.C2) #return values into ellipse class 

    def get(self):
        return (self.focli)


def labMenu(): #set up menu selection greet user
    'Menu Selection screen' #docstring
    print("Hello there! Plese follow the below instructions. ")
    print('Enter 1 for area and circumfrence of ellipse 1. ')
    print('Enter 2 for area and circumfrence of ellipse 2. ')
    print('Enter 3 for overlap of ellipses ')
    print('Enter 4 for unit testing ')
    print('Enter 5 to exit.')

def Major_Minor():
    'Set up Major and Minor Axis'
    final = False
    while not final:
        axisA = int(random.randint(3,15)) #random number gen
        axisB = int(random.randint(3,15)) # random number gen 
        if axisA == axisB: #make sure ellipse is an ellipse not a circle so points cant equal 
            axisA = int(random.randint(3,15))
            axisB = int(random.randint(3,15))
        if axisA > axisB:
            Major = axisA #set axis A as the major axis 
            Minor = axisB #set Axis B as the minor axis 
            final = True

    return Major,Minor






def circumference(Major,Minor):
    ' Unit test Calculate the circumference of the ellipse'
    print("Unit testCalculate the circumference of the ellipse")

    # formula for circumference of a circle using major and minor axis 
    circumference = math.pi * ( 3*(Major+Minor) - math.sqrt( (3*Major + Minor) * (Major + 3*Minor) ) )
    print("Circumference is " + str(circumference))
    return round(circumference,2)

def area(Major,Minor):
    'Calculate the area of the ellipse'
    print("Calculate the are of the ellipse Unit test")

    area = math.pi * Major * Minor
    print("Area is " + str(area))
    return round(area,2)

def pointCheck(ellipseObject):
    'Function used to check points on ellipse, if its in bounds '
    #print(ellipseObject)
    focal1 = [ellipseObject.F1,ellipseObject.C2] # set focal point one on axis 
    focal2 = [ellipseObject.F2,ellipseObject.C2] #set focal point 2 on axis 
    final = False
    while not final:
        x = random.randint(ellipseObject.V2,ellipseObject.V1) #set up random point 
        y = random.randint(ellipseObject.V2,ellipseObject.V1) #set up random point 
        point = [x,y] #set cord 
        d1 = ((point[0] - (focal1[0]))**2) + ((point[1] - (focal1[1]))**2)
        d2 = ((point[0] - (focal2[0]))**2) + ((point[1] - (focal2[1]))**2)

        d1 = math.sqrt(d1)
        d2 = math.sqrt(d2)

        dist = d1 + d2 # get distance of points add together 
        if d1 + d2 == ellipseObject.Major * 2: #make sure distance of point(x,y) is same equal to sum of major axis distance 
            print("point is good ")
            final = True     


def checkpoint(ellipseObject,point):
    'Function used to check if point falls into ellipse'
    E1 = 0 # set to 0 
    focal1 = [ellipseObject.F1,ellipseObject.C2] # set focal point one on axis 
    focal2 = [ellipseObject.F2,ellipseObject.C2] #set focal point 2 on axis 

        #point = [x,y] #set cord 
    d1 = ((point[0] - (focal1[0]))**2) + ((point[1] - (focal1[1]))**2)
    d2 = ((point[0] - (focal2[0]))**2) + ((point[1] - (focal2[1]))**2)

    d1 = math.sqrt(d1)
    d2 = math.sqrt(d2)

    dist = d1 + d2 # get distance of points add together 
    if dist <= ellipseObject.Major * 2: #make sure distance of point(x,y) is same equal to sum of major axis distance 
        E1 = 1 #give value of 1 if its a match 
    return E1



def boxSetUp(ellipseOne,ellipseTwo):
    'Set up bounds of box for ellipses'
    boxMaxX = max(ellipseOne.V1,ellipseTwo.V1) # get max x vert  ellipse 1 or 2 
    boxMinX= min(ellipseOne.V2,ellipseTwo.V2) # get min x vert of ellipse 1 or 2

    boxMaxY = max(ellipseOne.V3,ellipseTwo.V3) # get max vert of y axis 
    boxMinY = min(ellipseOne.V4,ellipseTwo.V4) # get min vert of y axis 

    xBound = [boxMaxX + 0,boxMinX - 0]
    yBound = [boxMaxY + 0, boxMinY - 0] 

    boxArea = (abs(xBound[0]) + abs(xBound[1])) * (abs(yBound[0] + abs(yBound[1]))) #get area of the box 

    return xBound, yBound, boxArea


def OverlapFn(ellipseOne,ellipseTwo,xBound, yBound, boxArea):
    'Calculate the overlap between the two ellipses'
    n = 0 # set to 0
    hit = 0  # set to 0 for amount of times point falls within 
    full = False # set while condtion to false, once it hits 10000 then its true 

    while not full:
        point = [int(random.randint(xBound[1],xBound[0])),int(random.randint(yBound[1],yBound[0]))] # make random points within bounds of box 
        #print (point)
        E1 = checkpoint(ellipseOne,point) #check and see if point falls into ellipse 1 
        E2 = checkpoint(ellipseTwo,point) #check and see if point falls into ellipse 2

        if E1 == 1 and E2 == 1: #point must fall into both ellipse to be true 
            hit += 1 # count how many times point falls between both ellipse 

        n += 1 # add to counter 
        if n == 100000:
            full = True # once all points have been hit, make while true 
            OverLapArea = (hit/boxArea) / 2 #Calculate the overlap between the ellipses hits over the box area 

    return round(OverLapArea,2)
#(random.randint(xBound[1],xBound[0]))

done = False
while not done:
    labMenu()
    choice = int(input('Please make an entry: '))

    if choice == 1:
      # set up ellipse 1 
        Major, Minor = Major_Minor() # Get the major radius and minor radius axis of Ellipse 
        ellipseOne = ellipse(Major,Minor) #set bounds of Major radius and Minor Axis radius 
        ellipseOne.setCenter(ellipseOne) #get center point / location of ellipse 
        focal = ellipseOne.setFocli(ellipseOne.Major,ellipseOne.Minor,ellipseOne.C1) #get main focal points
        ellipseOne.setMajor_Minor_Axis(ellipseOne.Major,ellipseOne.Minor,ellipseOne.C1,ellipseOne.C2) # get upper/lower bounds of axis
        areaCalc = area(ellipseOne.Major,ellipseOne.Minor) #calc the area of the ellipse 
        circumferenceCalc = circumference(ellipseOne.Major,ellipseOne.Minor) # get circumference of the ellipse 
        print("The circumference of the ellipse 1 is "+ str(circumferenceCalc))
        print("The area of the ellipse 1 is " +str(areaCalc))

    elif choice == 2:
        #Ellipse 2 setup
        Major, Minor = Major_Minor() # Get the major radius and minor radius axis of Ellipse 
        ellipseTwo = ellipse(Major,Minor) #set bounds of Major radius and Minor Axis radius 
        ellipseTwo.setCenter(ellipseTwo) #get center point / location of ellipse 
        focal = ellipseTwo.setFocli(ellipseTwo.Major,ellipseTwo.Minor,ellipseTwo.C1) #get main focal points
        ellipseTwo.setMajor_Minor_Axis(ellipseTwo.Major,ellipseTwo.Minor,ellipseTwo.C1,ellipseTwo.C2) # get upper/lower bounds of axis
        areaCalc = area(ellipseTwo.Major,ellipseTwo.Minor) #calc the area of the ellipse 
        circumferenceCalc = circumference(ellipseTwo.Major,ellipseTwo.Minor) # get circumference of the ellipse 
        print("The circumference of the ellipse 2 is "+ str(circumferenceCalc))
        print("The area of the ellipse 2 is " +str(areaCalc))

    elif choice == 3:
        #Get ellipse 1 
        Major, Minor = Major_Minor() # Get the major radius and minor radius axis of Ellipse 
        ellipseOne = ellipse(Major,Minor) #set bounds of Major radius and Minor Axis radius 
        ellipseOne.setCenter(ellipseOne) #get center point / location of ellipse 
        focal = ellipseOne.setFocli(ellipseOne.Major,ellipseOne.Minor,ellipseOne.C1) #get main focal points
        ellipseOne.setMajor_Minor_Axis(ellipseOne.Major,ellipseOne.Minor,ellipseOne.C1,ellipseOne.C2) # get upper/lower bounds of axis
        areaCalc = area(ellipseOne.Major,ellipseOne.Minor) #calc the area of the ellipse 
        circumferenceCalc = circumference(ellipseOne.Major,ellipseOne.Minor) # get circumference of the ellipse 
        print("The circumference of the ellipse 1 is "+ str(circumferenceCalc))
        print("The area of the ellipse 1 is " +str(areaCalc))

        # Get ellipse 2 
        Major, Minor = Major_Minor() # Get the major radius and minor radius axis of Ellipse 
        ellipseTwo = ellipse(Major,Minor) #set bounds of Major radius and Minor Axis radius 
        ellipseTwo.setCenter(ellipseTwo) #get center point / location of ellipse 
        focal = ellipseTwo.setFocli(ellipseTwo.Major,ellipseTwo.Minor,ellipseTwo.C1) #get main focal points
        ellipseTwo.setMajor_Minor_Axis(ellipseTwo.Major,ellipseTwo.Minor,ellipseTwo.C1,ellipseTwo.C2) # get upper/lower bounds of axis
        areaCalc = area(ellipseTwo.Major,ellipseTwo.Minor) #calc the area of the ellipse 
        circumferenceCalc = circumference(ellipseTwo.Major,ellipseTwo.Minor) # get circumference of the ellipse 
        print("The circumference of the ellipse 2 is "+ str(circumferenceCalc))
        print("The area of the ellipse 2 is " +str(areaCalc))

        # set up overlap function 
        xBound, yBound, boxArea = boxSetUp(ellipseOne,ellipseTwo) #grab the bounds of the box around ellipse / area as well

        OverLapArea = OverlapFn(ellipseOne,ellipseTwo,xBound, yBound, boxArea) #overlap function to calc overlap 
        print("The Overlap of the two ellipses is "+ str(OverLapArea))
        
    elif choice == 4:
        print("Unit test of Ellipse")
        
        #set up small ellipse 1
        ellipseOne = ellipse(3,1) #set bounds of Major radius and Minor Axis radius unit test 
        print("The major axis is 3 and minor axis is 1")
        ellipseOne.Unit_setCenter(ellipseOne,0,0) #set center to 0 Unit test 
        focal = ellipseOne.setFocli(ellipseOne.Major,ellipseOne.Minor,ellipseOne.C1) #get main focal points
        ellipseOne.setMajor_Minor_Axis(ellipseOne.Major,ellipseOne.Minor,ellipseOne.C1,ellipseOne.C2) # get upper/lower bounds of axis
        areaCalc = area(ellipseOne.Major,ellipseOne.Minor) #calc the area of the ellipse 
        circumferenceCalc = circumference(ellipseOne.Major,ellipseOne.Minor) 
        print("The circumference of the ellipse 1 is "+ str(circumferenceCalc)) # print our circum of test ellipse 
        print("The area of the ellipse 1 is " +str(areaCalc)) #print out area of test ellipse 1 

        #Set up large Ellipse 2
        ellipseTwo = ellipse(9,5) #set bounds of Major radius and Minor Axis radius unit test 
        print("The major axis is 9 and minor axis is 5")
        ellipseTwo.Unit_setCenter(ellipseTwo,0,0) #set center to 0 Unit test 
        focal = ellipseTwo.setFocli(ellipseTwo.Major,ellipseTwo.Minor,ellipseTwo.C1) #get main focal points
        ellipseTwo.setMajor_Minor_Axis(ellipseTwo.Major,ellipseTwo.Minor,ellipseTwo.C1,ellipseTwo.C2) # get upper/lower bounds of axis
        areaCalc = area(ellipseTwo.Major,ellipseTwo.Minor) #calc the area of the ellipse 
        circumferenceCalc = circumference(ellipseTwo.Major,ellipseTwo.Minor) 
        print("The circumference of the ellipse 2 is "+ str(circumferenceCalc)) # print our circum of test ellipse 2
        print("The area of the ellipse 2 is " +str(areaCalc)) #print out area of test ellipse 2


        #Set up ellipse 3 off centered  
        ellipseThree = ellipse(3,1) #set bounds of Major radius and Minor Axis radius unit test 
        print("The major axis is 3 and minor axis is 1")
        ellipseThree.Unit_setCenter(ellipseThree,5,5) #set center to 5,5Unit test  no overlap should occur
        focal = ellipseThree.setFocli(ellipseThree.Major,ellipseThree.Minor,ellipseThree.C1) #get main focal points
        ellipseThree.setMajor_Minor_Axis(ellipseThree.Major,ellipseThree.Minor,ellipseThree.C1,ellipseThree.C2) # get upper/lower bounds of axis
        areaCalc = area(ellipseThree.Major,ellipseThree.Minor) #calc the area of the ellipse 
        circumferenceCalc = circumference(ellipseThree.Major,ellipseThree.Minor) 

        print("The circumference of the ellipse 3 is "+ str(circumferenceCalc)) # print our circum of test ellipse 3
        print("The area of the ellipse 3 is " +str(areaCalc)) #print out area of test ellipse 3 

        #Set up large ellpise 4 to overlap with ellipse 2 
        ellipseFour = ellipse(11,9) #set bounds of Major radius and Minor Axis radius unit test 
        print("The major axis is 11 and minor axis is 9")
        ellipseFour.Unit_setCenter(ellipseFour,0,0) #set center to 0,0 Unit test 
        focal = ellipseFour.setFocli(ellipseFour.Major,ellipseFour.Minor,ellipseFour.C1) #get main focal points
        ellipseFour.setMajor_Minor_Axis(ellipseFour.Major,ellipseFour.Minor,ellipseFour.C1,ellipseFour.C2) # get upper/lower bounds of axis
        areaCalc = area(ellipseFour.Major,ellipseFour.Minor) #calc the area of the ellipse 
        circumferenceCalc = circumference(ellipseFour.Major,ellipseFour.Minor) 

        print("The circumference of the ellipse 4 is "+ str(circumferenceCalc)) # print our circum of test ellipse 4
        print("The area of the ellipse 4 is " +str(areaCalc)) #print out area of test ellipse 4 
        
        print("Test Ellipse 1 and 2 overlap area Ellipse one should be within ellipse 2  ")
        #Set up Ellipse 1 and 2, see if the area of overlap = ellipse 1 
        xBound, yBound, boxArea = boxSetUp(ellipseOne,ellipseTwo) #grab the bounds of the box around ellipse / area as well

        OverLapArea = OverlapFn(ellipseOne,ellipseTwo,xBound, yBound, boxArea) #overlap function to calc overlap 
        print("The Overlap of the two ellipses is "+ str(OverLapArea))

        print("Test Ellipse 2 and 1 overlap area, see if points are similar ")
        OverLapArea = OverlapFn(ellipseTwo,ellipseOne,xBound, yBound, boxArea)
        print("The Overlap of the two ellipses is "+ str(OverLapArea))

        print("test Ellipse 1 and 3, make sure that overlap area is 0, due to center being off ")
        xBound, yBound, boxArea = boxSetUp(ellipseOne,ellipseThree)
        OverLapArea = OverlapFn(ellipseOne,ellipseThree,xBound, yBound, boxArea)
        print("The Overlap of the two ellipses is "+ str(OverLapArea))

        print("test Ellipse 2 and 4, check large overlap area ")
        xBound, yBound, boxArea = boxSetUp(ellipseTwo,ellipseFour)
        OverLapArea = OverlapFn(ellipseTwo,ellipseFour,xBound, yBound, boxArea)
        print("The Overlap of the two ellipses is "+ str(OverLapArea))

    else:
        done = True 

