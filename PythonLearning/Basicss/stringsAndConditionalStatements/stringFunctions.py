str="manshi sharma"
# endswith() return true if string ends with substr
print(str.endswith("Sharma")) #True
print(str.endswith("shandilya")) #False

#capitalize() capatilizes first char
print(str.capitalize())  #Manshi sharma
print(str) # remains same manshi sharma so do 
str=str.capitalize()
print(str) #Manshi sharma

#replace replaces all occurence of old str char with given char
str="iiiggghhhh"
print(str.replace("i","t")) #tttggghhhh

#find() return first occ index
st="where are u"
print(st.find("h")) #1
print(st.find("z")) #-1 

#count() count occ of substr in a str
stt="i me i too i am"
print(stt.count("i")) #3




