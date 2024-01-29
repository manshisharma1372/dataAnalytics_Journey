#WAP to check if a number entered by user is odd or even

num=int(input("enter a number"))
if(num%2==0):
    print("even")
else:
    print("odd")    
    

#WAP to find the greatest of 3 numbers enterd by user
num1= int(input("enter a number 1"))
num2= int(input("enter a number 2 "))
num3= int(input("enter a number 3"))
if(num1>num2 and num1>num3):
    print("num1 is greatest")
elif(num2>num1 and num2>num3):
    print("num2 is greatest")
else:
    print("num3 is greatest")
    
    
#WAP to check if a number is a mutiple of 7 or not
x=14
if(x%7==0):
    print("yes")
else:
    print("No")        