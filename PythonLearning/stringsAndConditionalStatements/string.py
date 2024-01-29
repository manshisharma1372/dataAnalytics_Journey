str1="Hi my name is manshi \n"

str2='mannu also'

str3="""Mona too"""

# we use diff methods because
# "this is Manshi's directory"

#for nextline
#use escape sequence char
print(str1,str2)
print(str3)

#*****************************************************************************


#concatenation in string
a="hello"
b="geek"
print(a+b)

#find len of string
print(len(a))

newStr=a+" "+b
print(newStr)

#indexing
myStr="Manshi Sharma"
ch1=myStr[0]
print(ch1)
print(myStr[5])

#not possible
#myStr[0]='S''str' object does not support item assignment
 

#SLICING: accesing parts of a string
#str[startIndex : endIndex] here endIndex is not included

str="Geeksforgeeks"
print(str[0:4]) #GEEK
print(str[:4])  #Geeks
print(str[0:]) #Geeksforgeeks
print(str[0:len(str)]) #Geeksforgeeks

#negative indexing
str2="Apple"
print(str2[-5:-1]) #Appl



