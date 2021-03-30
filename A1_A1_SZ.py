Fname = input("What is your first name?: ") # Hold First Name
Lname = input("What is your last name?: ") #Hold Last Name 
IQ = int(input("What is your IQ?: ")) #Hold IQ score


if IQ < 90: #If statement to run and decide if IQ is apporiate value
    Result = "you will get a D in DSC430." 
elif IQ > 90 and IQ <= 110:
    Result = "you will get a C in DSC430."
elif IQ > 110 and IQ <= 130:
    Result = "you will get a B in DSC430."
else:
    Result = "you are a liar!"

print(Fname + " " + Lname + " " + Result) #output results 


