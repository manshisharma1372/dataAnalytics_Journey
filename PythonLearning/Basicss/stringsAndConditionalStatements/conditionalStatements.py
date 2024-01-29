age=18
if (age>18):
    print("eligible to vote")
    
elif(age==18):
    print("can do something")    
else:
    print("cannot vote not eligible")
    
    
#*****************************************************************************8

#Grade students based on marks

marks=55
if(marks>=90):
    print("A")
elif(marks<90 and marks>=80):
    print("B")
elif(marks<80 and marks>=70):
    print("C")
else:
    print("D") #D 
    
#****************************************************************************************
#NESTING IN C++

age=34
if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("yes can drive")
            
else:
    print("cannot drive")
#yes can drive